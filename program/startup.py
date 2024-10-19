import winreg


class StartupManager():
    def __init__(self):
        pass

    def get_startup_apps(self):
        startup_apps = []
        registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,registry_path,0,winreg.KEY_READ)
        for i in range(0,winreg.QueryInfoKey(key)[1]):
            startup_apps.append(winreg.EnumValue(key,i))
        return startup_apps


    def remove_startup_app_by_name(self,app_name):
        registery_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,registery_path,0,winreg.KEY_SET_VALUE)

            winreg.DeleteValue(key,app_name)
            print(f"{app_name} removed from startup apps.")
        except FileNotFoundError:
            print(f"{app_name} could't be found!")
        except Exception as e:
            print(f"Error! Message -> {e}")

