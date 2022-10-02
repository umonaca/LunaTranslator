
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QRect,pyqtSignal ,QSize
import qtawesome
import utils.screen_rate  
class MySwitch(QtWidgets.QPushButton):
    realclicksignal=pyqtSignal(bool)
    def __init__(self, parent = None,sign=True, textOn='On',textOff='off'):
        super().__init__(parent) 
        self.setCheckable(True)
        self.setChecked(sign) 
        self.TextOff=textOff
        self.TextOn=textOn
        self.setStyleSheet('''background-color: rgba(255, 255, 255, 0);
          color: black;
          border: 0px;
          font: 100 10pt;''')
        self.rate= utils.screen_rate.getScreenRate() 
        self.clicked.connect(self.clickfunction)
        self.clicked=self.realclicksignal
        self.setIconSize(QSize(int(30*self.rate),
                                 int(30*self.rate)))
        #self.setIcon(qtawesome.icon("fa.check" ,color="#FF69B4" if self.isChecked() else '#dadbdc'))
        self.setIcon(qtawesome.icon("fa.check" ,color="#FF69B4") if self.isChecked() else qtawesome.icon("fa.times" ,color='#dadbdc'))
    def clickfunction(self,_):
        #self.setIcon(qtawesome.icon("fa.check" ,color="#FF69B4" if self.isChecked() else '#dadbdc'))
        self.setIcon(qtawesome.icon("fa.check" ,color="#FF69B4") if self.isChecked() else qtawesome.icon("fa.times" ,color='#dadbdc'))
        self.realclicksignal.emit(_)
    def setChecked(self,  a0)  :
        super().setChecked(a0)
        self.clickfunction(a0)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 350)
        MainWindow.setMinimumSize(QtCore.QSize(550, 350))
        MainWindow.setMaximumSize(QtCore.QSize(550, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 500, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_Save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Save.setGeometry(QtCore.QRect(120, 250, 100, 50))
        self.pushButton_Save.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_Save.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_Save.setObjectName("pushButton_Save")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.retranslateUi(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Filter"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "complement"))
        self.pushButton_Save.setText(_translate("MainWindow", "Save"))
        self.pushButton_Save.clicked.connect(self.bindSave)
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "status"))
    def bindSave(self):
        numRows = self.tableWidget.rowCount()
        self.tableWidget.insertRow(numRows)

        groupButton = QtWidgets.QButtonGroup(self.tableWidget)
        groupButton.setExclusive(True)
        it1 = QtWidgets.QTableWidgetItem("filter "+str(numRows))
        self.tableWidget.setItem(numRows, 0, it1)
        ch_bx1 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx1)
        self.tableWidget.setCellWidget(numRows, 1, ch_bx1)
        ch_bx2 = QtWidgets.QCheckBox()
        groupButton.addButton(ch_bx2)
        self.tableWidget.setCellWidget(numRows, 2, ch_bx2)
        ch_bx3 = MySwitch()
        ch_bx3.setChecked(False)
        ch_bx3.clicked.connect(ch_bx1.setEnabled)
        ch_bx3.clicked.connect(ch_bx2.setEnabled)
        self.tableWidget.setCellWidget(numRows, 3, ch_bx3)
import sys

if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    MainWindow = QtWidgets.QMainWindow()
    ui        = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exit(app.exec_())