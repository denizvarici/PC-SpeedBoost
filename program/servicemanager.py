import psutil
import win32service

class ServiceManager():
    def __init__(self):
        self.services = self.get_services()
        self.service_names = self.get_only_service_display_names()

    def get_services(self):
        services = {}
        for service in psutil.win_service_iter():
            if service.status() == "running":
                services[service.display_name()] = service
        return services
    
    def get_only_service_display_names(self):
        service_names = []
        for name in self.services:
            service_names.append(name)
        return service_names
    
    def get_service_detail_by_display_name(self,serviceName):
        try:
            return self.services[serviceName]
        except:
            return None
        
    def stop_service_by_display_name(self,serviceName):
        if serviceName in self.services:
            try:
                service = self.services[serviceName]
                serviceName = service.name()
                if service.status() == "running":
                    svc = win32service.OpenService(win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS), serviceName, win32service.SERVICE_STOP)
                    win32service.ControlService(svc, win32service.SERVICE_CONTROL_STOP)
                    print("works")
            except Exception as e:
                print(e)
        else:
            print("no such service")
    

manager = ServiceManager()
print(manager.service_names)
