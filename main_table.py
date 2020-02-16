from PyQt5 import QtCore, QtGui, QtWidgets
import random
import functions

def create_label(Form, name, pos, color, text, table):
        _translate = QtCore.QCoreApplication.translate
        color = str(color[0]) + "," + str(color[1])+ "," + str(color[2])
        label = lbl(Form)
        label.setGeometry(QtCore.QRect(pos[0], pos[1], 120, 60))
        label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        label.setObjectName(name)
        label.set_table(table)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        label.setPalette(palette)
        label.setText(_translate("Form", text))
        label.setStyleSheet("background: rgb(57,57,67);" + 
                                "padding-left: 1px;" + 
                                "border-left-width: 3px;" + 
                                "border-left-color: rgb(" + color + ");" + 
                                "border-left-style: solid")
        # self.label.setFrameShape(QtWidgets.QFrame.StyledPanel) # QtWidgets.QFrame.Panel
        # # self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.label.setLineWidth(1)
        # self.label.setMidLineWidth(0)
        return label

def generate_label_list(Form, base_name, pos, table):
    color = [(55, 239, 186),(30, 185, 128),(0, 93, 87),(0, 125, 81)] # random.randint(0, 3)
    l = []
    dicc = functions.lector()
    lt = functions.dicc_to_tuple_list(dicc)
    # for i in range(a * b):
    #     print(y, x)
    #     label = create_label(Form, base_name + str(i), (pos[0] + x * 122, pos[1] + y * 62), color[i%4], lt[y][x]) # 122 is 120 (width) + 2 (sep)
    #     l.append(label)
    #     if x == len(lt[y]) - 1:
    #         y += 1
    #         y %= b
    #     x += 1
    #     x %= len(lt[y])
    y = 0
    for t in lt:
        x = 0
        fol = "Folder: "
        for text in t:
            label = create_label(Form, base_name + str(x) + str(y)
                    , (pos[0] + x * 122, pos[1] + y * 62), color[x%4], fol + lt[y][x], table) # 122 is 120 (width) + 2 (sep)
            l.append(label)
            fol = ""
            x += 1
        y += 1
    return l 

class table(QtWidgets.QWidget):
    label_list = []
    coords = []

    def generate_coords(self, pos, x_amount, y_amount, width, height, sep):
        x, y = pos[0], pos[1]
        lx = []
        ly = []
        for x1 in range(x, x_amount * (width + sep), width + sep):
            lx.append(x1)
        for y1 in range(y, y_amount * (height + sep), height + sep):
            ly.append(y1)
        l = []
        for y in ly:
            for x in lx:
                t = (x, y)
                l.append(t)
        self.coords = l
    
    def add_label(self, x, y, label):
        if self.label_list[y][x] == None:
            self.label_list[y][x] = label
            label.move(self.coords[y][x])
    
    def move_label(self, x, y, x1, y1, label):
        if not x == x1 and y == y1:
            temp_label = self.label_list[y][x]
            self.label_list[y1][x1] = temp_label
            self.label_list[y][x] = label
            temp_label.move(self.coords[y][x])
            label.move(self.coords[y][x])

    def get_closest_tablepos(self, pos):
        x, y = pos[0], pos[1]
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            rx, ry = x - self.coords[0][0], y - self.coords[0][1]
            cx, cy = self.coords[0][0], self.coords[0][1]
            for coord in self.coords:
                rxt, ryt = x - coord[0], y - coord[1]
                if rx < rxt and ry < ryt:
                    rx, ry = rxt, ryt
                    cx, cy = coord[0], coord[1]
            
    
    def mousePressEvent(self, QMouseEvent):

        return super().mousePressEvent(QMouseEvent)

    

class lbl(QtWidgets.QLabel):

    dist_x = 0
    dist_y = 0
    grabbing = False
    table = None

    def set_table(self, table):
        self.table = table

    def mousePressEvent(self, QMouseEvent):
        # self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.raise_() # This put the label in front of the screen
        temp = self.styleSheet()
        splits = temp.split(";")
        splits[0] = "background: rgb(67,67,77)"
        temp = ";".join(splits)
        self.setStyleSheet(temp)
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
        if self.grabbing:
            # self.setFrameShadow(QtWidgets.QFrame.Raised)
            temp = self.styleSheet()
            splits = temp.split(";")
            splits[0] = "background: rgb(57,57,67)"
            temp = ";".join(splits)
            self.setStyleSheet(temp)
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

def generate_table(Form):
    widget = table(Form)
    widget.setGeometry(QtCore.QRect(140, 70, 461, 361))
    widget.setObjectName("widget")
    return widget

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(863, 574)
        Form.setAcceptDrops(True)
        Form.setStyleSheet("background:rgb(44,44,54)")
        
        self.label_list = generate_label_list(Form, "label", (50,50), None)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())