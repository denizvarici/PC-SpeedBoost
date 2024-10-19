import os
import shutil
import ctypes

class Cleaner():
    def __init__(self):
        self.temp_dir = os.environ['TEMP']

    def clean_temp_folder(self):
        for item in os.listdir(self.temp_dir):
            item_path = os.path.join(self.temp_dir,item)
            try:
                if os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                else:
                    os.remove(item_path)

            except:
                continue

    def clean_recycle_bin(self):
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(0, None, 0x00000001)
            print("recycle bin cleaned!")
        except:
            print("recycle bin could't cleaned")



cleaner = Cleaner()
cleaner.clean_recycle_bin()