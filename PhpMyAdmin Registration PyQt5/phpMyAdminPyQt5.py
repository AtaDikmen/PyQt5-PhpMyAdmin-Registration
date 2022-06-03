import sys
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(450, 350)
        Form.setMinimumSize(QtCore.QSize(450, 350))
        Form.setMaximumSize(QtCore.QSize(450, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"background-color: qlineargradient(spread:pad, x1:0.04, y1:0.051, x2:0.534, y2:0.914, stop:0 rgba(0, 255, 255, 255), stop:0.988636 rgba(255, 255, 255, 255));\n"
"}")
        self.title_text = QtWidgets.QLabel(Form)
        self.title_text.setGeometry(QtCore.QRect(80, 30, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_text.setFont(font)
        self.title_text.setStyleSheet("")
        self.title_text.setObjectName("title_text")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 50, 371, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setGeometry(QtCore.QRect(210, 90, 171, 21))
        self.name_line.setObjectName("name_line")
        self.name_text = QtWidgets.QLabel(Form)
        self.name_text.setGeometry(QtCore.QRect(60, 90, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.name_text.setFont(font)
        self.name_text.setStyleSheet("")
        self.name_text.setObjectName("name_text")
        self.mail_line = QtWidgets.QLineEdit(Form)
        self.mail_line.setGeometry(QtCore.QRect(210, 120, 171, 21))
        self.mail_line.setObjectName("mail_line")
        self.mail_text = QtWidgets.QLabel(Form)
        self.mail_text.setGeometry(QtCore.QRect(150, 120, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mail_text.setFont(font)
        self.mail_text.setObjectName("mail_text")
        self.uni_text = QtWidgets.QLabel(Form)
        self.uni_text.setEnabled(True)
        self.uni_text.setGeometry(QtCore.QRect(120, 150, 91, 19))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.uni_text.setFont(font)
        self.uni_text.setObjectName("uni_text")
        self.uni_line = QtWidgets.QLineEdit(Form)
        self.uni_line.setGeometry(QtCore.QRect(210, 150, 171, 21))
        self.uni_line.setObjectName("uni_line")
        self.dep_line = QtWidgets.QLineEdit(Form)
        self.dep_line.setGeometry(QtCore.QRect(210, 180, 171, 21))
        self.dep_line.setObjectName("dep_line")
        self.dep_text = QtWidgets.QLabel(Form)
        self.dep_text.setGeometry(QtCore.QRect(110, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dep_text.setFont(font)
        self.dep_text.setObjectName("dep_text")
        self.save_button = QtWidgets.QPushButton(Form)
        self.save_button.setGeometry(QtCore.QRect(150, 250, 151, 51))
        self.save_button.setStyleSheet("border-radius:20px;\n"
"background-color:rgb(28, 214, 255);\n"
"font: 75 13pt \"Times New Roman\";\n"
"")
        self.save_button.setObjectName("save_button")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(70, 220, 331, 20))
        self.error.setStyleSheet("font: 75 11pt \"Times New Roman\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.name_text_2 = QtWidgets.QLabel(Form)
        self.name_text_2.setGeometry(QtCore.QRect(300, 320, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.name_text_2.setFont(font)
        self.name_text_2.setObjectName("name_text_2")

        self.save_button.clicked.connect(self.connect_to_db)
        self.unique = 0

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PhpMyAdmin Registration"))
        self.title_text.setText(_translate("Form", "PhpMyAdmin Database Registration"))
        self.name_text.setText(_translate("Form", "Name and Surname :"))
        self.mail_text.setText(_translate("Form", "E-mail :"))
        self.uni_text.setText(_translate("Form", "University :"))
        self.dep_text.setText(_translate("Form", "Department :"))
        self.save_button.setText(_translate("Form", "Save to database"))
        self.name_text_2.setText(_translate("Form", "Created by Ata DİKMEN"))


    def connect_to_db(self):
        self.connection = mysql.connector.connect(host="localhost", database="pyqt5_db", user="root", password="")
        self.cursor = self.connection.cursor()

        name = self.name_line.text()
        mail = self.mail_line.text()
        uni = self.uni_line.text()
        dep = self.dep_line.text()

        if len(name) == 0 or len(mail) == 0 or len(uni) == 0 or len(dep) == 0:
            self.error.setText("Please input all fields.")
            self.cursor.close()
            self.connection.close()
        else:
            self.error.setText("")
            self.cursor.execute("SELECT * FROM pyqt5_tbl")
            for name_, mail_, uni_, dep_ in self.cursor:
                if mail == mail_:
                    self.unique = 1

            if self.unique == 1:
                self.unique = 0
                self.error.setText("This email address has been used before.")
            else:
                self.unique = 0
                self.error.setText("")
                sql = "INSERT INTO pyqt5_tbl VALUES(%s,%s,%s,%s)"
                val = (name, mail, uni, dep)

                self.cursor.execute(sql, val)
                self.connection.commit()
                self.error.setText("Successfully saved!")

        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
