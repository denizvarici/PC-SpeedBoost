# Form implementation generated from reading ui file 'taskmanager_form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_form_taskmanager(object):
    def setupUi(self, form_taskmanager):
        form_taskmanager.setObjectName("form_taskmanager")
        form_taskmanager.resize(821, 432)
        self.lbl_header = QtWidgets.QLabel(parent=form_taskmanager)
        self.lbl_header.setGeometry(QtCore.QRect(220, 20, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_header.setFont(font)
        self.lbl_header.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
        self.lbl_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_header.setObjectName("lbl_header")
        self.listview_taskapps = QtWidgets.QListView(parent=form_taskmanager)
        self.listview_taskapps.setGeometry(QtCore.QRect(80, 90, 591, 301))
        self.listview_taskapps.setObjectName("listview_taskapps")
        self.btn_kill_process = QtWidgets.QPushButton(parent=form_taskmanager)
        self.btn_kill_process.setGeometry(QtCore.QRect(690, 90, 101, 61))
        self.btn_kill_process.setObjectName("btn_kill_process")
        self.btn_get_process_info = QtWidgets.QPushButton(parent=form_taskmanager)
        self.btn_get_process_info.setGeometry(QtCore.QRect(690, 160, 41, 41))
        self.btn_get_process_info.setObjectName("btn_get_process_info")
        self.btn_reload_processes = QtWidgets.QPushButton(parent=form_taskmanager)
        self.btn_reload_processes.setGeometry(QtCore.QRect(580, 50, 93, 28))
        self.btn_reload_processes.setObjectName("btn_reload_processes")

        self.retranslateUi(form_taskmanager)
        QtCore.QMetaObject.connectSlotsByName(form_taskmanager)

    def retranslateUi(self, form_taskmanager):
        _translate = QtCore.QCoreApplication.translate
        form_taskmanager.setWindowTitle(_translate("form_taskmanager", "Task Management"))
        self.lbl_header.setText(_translate("form_taskmanager", "Task Manager Apps"))
        self.btn_kill_process.setText(_translate("form_taskmanager", "Kill Process"))
        self.btn_get_process_info.setText(_translate("form_taskmanager", "?"))
        self.btn_reload_processes.setText(_translate("form_taskmanager", "Reload"))
