import cmath
import sys
import math
import time
from typing import List, Any
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qtpy import QtWidgets
from GUI.mainwindow import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Taschenrechner")
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #setzt Länge der Zahl die angezeigt werden kann auf max
        self.ui.Display.setDigitCount(2147483647)
        #Variablen die korrekte Funktionsweise ermöglichen
        self.Eingabe1 = 0
        self.Eingabe2 = 0
        self.operator = ""
        self.counter = 0
        self.counterAdd = 0
        self.Result = 0
        #Listener für die Button
        self.ui.zahl0.clicked.connect(self.on_zahl0_click)
        self.ui.zahl1.clicked.connect(self.on_zahl1_click)
        self.ui.zahl2.clicked.connect(self.on_zahl2_click)
        self.ui.zahl3.clicked.connect(self.on_zahl3_click)
        self.ui.zahl4.clicked.connect(self.on_zahl4_click)
        self.ui.zahl5.clicked.connect(self.on_zahl5_click)
        self.ui.zahl6.clicked.connect(self.on_zahl6_click)
        self.ui.zahl7.clicked.connect(self.on_zahl7_click)
        self.ui.zahl8.clicked.connect(self.on_zahl8_click)
        self.ui.zahl9.clicked.connect(self.on_zahl9_click)
        self.ui.reset.clicked.connect(self.on_reset_click)
        self.ui.addition.clicked.connect(self.on_addition_click)
        self.ui.subtraktion.clicked.connect(self.on_subtraktion_click)
        self.ui.multiplikation.clicked.connect(self.on_multiplikation_click)
        self.ui.division.clicked.connect(self.on_division_click)
        self.ui.gleich.clicked.connect(self.on_istgleich_click)
        self.ui.fak.clicked.connect(self.on_fak_click)
        self.ui.exp.clicked.connect(self.on_exp_click)
        self.ui.quadratx.clicked.connect(self.on_quadratx_click)
        self.ui.kubischx.clicked.connect(self.on_cube_click)
        self.ui.xhochy.clicked.connect(self.on_pow_click)
        self.ui.wurzel.clicked.connect(self.on_sqr_click)
        self.ui.ntewurzel.clicked.connect(self.on_ntewurzel_click)
        self.ui.drittewurzel.clicked.connect(self.on_drittewurzel_click)
        self.ui.viertewurzel.clicked.connect(self.on_viertewurzel_click)
        self.ui.sinus.clicked.connect(self.on_sinus_click)
        self.ui.cosinus.clicked.connect(self.on_cosinus_click)
        self.ui.tangens.clicked.connect(self.on_tangens_click)
        self.ui.pi.clicked.connect(self.on_pi_click)
        self.ui.fib.clicked.connect(self.on_fib_click)
        self.ui.ggt.clicked.connect(self.on_ggt_click)
        self.ui.kgv.clicked.connect(self.on_kgv_click)
        self.ui.euler.clicked.connect(self.on_euler_click)
        self.ui.eulerhochx.clicked.connect(self.on_eulerhochx_click)
        self.ui.negation.clicked.connect(self.on_negation_click)
        self.ui.betrag.clicked.connect(self.on_betrag_click)
        self.ui.standardhyperbel.clicked.connect(self.on_standardhyperbel_click)
        self.ui.log10.clicked.connect(self.on_log10_click)
        self.ui.natlogarithmus.clicked.connect(self.on_natlog_click)
        self.ui.logxy.clicked.connect(self.on_logxy_click)
        self.ui.prozent.clicked.connect(self.on_prozent_click)

    # Methoden zur Zahleneingabe
    def on_zahl0_click(self):
        if self.counter != 1:
            zahl0 = self.concat(self.ui.Display.intValue(), 0)
            self.ui.Display.display(zahl0)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(0)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(0)
            self.counter = 0

    def on_zahl1_click(self):
        if self.counter != 1:
            zahl1 = self.concat(self.ui.Display.intValue(), 1)
            self.ui.Display.display(zahl1)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(1)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(1)
            self.counter = 0

    def on_zahl2_click(self):
        if self.counter != 1:
            zahl2 = self.concat(self.ui.Display.intValue(), 2)
            self.ui.Display.display(zahl2)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(2)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(2)
            self.counter = 0

    def on_zahl3_click(self):
        if self.counter != 1:
            zahl3 = self.concat(self.ui.Display.intValue(), 3)
            self.ui.Display.display(zahl3)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(3)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(3)
            self.counter = 0

    def on_zahl4_click(self):
        if self.counter != 1:
            zahl4 = self.concat(self.ui.Display.intValue(), 4)
            self.ui.Display.display(zahl4)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(4)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(4)
            self.counter = 0

    def on_zahl5_click(self):
        if self.counter != 1:
            zahl5 = self.concat(self.ui.Display.intValue(), 5)
            self.ui.Display.display(zahl5)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(5)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(5)
            self.counter = 0

    def on_zahl6_click(self):
        if self.counter != 1:
            zahl6 = self.concat(self.ui.Display.intValue(), 6)
            self.ui.Display.display(zahl6)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(6)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(6)
            self.counter = 0

    def on_zahl7_click(self):
        if self.counter != 1:
            zahl7 = self.concat(self.ui.Display.intValue(), 7)
            self.ui.Display.display(zahl7)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(7)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(7)
            self.counter = 0

    def on_zahl8_click(self):
        if self.counter != 1:
            zahl8 = self.concat(self.ui.Display.intValue(),8)
            self.ui.Display.display(zahl8)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(8)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(8)
            self.counter = 0

    def on_zahl9_click(self):
        if self.counter != 1:
            zahl9 = self.concat(self.ui.Display.intValue(), 9)
            self.ui.Display.display(zahl9)
        if self.counter == 1 and self.operator == "logxy":
            self.ui.Display.display(9)
            self.counter = 0
        if self.counter == 1:
            self.ui.Display.display(9)
            self.counter = 0

    #Grundfunktionen
    def on_addition_click(self):
        self.on_istgleich_click()
        self.operator = "+"
        self.counter = 1
        self.Eingabe1 = self.current_state_of_display()

    def on_multiplikation_click(self):
        self.on_istgleich_click()
        self.operator = "*"
        self.counter = 1
        self.Eingabe1 = self.current_state_of_display()

    def on_subtraktion_click(self):

            self.on_istgleich_click()
            self.operator = "-"
            self.counter = 1
            self.Eingabe1 = self.current_state_of_display()

    def on_division_click(self):
        self.on_istgleich_click()
        self.operator = "/"
        self.counter = 1
        self.Eingabe1 = self.current_state_of_display()
#Methode die die korrekte Eingabe einer zweiten Variable gewährleistet
    def on_istgleich_click(self):
        self.Eingabe2 = self.current_state_of_display()
        if self.operator == "+":
            if self.Result != 0:
                self.Result += self.Eingabe1
            else:
                self.Result = self.Eingabe1 + self.Eingabe2
            self.ui.Display.display(self.Result)
        elif self.operator =="-":

            if self.Result != 0:
                self.Result -= self.Eingabe1
            else:
                self.Result = self.Eingabe1 - self.Eingabe2
            self.ui.Display.display(self.Result)
        elif self.operator == "*":
            if self.Result != 0:
                self.Result *= self.Eingabe1
            else:
                self.Result = self.Eingabe1 * self.Eingabe2
            self.ui.Display.display(self.Result)
        elif self.operator == "ggt":
            self.Result = math.gcd(int(self.Eingabe1),int(self.Eingabe2))
            self.ui.Display.display(self.Result)
        elif self.operator == "kgv":
            self.Result = int(self.Eingabe1 * self.Eingabe2) / math.gcd(int(self.Eingabe1),int(self.Eingabe2))
            self.ui.Display.display(self.Result)
        elif self.operator == "/":
            if self.Result != 0:
                self.Result /= self.Eingabe1
            if self.Eingabe2 != 0:
                    self.Result = self.Eingabe1 / self.Eingabe2
                    self.ui.Display.display(self.Result)
            if self.operator == "/" and int(self.Eingabe2) == 0:
                self.ui.Display.display("Error")
        elif self.operator == "pow":
            if self.Result != 0:
                self.Result = math.pow(self.Result, self.Eingabe1)
            else:
                self.Result = math.pow(self.Eingabe1, self.Eingabe2)
            self.ui.Display.display(self.Result)
        elif self.operator == "nte":
            if self.Result != 0:
                if self.Result <=4:
                    self.ui.Display.display("Error")
                else:
                    self.Result = self.nteWurzel(self.Result, self.Eingabe1)
                    self.ui.Display.display(self.Result)
            else:
                if int(self.Eingabe1) <= 4:
                    self.ui.Display.display("Error")
                else:
                    self.Result = self.nteWurzel(self.Eingabe1, self.Eingabe2)
                    self.ui.Display.display(self.Result)
        elif self.operator == "e^x":
            self.Result = self.Eingabe1**self.Eingabe2
            self.ui.Display.display(self.Result)
        elif self.operator == "logxy":
            if self.Eingabe2 <= 0:
                self.ui.Display.display("Error")
            else:
                self.ui.Display.display(math.log(self.Eingabe2,self.Eingabe1))
        self.resetInput()

#Funktionen
    def on_fak_click(self):
        fak = int(self.ui.Display.value())
        if fak < 0:
            self.ui.Display.display("Error")
        else:
            fak = math.factorial(fak)
            if fak > 2147483647:
                fak = "{:e}".format(fak)
                self.ui.Display.display(fak)
            else:
                self.ui.Display.display(fak)
    def on_exp_click(self):
        exp = self.ui.Display.value()
        self.ui.Display.display(math.exp(exp))
    def on_quadratx_click(self):
        quad = self.ui.Display.value()
        self.ui.Display.display(quad*quad)
    def on_cube_click(self):
        cube = self.ui.Display.value()
        self.ui.Display.display(cube*cube*cube)
    def on_pow_click(self):
        self.operator = "pow"
        self.counter = 1
        self.Eingabe1 = self.ui.Display.value()
    def on_sqr_click(self):
        sqr = self.ui.Display.value()
        self.ui.Display.display(math.sqrt(sqr))
    def on_ntewurzel_click(self):
        self.operator = "nte"
        self.counter = 1
        self.Eingabe1 = self.ui.Display.value()
    def on_drittewurzel_click(self):
        self.ui.Display.display(self.nteWurzel(3,self.ui.Display.value()))
    def on_viertewurzel_click(self):
        self.ui.Display.display(self.nteWurzel(4,self.ui.Display.value()))
    def on_sinus_click(self):
        sin = self.ui.Display.value()
        self.ui.Display.display(math.sin(sin))
    def on_cosinus_click(self):
        cos = self.ui.Display.value()
        self.ui.Display.display(math.cos(cos))
    def on_tangens_click(self):
        tan = self.ui.Display.value()
        self.ui.Display.display(math.tan(tan))
    def on_pi_click(self):
        self.ui.Display.display(math.pi)
    def on_fib_click(self):
        fibo = int(self.ui.Display.value())
        if fibo < 0:
            self.ui.Display.display("Error")
        else:
            fibo = self.fib(fibo)
            if fibo > 2147483647:
                fibo = "{:e}".format(fibo)
                self.ui.Display.display(fibo)
            else:
                self.ui.Display.display(fibo)
    def on_ggt_click(self):
        self.operator = "ggt"
        self.counter = 1
        self.Eingabe1 = self.ui.Display.value()
    def on_kgv_click(self):
        self.operator = "kgv"
        self.counter = 1
        self.Eingabe1 = self.ui.Display.value()
    def on_euler_click(self):
        self.ui.Display.display(2.718281828459045)
    def on_eulerhochx_click(self):
        self.operator = "e^x"
        self.counter=1
        self.ui.Display.display(2.718281828459045)
        self.Eingabe1 = self.ui.Display.value()
    def on_negation_click(self):
        if self.ui.Display.value() >= 0:
            self.ui.Display.display(0-self.ui.Display.value())
        else:
            self.ui.Display.display(0-(self.ui.Display.value()))
    def on_betrag_click(self):
        if self.ui.Display.value() < 0:
            self.ui.Display.display(0-(self.ui.Display.value()))
    def on_standardhyperbel_click(self):
        if self.ui.Display.value() == 0:
            self.ui.Display.display("Error")
        else:
            self.ui.Display.display(1 / (self.ui.Display.value()))
    def on_log10_click(self):
        if self.ui.Display.value() <= 0:
            self.ui.Display.display("Error")
        else:
            self.ui.Display.display(math.log10(self.ui.Display.value()))
    def on_natlog_click(self):
        if self.ui.Display.value() <= 0:
            self.ui.Display.display("Error")
        else:
            self.ui.Display.display(math.log(self.ui.Display.value()))
    def on_logxy_click(self):
        if self.ui.Display.value() <= 0:
            self.ui.Display.display("Error")
        else:
            self.counter = 1
            self.operator = "logxy"
            self.Eingabe1=self.ui.Display.value()
    def on_prozent_click(self):
        if self.Eingabe1 == 0:
            self.ui.Display.display(self.ui.Display.value()/100)
        else:
            self.ui.Display.display((self.Eingabe1/100)*self.ui.Display.value())

    def nteWurzel(self,a,b):
        return a**(1/float(b))

    def fib(self,a ):
        base = {0: 0, 1: 1}
        def fibo(a):
            if a not in base:
                base[a] = fibo(a - 1) + fibo(a - 2)
            return base[a]
        return fibo(a)

#Funktionen um die Werte zurückzusetzen
    def on_reset_click(self):
        self.ui.Display.display(0)
        self.Eingabe1 = 0
        self.Eingabe2 = 0
        self.counter = 0
        self.counter2 = 0
        self.operator = ""
        self.Result = 0

    def resetInput(self):
        self.Eingabe1 = 0
        self.Eingabe2 = 0
        self.counter = 0
        self.operator = ""
        self.Result = 0

#kokateniert die Eingaben
    def concat(self, a, b):
        return a * (10 ** len(str(b))) + b
#liefert den aktuellen Displaywert
    def current_state_of_display(self):
        return self.ui.Display.value()



window = MainWindow()
window.show()
sys.exit(app.exec())

