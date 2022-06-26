import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_n1=PyQt5.QtWidgets.QLabel(self)
        self.lbl_n1.setText("Number 1:")
        self.lbl_n1.move(50,30)

        self.txt_n1=PyQt5.QtWidgets.QLineEdit(self)
        self.txt_n1.move(150,30)
        self.txt_n1.resize(200,32)

        self.lbl_n2=PyQt5.QtWidgets.QLabel(self)
        self.lbl_n2.setText("Number 2:")
        self.lbl_n2.move(50,80)
        
        self.txt_n2=PyQt5.QtWidgets.QLineEdit(self)
        self.txt_n2.move(150,80)
        self.txt_n2.resize(200,32)

        self.btn_sum =PyQt5.QtWidgets.QPushButton(self)
        self.btn_sum.setText("Sum")
        self.btn_sum.move(150,130)
        self.btn_sum.clicked.connect(self.calculate)

        self.btn_subtract =PyQt5.QtWidgets.QPushButton(self)
        self.btn_subtract.setText("Subtract")
        self.btn_subtract.move(150,170)
        self.btn_subtract.clicked.connect(self.calculate)

        self.btn_mult =PyQt5.QtWidgets.QPushButton(self)
        self.btn_mult.setText("Multiplication")
        self.btn_mult.move(150,210)
        self.btn_mult.clicked.connect(self.calculate)

        
        self.btn_divide =PyQt5.QtWidgets.QPushButton(self)
        self.btn_divide.setText("Divide")
        self.btn_divide.move(150,250)
        self.btn_divide.clicked.connect(self.calculate)

        self.lbl_r=PyQt5.QtWidgets.QLabel(self)
        self.lbl_r.setText("Result: ")
        self.lbl_r.move(150,290)

    def calculate(self):
        sender=self.sender()
        sdText=sender.text()
       
        result=0
        if sdText =="Sum":
            result= int(self.txt_n1.text())-int(self.txt_n2.text())
       
        elif sdText == "Subtract":
            result= int(self.txt_n1.text())-int(self.txt_n2.text())

        elif sdText == "Multiplication":
            result= int(self.txt_n1.text())*int(self.txt_n2.text())

        elif sdText == "Divide":
            result= int(self.txt_n1.text())/int(self.txt_n2.text())
        
        self.lbl_r.setText("Result: "+str(result))
            

   

    # def subtract(self):
    #     result= int(self.txt_n1.text())-int(self.txt_n2.text())
    #     self.lbl_r.setText("Result: "+str(result))

    # def mult(self):
    #     result= int(self.txt_n1.text())*int(self.txt_n2.text())
    #     self.lbl_r.setText("Result: "+str(result))
    
    # def divide(self):
    #     result= int(self.txt_n1.text())/int(self.txt_n2.text())
    #     self.lbl_r.setText("Result: "+str(result))
        
      

def app():
    app=QApplication(sys.argv)
    win=MainForm()
    win.show()
    sys.exit(app.exec_())
app()