from PyQt6.QtWidgets import QMainWindow
from forms.cleaning_form import Ui_form_cleaning


from managers.cleanermanager import Cleaner

class CleaningWindow(QMainWindow):
    def __init__(self):
        super(CleaningWindow,self).__init__()
        self.ui = Ui_form_cleaning()
        self.ui.setupUi(self)

        self.ui.btn_clean_temp_folder.clicked.connect(self.clean_temp_folder)
        self.ui.btn_clean_trash_bin.clicked.connect(self.clean_trash_bin)

        self.manager = Cleaner()

    def clean_trash_bin(self):
        self.manager.clean_recycle_bin()

    def clean_temp_folder(self):
        self.manager.clean_temp_folder()