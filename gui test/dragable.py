# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dragable_test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class lbl(QtWidgets.QLabel):

    dist_x = 0
    dist_y = 0
    grabbing = False

    def mousePressEvent(self, QMouseEvent):
        # self.setFrameShadow(QtWidgets.QFrame.Sunken)
        mp = QMouseEvent.pos()
        self.dist_x = mp.x()
        self.dist_y = mp.y()
        self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.grabbing = True
        return super().mousePressEvent(QMouseEvent)
    
    def mouseMoveEvent(self, QMouseEvent):
        if self.grabbing:
            mp = QMouseEvent.pos()
            p = self.pos()
            self.move(mp.x() + p.x() - self.dist_x, mp.y() + p.y() - self.dist_y)
            # print("x_pos:", self.pos().x(), "dist_x:", self.dist_x, "mpx:", mp.x(), "x_pos-mpx:", self.pos().x() - mp.x())
        return super().mouseMoveEvent(QMouseEvent)
    
    def mouseReleaseEvent(self, QMouseEvent):
        # self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grabbing = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        return super().mouseReleaseEvent(QMouseEvent)
    
    def get_center(self):
        p = self.pos()
        w = self.width()
        h = self.height()
        x, y = p.x(), p.y()
        center = (x + w / 2, y + h / 2)
        return center    

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(863, 574)
        Form.setAcceptDrops(True)
        Form.setStyleSheet("background:rgb(25,25,25)")
        self.label = lbl(Form)
        self.label.setGeometry(QtCore.QRect(200, 150, 200, 100))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label.setObjectName("label")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        self.label.setStyleSheet("background: rgb(30,30,30);padding-left: 1px;border-left-width: 1px; border-left-color: white;border-left-style: solid;")
        # self.label.setFrameShape(QtWidgets.QFrame.StyledPanel) # QtWidgets.QFrame.Panel
        # # self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.label.setLineWidth(1)
        # self.label.setMidLineWidth(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
