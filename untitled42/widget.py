# This Python file uses the following encoding: utf-8
import sys
import json
import g4f

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mess=[]
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
#signals
        self.ui.lineEdit.returnPressed.connect(self.sl1)
        self.ui.pushButton.clicked.connect(self.sl2)
        self.ui.pushButton_2.clicked.connect(self.sl3)
        self.ui.pushButton_3.clicked.connect(self.sl4)


#slots
    def sl1(self):
        question = self.ui.lineEdit.text()
        if question.strip().lower()=="хватит":
            self.mess=[]
            self.ui.textBrowser.insertHtml("<br><strong>ai:</strong> <ai> Поговорим на другую тему. </ai>")
            self.ui.lineEdit.setText("")
        else:
            self.ui.textBrowser.insertHtml("<br><strong>me:</strong> <me> "+question+" </me>")
            self.mess.append({"role":"user", "content":question})
            answer = g4f.ChatCompletion.create(
#                model=g4f.models.gpt_4_32k_0613 ,
#                model=g4f.models.gpt_4 ,
                model=g4f.models.gpt_35_turbo ,
                messages=self.mess
            )
            self.ui.lineEdit.setText("")
            self.ui.textBrowser.insertHtml("<br><strong>ai:</strong> <ai> "+answer+" </ai>")
            self.mess.append({"role":"assistant", "content":answer})

    def sl2(self):
        #filename = self.ui.lineEdit_2.text().strip().lower()
        fileName = QFileDialog.getOpenFileName(self,
            "Open AI File", self.ui.lineEdit_2.text(), "AI Files (*.json)")
        filename=fileName[0]
        self.ui.lineEdit_2.setText(filename)
        if filename != "":
            with open(filename, "r") as file:
                self.mess = json.load(file)

    def sl3(self):
        #filename = self.ui.lineEdit_2.text().strip().lower()
        fileName = QFileDialog.getSaveFileName(self, "Save AI File",
                                   self.ui.lineEdit_2.text(), "AI Files (*.json)")
        filename=fileName[0]
        self.ui.lineEdit_2.setText(filename)
        if filename != "":
            with open(filename, "w") as file:
                json.dump(self.mess, file)

    def sl4(self):
        self.ui.textBrowser.setHtml("")
        for req in self.mess :
            if req["role"] == "user" :
                self.ui.textBrowser.insertHtml("<br><strong>me:</strong> <me> "+req["content"]+" </me>")
            else :
                self.ui.textBrowser.insertHtml("<br><strong>ai:</strong> <ai> "+req["content"]+" </ai>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
