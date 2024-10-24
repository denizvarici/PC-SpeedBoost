from PyQt6.QtWidgets import QMainWindow
from forms.main_form import Ui_Form_main


from windows.CleaningWindow import CleaningWindow
from windows.StartupWindow import StartupWindow
from windows.TaskWindow import TaskWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form_main() 
        self.ui.setupUi(self)    

        #window instances
        self.cleaning_window = CleaningWindow()
        self.startup_window = StartupWindow()
        self.taskmanager_window = TaskWindow()

        #window opener button clicked connects
        self.ui.btn_open_window_cleaning.clicked.connect(self.open_cleaning_window)
        self.ui.btn_open_window_startup.clicked.connect(self.open_startup_window)
        self.ui.btn_open_window_taskmanager.clicked.connect(self.open_taskmanager_window)


    #opening windows functions
    def open_cleaning_window(self):
        self.cleaning_window.show()
    def open_startup_window(self):
        self.startup_window.show()
    def open_taskmanager_window(self):
        self.taskmanager_window.show()