# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1872, 824)
        MainWindow.setStyleSheet("background-color:rgb(95, 97, 99)")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(872, 0))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.zahl5 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl5.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl5.setObjectName("zahl5")
        self.gridLayout.addWidget(self.zahl5, 4, 7, 1, 1)
        self.cosinus = QtWidgets.QPushButton(self.centralwidget)
        self.cosinus.setStyleSheet("color: rgb(255, 255, 255);")
        self.cosinus.setObjectName("cosinus")
        self.gridLayout.addWidget(self.cosinus, 5, 1, 1, 1)
        self.zahl8 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl8.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl8.setObjectName("zahl8")
        self.gridLayout.addWidget(self.zahl8, 2, 7, 1, 1)
        self.wurzel = QtWidgets.QPushButton(self.centralwidget)
        self.wurzel.setStyleSheet("color: rgb(255, 255, 255);")
        self.wurzel.setObjectName("wurzel")
        self.gridLayout.addWidget(self.wurzel, 2, 3, 1, 1)
        self.addition = QtWidgets.QPushButton(self.centralwidget)
        self.addition.setStyleSheet("background-color: rgb(255, 159, 12);\n"
"color: rgb(255, 255, 255);")
        self.addition.setObjectName("addition")
        self.gridLayout.addWidget(self.addition, 5, 9, 1, 1)
        self.sinus = QtWidgets.QPushButton(self.centralwidget)
        self.sinus.setStyleSheet("color: rgb(255, 255, 255);")
        self.sinus.setObjectName("sinus")
        self.gridLayout.addWidget(self.sinus, 4, 1, 1, 1)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setStyleSheet("color: rgb(255, 255, 255);")
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 1, 6, 1, 1)
        self.zahl6 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl6.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl6.setObjectName("zahl6")
        self.gridLayout.addWidget(self.zahl6, 4, 8, 1, 1)
        self.subtraktion = QtWidgets.QPushButton(self.centralwidget)
        self.subtraktion.setStyleSheet("background-color: rgb(255, 159, 12);\n"
"color: rgb(255, 255, 255);")
        self.subtraktion.setObjectName("subtraktion")
        self.gridLayout.addWidget(self.subtraktion, 4, 9, 1, 1)
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setStyleSheet("background-color: rgb(255, 159, 12);\n"
"color: rgb(255, 255, 255);")
        self.division.setObjectName("division")
        self.gridLayout.addWidget(self.division, 1, 9, 1, 1)
        self.kubischx = QtWidgets.QPushButton(self.centralwidget)
        self.kubischx.setStyleSheet("color: rgb(255, 255, 255);")
        self.kubischx.setInputMethodHints(QtCore.Qt.ImhNone)
        self.kubischx.setObjectName("kubischx")
        self.gridLayout.addWidget(self.kubischx, 4, 5, 1, 1)
        self.pi = QtWidgets.QPushButton(self.centralwidget)
        self.pi.setStyleSheet("color: rgb(255, 255, 255);")
        self.pi.setObjectName("pi")
        self.gridLayout.addWidget(self.pi, 6, 2, 1, 1)
        self.multiplikation = QtWidgets.QPushButton(self.centralwidget)
        self.multiplikation.setStyleSheet("background-color: rgb(255, 159, 12);\n"
"color: rgb(255, 255, 255);")
        self.multiplikation.setObjectName("multiplikation")
        self.gridLayout.addWidget(self.multiplikation, 2, 9, 1, 1)
        self.zahl0 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl0.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl0.setObjectName("zahl0")
        self.gridLayout.addWidget(self.zahl0, 6, 6, 1, 2)
        self.quadratx = QtWidgets.QPushButton(self.centralwidget)
        self.quadratx.setStyleSheet("color: rgb(255, 255, 255);")
        self.quadratx.setObjectName("quadratx")
        self.gridLayout.addWidget(self.quadratx, 5, 5, 1, 1)
        self.ntewurzel = QtWidgets.QPushButton(self.centralwidget)
        self.ntewurzel.setStyleSheet("color: rgb(255, 255, 255);")
        self.ntewurzel.setObjectName("ntewurzel")
        self.gridLayout.addWidget(self.ntewurzel, 6, 3, 1, 1)
        self.zahl3 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl3.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl3.setObjectName("zahl3")
        self.gridLayout.addWidget(self.zahl3, 5, 8, 1, 1)
        self.zahl7 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl7.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl7.setObjectName("zahl7")
        self.gridLayout.addWidget(self.zahl7, 2, 6, 1, 1)
        self.fib = QtWidgets.QPushButton(self.centralwidget)
        self.fib.setStyleSheet("color: rgb(255, 255, 255);")
        self.fib.setObjectName("fib")
        self.gridLayout.addWidget(self.fib, 1, 5, 1, 1)
        self.tangens = QtWidgets.QPushButton(self.centralwidget)
        self.tangens.setStyleSheet("color: rgb(255, 255, 255);")
        self.tangens.setObjectName("tangens")
        self.gridLayout.addWidget(self.tangens, 6, 1, 1, 1)
        self.eulerhochx = QtWidgets.QPushButton(self.centralwidget)
        self.eulerhochx.setStyleSheet("color: rgb(255, 255, 255);")
        self.eulerhochx.setObjectName("eulerhochx")
        self.gridLayout.addWidget(self.eulerhochx, 4, 2, 1, 1)
        self.euler = QtWidgets.QPushButton(self.centralwidget)
        self.euler.setStyleSheet("color: rgb(255, 255, 255);")
        self.euler.setObjectName("euler")
        self.gridLayout.addWidget(self.euler, 5, 2, 1, 1)
        self.negation = QtWidgets.QPushButton(self.centralwidget)
        self.negation.setStyleSheet("color: rgb(255, 255, 255);")
        self.negation.setObjectName("negation")
        self.gridLayout.addWidget(self.negation, 1, 7, 1, 1)
        self.zahl4 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl4.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl4.setObjectName("zahl4")
        self.gridLayout.addWidget(self.zahl4, 4, 6, 1, 1)
        self.zahl9 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl9.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl9.setObjectName("zahl9")
        self.gridLayout.addWidget(self.zahl9, 2, 8, 1, 1)
        self.prozent = QtWidgets.QPushButton(self.centralwidget)
        self.prozent.setStyleSheet("color: rgb(255, 255, 255);")
        self.prozent.setObjectName("prozent")
        self.gridLayout.addWidget(self.prozent, 1, 8, 1, 1)
        self.komma = QtWidgets.QPushButton(self.centralwidget)
        self.komma.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.komma.setObjectName("komma")
        self.gridLayout.addWidget(self.komma, 6, 8, 1, 1)
        self.gleich = QtWidgets.QPushButton(self.centralwidget)
        self.gleich.setStyleSheet("background-color: rgb(255, 159, 12);\n"
"color: rgb(255, 255, 255);")
        self.gleich.setObjectName("gleich")
        self.gridLayout.addWidget(self.gleich, 6, 9, 1, 1)
        self.zahl2 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl2.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl2.setDefault(False)
        self.zahl2.setObjectName("zahl2")
        self.gridLayout.addWidget(self.zahl2, 5, 7, 1, 1)
        self.xhochy = QtWidgets.QPushButton(self.centralwidget)
        self.xhochy.setStyleSheet("color: rgb(255, 255, 255);")
        self.xhochy.setObjectName("xhochy")
        self.gridLayout.addWidget(self.xhochy, 2, 5, 1, 1)
        self.zahl1 = QtWidgets.QPushButton(self.centralwidget)
        self.zahl1.setStyleSheet("background-color: rgb(122, 123, 123);\n"
"color: rgb(255, 255, 255);")
        self.zahl1.setObjectName("zahl1")
        self.gridLayout.addWidget(self.zahl1, 5, 6, 1, 1)
        self.betrag = QtWidgets.QPushButton(self.centralwidget)
        self.betrag.setStyleSheet("color: rgb(255, 255, 255);")
        self.betrag.setObjectName("betrag")
        self.gridLayout.addWidget(self.betrag, 2, 2, 1, 1)
        self.viertewurzel = QtWidgets.QPushButton(self.centralwidget)
        self.viertewurzel.setStyleSheet("color: rgb(255, 255, 255);")
        self.viertewurzel.setObjectName("viertewurzel")
        self.gridLayout.addWidget(self.viertewurzel, 5, 3, 1, 1)
        self.drittewurzel = QtWidgets.QPushButton(self.centralwidget)
        self.drittewurzel.setStyleSheet("color: rgb(255, 255, 255);")
        self.drittewurzel.setObjectName("drittewurzel")
        self.gridLayout.addWidget(self.drittewurzel, 4, 3, 1, 1)
        self.exp = QtWidgets.QPushButton(self.centralwidget)
        self.exp.setStyleSheet("color: rgb(255, 255, 255);")
        self.exp.setObjectName("exp")
        self.gridLayout.addWidget(self.exp, 2, 1, 1, 1)
        self.standardhyperbel = QtWidgets.QPushButton(self.centralwidget)
        self.standardhyperbel.setStyleSheet("color: rgb(255, 255, 255);")
        self.standardhyperbel.setObjectName("standardhyperbel")
        self.gridLayout.addWidget(self.standardhyperbel, 6, 5, 1, 1)
        self.logxy = QtWidgets.QPushButton(self.centralwidget)
        self.logxy.setStyleSheet("color: rgb(255, 255, 255);")
        self.logxy.setObjectName("logxy")
        self.gridLayout.addWidget(self.logxy, 6, 4, 1, 1)
        self.log10 = QtWidgets.QPushButton(self.centralwidget)
        self.log10.setStyleSheet("color: rgb(255, 255, 255);")
        self.log10.setObjectName("log10")
        self.gridLayout.addWidget(self.log10, 5, 4, 1, 1)
        self.natlogarithmus = QtWidgets.QPushButton(self.centralwidget)
        self.natlogarithmus.setStyleSheet("color: rgb(255, 255, 255);")
        self.natlogarithmus.setObjectName("natlogarithmus")
        self.gridLayout.addWidget(self.natlogarithmus, 4, 4, 1, 1)
        self.fak = QtWidgets.QPushButton(self.centralwidget)
        self.fak.setStyleSheet("color: rgb(255, 255, 255);")
        self.fak.setObjectName("fak")
        self.gridLayout.addWidget(self.fak, 2, 4, 1, 1)
        self.ggt = QtWidgets.QPushButton(self.centralwidget)
        self.ggt.setStyleSheet("color: rgb(255, 255, 255);")
        self.ggt.setObjectName("ggt")
        self.gridLayout.addWidget(self.ggt, 1, 4, 1, 1)
        self.kgv = QtWidgets.QPushButton(self.centralwidget)
        self.kgv.setStyleSheet("color: rgb(255, 255, 255);")
        self.kgv.setObjectName("kgv")
        self.gridLayout.addWidget(self.kgv, 1, 3, 1, 1)
        self.klammerzu = QtWidgets.QPushButton(self.centralwidget)
        self.klammerzu.setStyleSheet("color: rgb(255, 255, 255);")
        self.klammerzu.setObjectName("klammerzu")
        self.gridLayout.addWidget(self.klammerzu, 1, 2, 1, 1)
        self.klammerauf = QtWidgets.QPushButton(self.centralwidget)
        self.klammerauf.setStyleSheet("color: rgb(255, 255, 255);")
        self.klammerauf.setObjectName("klammerauf")
        self.gridLayout.addWidget(self.klammerauf, 1, 1, 1, 1)
        self.Display = QtWidgets.QLCDNumber(self.centralwidget)
        self.Display.setStyleSheet("background-color: rgb(77, 79, 80);\n"
"color: rgb(255, 255, 255);")
        self.Display.setObjectName("Display")
        self.gridLayout.addWidget(self.Display, 0, 1, 1, 9)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Taschenrechner"))
        self.zahl5.setText(_translate("MainWindow", "5"))
        self.cosinus.setText(_translate("MainWindow", "cos"))
        self.zahl8.setText(_translate("MainWindow", "8"))
        self.wurzel.setText(_translate("MainWindow", "√x"))
        self.addition.setText(_translate("MainWindow", "+"))
        self.sinus.setText(_translate("MainWindow", "sin"))
        self.reset.setText(_translate("MainWindow", "AC"))
        self.zahl6.setText(_translate("MainWindow", "6"))
        self.subtraktion.setText(_translate("MainWindow", "-"))
        self.division.setText(_translate("MainWindow", "/"))
        self.kubischx.setText(_translate("MainWindow", "x^3"))
        self.pi.setText(_translate("MainWindow", "π"))
        self.multiplikation.setText(_translate("MainWindow", "x"))
        self.zahl0.setText(_translate("MainWindow", "0"))
        self.quadratx.setText(_translate("MainWindow", "x^2"))
        self.ntewurzel.setText(_translate("MainWindow", "ysqrt(n)"))
        self.zahl3.setText(_translate("MainWindow", "3"))
        self.zahl7.setText(_translate("MainWindow", "7"))
        self.fib.setText(_translate("MainWindow", "fib"))
        self.tangens.setText(_translate("MainWindow", "tan"))
        self.eulerhochx.setText(_translate("MainWindow", "e^x"))
        self.euler.setText(_translate("MainWindow", "e"))
        self.negation.setText(_translate("MainWindow", "+/-"))
        self.zahl4.setText(_translate("MainWindow", "4"))
        self.zahl9.setText(_translate("MainWindow", "9"))
        self.prozent.setText(_translate("MainWindow", "%"))
        self.komma.setText(_translate("MainWindow", ","))
        self.gleich.setText(_translate("MainWindow", "="))
        self.zahl2.setText(_translate("MainWindow", "2"))
        self.xhochy.setText(_translate("MainWindow", "x^y"))
        self.zahl1.setText(_translate("MainWindow", "1"))
        self.betrag.setText(_translate("MainWindow", "|x|"))
        self.viertewurzel.setText(_translate("MainWindow", "∜x"))
        self.drittewurzel.setText(_translate("MainWindow", "∛x"))
        self.exp.setText(_translate("MainWindow", "exp(x)"))
        self.standardhyperbel.setText(_translate("MainWindow", "1/x"))
        self.logxy.setText(_translate("MainWindow", "logxy"))
        self.log10.setText(_translate("MainWindow", "log10"))
        self.natlogarithmus.setText(_translate("MainWindow", "ln"))
        self.fak.setText(_translate("MainWindow", "n!"))
        self.ggt.setText(_translate("MainWindow", "ggT"))
        self.kgv.setText(_translate("MainWindow", "KgV"))
        self.klammerzu.setText(_translate("MainWindow", ")"))
        self.klammerauf.setText(_translate("MainWindow", "("))