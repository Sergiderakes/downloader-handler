# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import functions

class table(QtWidgets.QTableWidget):

    def lista(cls):
        l1 = []
        for row in range(cls.rowCount()):
            t = []
            for col in range(cls.columnCount()):
                item = cls.item(row, col)
                if item is not None:
                    t.append(item.text())
            tuple(t)
            l1.append(t)
        return l1

    def dropEvent(cls, e):
        
        print(cls.lista())

        return super().dropEvent(e)

    # @QtCore.pyqtSlot()
    # def 

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = table(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        dicc = functions.lector()
        list_dicc = functions.dicc_to_tuple_list(dicc)
        row = 0
        for tup in list_dicc:
            col = 0
            if self.tableWidget.rowCount() <= row + 1:
                self.tableWidget.setRowCount(row + 2)
            for item in tup:
                if self.tableWidget.columnCount() <= col + 1:
                    self.tableWidget.setColumnCount(col + 2)
                col+=1
            row+=1
        row = 0
        for tup in list_dicc:
            col = 0
            for item in tup:
                cellinfo = QtWidgets.QTableWidgetItem(item)
                self.tableWidget.setItem(row, col, cellinfo)
                col+=1
            row+=1

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
