from PyQt6.QtWidgets import QMainWindow, QMessageBox
from forms.startup_form import Ui_form_startup

from PyQt6.QtCore import QStringListModel


from managers.startupmanager import StartupManager

class StartupWindow(QMainWindow):
    def __init__(self):
        super(StartupWindow,self).__init__()
        self.ui = Ui_form_startup()
        self.ui.setupUi(self)

        self.selected_app_name = None
        self.ui.btn_remove_from_startup_apps.clicked.connect(self.remove_app_from_startup)

        #implement data to listView
        self.setup_list_view()

        self.ui.listview_startupapps.clicked.connect(self.on_item_clicked_on_list_view)

    def setup_list_view(self):
        self.manager = StartupManager()
        data = self.manager.get_startup_apps()
        formatted_data = [f"{appname}-{path}-{isopen}" for appname,path,isopen in data]
        self.data_model = QStringListModel()
        self.data_model.setStringList(formatted_data)
        self.ui.listview_startupapps.setModel(self.data_model)
 
    def on_item_clicked_on_list_view(self,index):
        selected_item = self.data_model.data(index,0)
        app_name = selected_item.split('-')[0]
        self.selected_app_name = app_name
        #QMessageBox.information(self,"Selected Item",app_name)

    def remove_app_from_startup(self):
        if(self.selected_app_name != None):
            self.manager.remove_startup_app_by_name(self.selected_app_name)
            self.setup_list_view()
        else:
            QMessageBox.warning(self,"No App Selected","Please select an app from list to remove.")


