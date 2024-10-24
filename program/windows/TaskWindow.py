from PyQt6.QtWidgets import QMainWindow,QMessageBox
from forms.taskmanager_form import Ui_form_taskmanager


from managers.taskmanager import TaskManager

import webbrowser


from PyQt6.QtCore import QStringListModel

class TaskWindow(QMainWindow):
    def __init__(self):
        super(TaskWindow,self).__init__()
        self.ui = Ui_form_taskmanager()
        self.ui.setupUi(self)


        self.selected_app_name = None

        self.setup_list_view()

        self.ui.listview_taskapps.clicked.connect(self.on_listview_item_clicked)
        self.ui.btn_kill_process.clicked.connect(self.kill_process)
        self.ui.btn_get_process_info.clicked.connect(self.open_web_and_search_for_process)
        self.ui.btn_reload_processes.clicked.connect(self.setup_list_view)


    def setup_list_view(self):
        self.manager = TaskManager()
        data = self.manager.processes
        formatted_data = [f"{appname}-{details}" for appname,details in data]
        self.data_model = QStringListModel()
        self.data_model.setStringList(formatted_data)
        self.ui.listview_taskapps.setModel(self.data_model)

    def on_listview_item_clicked(self,index):
        selected_item = self.data_model.data(index,0)
        app_name = selected_item.split('-')[0]
        self.selected_app_name = app_name

    

    def kill_process(self):
        if self.selected_app_name != None:
            self.manager.kill_process(self.selected_app_name)
            self.setup_list_view()
        else:
            QMessageBox.warning(self,"No process selected","Choose a process to kill")
    
    def open_web_and_search_for_process(self):
        if self.selected_app_name != None:
            query = f"what is {self.selected_app_name} in task manager ?"
            url = f"https://www.google.com/search?q={query}"

            webbrowser.open(url)


        else:
            QMessageBox(self,"No process selected","Choose a process to search on google.")