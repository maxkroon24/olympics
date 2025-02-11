# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designschoolproject.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 659)
        self.firstpage = QtWidgets.QWidget(MainWindow)
        self.firstpage.setObjectName("firstpage")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.firstpage)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame = QtWidgets.QFrame(self.firstpage)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(60, 20, 1151, 661))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.headtitle = QtWidgets.QLabel(self.start)
        self.headtitle.setGeometry(QtCore.QRect(-20, 0, 1141, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headtitle.setFont(font)
        self.headtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.headtitle.setObjectName("headtitle")
        self.subtitle = QtWidgets.QLabel(self.start)
        self.subtitle.setGeometry(QtCore.QRect(10, 140, 1131, 20))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle.setFont(font)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")
        self.firstnametitle = QtWidgets.QLabel(self.start)
        self.firstnametitle.setGeometry(QtCore.QRect(80, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.firstnametitle.setFont(font)
        self.firstnametitle.setAutoFillBackground(False)
        self.firstnametitle.setAlignment(QtCore.Qt.AlignCenter)
        self.firstnametitle.setObjectName("firstnametitle")
        self.firstname = QtWidgets.QLineEdit(self.start)
        self.firstname.setGeometry(QtCore.QRect(80, 250, 113, 20))
        self.firstname.setObjectName("firstname")
        self.lastnametitle = QtWidgets.QLabel(self.start)
        self.lastnametitle.setGeometry(QtCore.QRect(310, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lastnametitle.setFont(font)
        self.lastnametitle.setAutoFillBackground(False)
        self.lastnametitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lastnametitle.setObjectName("lastnametitle")
        self.lastname = QtWidgets.QLineEdit(self.start)
        self.lastname.setGeometry(QtCore.QRect(310, 250, 113, 20))
        self.lastname.setObjectName("lastname")
        self.weighttitle = QtWidgets.QLabel(self.start)
        self.weighttitle.setGeometry(QtCore.QRect(90, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weighttitle.setFont(font)
        self.weighttitle.setAutoFillBackground(False)
        self.weighttitle.setAlignment(QtCore.Qt.AlignCenter)
        self.weighttitle.setObjectName("weighttitle")
        self.weight = QtWidgets.QLineEdit(self.start)
        self.weight.setGeometry(QtCore.QRect(80, 400, 113, 20))
        self.weight.setObjectName("weight")
        self.heighttitle = QtWidgets.QLabel(self.start)
        self.heighttitle.setGeometry(QtCore.QRect(320, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.heighttitle.setFont(font)
        self.heighttitle.setAutoFillBackground(False)
        self.heighttitle.setAlignment(QtCore.Qt.AlignCenter)
        self.heighttitle.setObjectName("heighttitle")
        self.height = QtWidgets.QLineEdit(self.start)
        self.height.setGeometry(QtCore.QRect(310, 400, 113, 20))
        self.height.setText("")
        self.height.setObjectName("height")
        self.agetitle = QtWidgets.QLabel(self.start)
        self.agetitle.setGeometry(QtCore.QRect(90, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.agetitle.setFont(font)
        self.agetitle.setAutoFillBackground(False)
        self.agetitle.setAlignment(QtCore.Qt.AlignCenter)
        self.agetitle.setObjectName("agetitle")
        self.age = QtWidgets.QLineEdit(self.start)
        self.age.setGeometry(QtCore.QRect(80, 550, 113, 20))
        self.age.setObjectName("age")
        self.sextitle = QtWidgets.QLabel(self.start)
        self.sextitle.setGeometry(QtCore.QRect(310, 510, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sextitle.setFont(font)
        self.sextitle.setAutoFillBackground(False)
        self.sextitle.setAlignment(QtCore.Qt.AlignCenter)
        self.sextitle.setObjectName("sextitle")
        self.sex = QtWidgets.QComboBox(self.start)
        self.sex.setGeometry(QtCore.QRect(310, 550, 111, 21))
        self.sex.setObjectName("sex")
        self.sex.addItem("")
        self.sex.addItem("")
        self.teamtitle = QtWidgets.QLabel(self.start)
        self.teamtitle.setGeometry(QtCore.QRect(530, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.teamtitle.setFont(font)
        self.teamtitle.setAutoFillBackground(False)
        self.teamtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.teamtitle.setObjectName("teamtitle")
        self.team = QtWidgets.QLineEdit(self.start)
        self.team.setGeometry(QtCore.QRect(530, 250, 113, 20))
        self.team.setObjectName("team")
        self.noctitle = QtWidgets.QLabel(self.start)
        self.noctitle.setGeometry(QtCore.QRect(530, 370, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.noctitle.setFont(font)
        self.noctitle.setAutoFillBackground(False)
        self.noctitle.setAlignment(QtCore.Qt.AlignCenter)
        self.noctitle.setObjectName("noctitle")
        self.noc = QtWidgets.QLineEdit(self.start)
        self.noc.setGeometry(QtCore.QRect(530, 400, 113, 20))
        self.noc.setObjectName("noc")
        self.yeartitle = QtWidgets.QLabel(self.start)
        self.yeartitle.setGeometry(QtCore.QRect(740, 220, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.yeartitle.setFont(font)
        self.yeartitle.setAutoFillBackground(False)
        self.yeartitle.setAlignment(QtCore.Qt.AlignCenter)
        self.yeartitle.setObjectName("yeartitle")
        self.year = QtWidgets.QLineEdit(self.start)
        self.year.setGeometry(QtCore.QRect(740, 250, 113, 20))
        self.year.setObjectName("year")
        self.seasontitle = QtWidgets.QLabel(self.start)
        self.seasontitle.setGeometry(QtCore.QRect(740, 370, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.seasontitle.setFont(font)
        self.seasontitle.setAutoFillBackground(False)
        self.seasontitle.setAlignment(QtCore.Qt.AlignCenter)
        self.seasontitle.setObjectName("seasontitle")
        self.season = QtWidgets.QLineEdit(self.start)
        self.season.setGeometry(QtCore.QRect(740, 400, 113, 20))
        self.season.setObjectName("season")
        self.citytitle = QtWidgets.QLabel(self.start)
        self.citytitle.setGeometry(QtCore.QRect(530, 510, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.citytitle.setFont(font)
        self.citytitle.setAutoFillBackground(False)
        self.citytitle.setAlignment(QtCore.Qt.AlignCenter)
        self.citytitle.setObjectName("citytitle")
        self.city = QtWidgets.QLineEdit(self.start)
        self.city.setGeometry(QtCore.QRect(530, 550, 113, 20))
        self.city.setToolTip("")
        self.city.setToolTipDuration(8)
        self.city.setText("")
        self.city.setObjectName("city")
        self.sportitle = QtWidgets.QLabel(self.start)
        self.sportitle.setGeometry(QtCore.QRect(950, 220, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sportitle.setFont(font)
        self.sportitle.setAutoFillBackground(False)
        self.sportitle.setAlignment(QtCore.Qt.AlignCenter)
        self.sportitle.setObjectName("sportitle")
        self.sport = QtWidgets.QLineEdit(self.start)
        self.sport.setGeometry(QtCore.QRect(950, 250, 113, 20))
        self.sport.setObjectName("sport")
        self.eventtitle = QtWidgets.QLabel(self.start)
        self.eventtitle.setGeometry(QtCore.QRect(950, 370, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.eventtitle.setFont(font)
        self.eventtitle.setAutoFillBackground(False)
        self.eventtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.eventtitle.setObjectName("eventtitle")
        self.event = QtWidgets.QLineEdit(self.start)
        self.event.setGeometry(QtCore.QRect(950, 400, 113, 20))
        self.event.setObjectName("event")
        self.medaltitle = QtWidgets.QLabel(self.start)
        self.medaltitle.setGeometry(QtCore.QRect(740, 520, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.medaltitle.setFont(font)
        self.medaltitle.setAutoFillBackground(False)
        self.medaltitle.setAlignment(QtCore.Qt.AlignCenter)
        self.medaltitle.setObjectName("medaltitle")
        self.medal = QtWidgets.QLineEdit(self.start)
        self.medal.setGeometry(QtCore.QRect(740, 550, 113, 20))
        self.medal.setToolTip("")
        self.medal.setToolTipDuration(8)
        self.medal.setText("")
        self.medal.setObjectName("medal")
        self.resultsButton = QtWidgets.QPushButton(self.start)
        self.resultsButton.setGeometry(QtCore.QRect(950, 520, 121, 41))
        self.resultsButton.clicked.connect(self.getResults)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resultsButton.setFont(font)
        self.resultsButton.setObjectName("resultsButton")
        self.stackedWidget.addWidget(self.start)
        self.resultspage = QtWidgets.QWidget()
        self.resultspage.setObjectName("results-page")
        self.resultstitle = QtWidgets.QLabel(self.resultspage)
        self.resultstitle.setGeometry(QtCore.QRect(275, 20, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.resultstitle.setFont(font)
        self.resultstitle.setAlignment(QtCore.Qt.AlignCenter)
        self.resultstitle.setObjectName("resultstitle")
        self.table = QtWidgets.QTableWidget(0,15,self.resultspage)
        self.table.setGeometry(40, 140,1000, 400)
        self.table.resizeRowsToContents()
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Sex", "Age","Height", "Weight", "Team","NOC", "Games", "Year","Season", "City", "Sport", "Event", "Medal"])
        self.noresultstitle = QtWidgets.QLabel(self.resultspage)
        self.noresultstitle.setGeometry(QtCore.QRect(380, 340, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.noresultstitle.setFont(font)
        self.noresultstitle.setAutoFillBackground(False)
        self.noresultstitle.setAlignment(QtCore.Qt.AlignCenter)
        self.noresultstitle.setObjectName("noresultstitle")
        self.noresultstitle.setHidden(True)
        self.againButton = QtWidgets.QPushButton(self.resultspage)
        self.againButton.setGeometry(QtCore.QRect(470, 560, 121, 41))
        self.againButton.clicked.connect(self.reset)
        self.stackedWidget.addWidget(self.resultspage)
        self.verticalLayout_26.addWidget(self.frame)
        MainWindow.setCentralWidget(self.firstpage)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getResults(self):
        self.stackedWidget.setCurrentIndex(1)
        print('results')
        self.nameinput = self.firstname.text() + ' ' + self.lastname.text()
        self.sexinput = self.sex.currentText()
        self.ageinput = self.age.text()
        self.heightinput = self.height.text()
        self.weightinput = self.weight.text()
        self.teaminput = self.team.text()
        self.nocinput = self.noc.text()
        self.yearinput = self.year.text()
        self.seasoninput = self.season.text()
        self.cityinput = self.city.text()
        self.sportinput = self.sport.text()
        self.eventinput = self.event.text()
        self.medalinput = self.medal.text()
        for widget in self.start.children():
         if isinstance(widget, QtWidgets.QLineEdit or QtWidgets.QComboBox):
              widget.clear()
        self.getQuery()
        self.loadData()

    def getQuery(self):
        self.query = "SELECT * FROM athlete_events WHERE"
        if (self.nameinput == ''):
             print('')
        else: self.query = f"{self.query}" + " Name=" + f"\"{self.nameinput.title()}\"";
        if (self.sexinput == '' or 'Any'):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Sex=" + f"\"{self.sexinput}\"";
        if (self.ageinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Age=" + f"{int(self.ageinput)}";
        if (self.heightinput == ''):
             print('')
        else: self.query = f"{self.query}" + " AND" + " Height=" + f"{int(self.heightinput)}";
        if (self.weightinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Weight=" + f"{int(self.weightinput)}";
        if (self.teaminput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Team=" + f"\"{self.teaminput.title()}\"";
        if (self.nocinput== ''):
             print('')
        else: self.query = f"{self.query}" + " AND" + " NOC=" + f"\"{self.nocinput.upper()}\""; 
        if (self.yearinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Year=" + f"{int(self.yearinput)}";
        if (self.seasoninput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Season=" + f"\"{self.seasoninput.title()}\"";
        if (self.cityinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " City=" + f"\"{self.cityinput.title()}\"";
        if (self.sportinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Sport=" + f"\"{self.sportinput.title()}\"";
        if (self.eventinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Event=" + f"\"{self.eventinput.title()}\"";
        if (self.medalinput == ''):
             print('')
        else: self.query =  f"{self.query}" + " AND" + " Medal=" + f"\"{self.medalinput.title()}\"";
    def loadData(self):
        print(self.query)
        connection = sqlite3.connect('olympics2.db')
        self.results = connection.execute(self.query).fetchall()
        self.displayResults()

    def displayResults(self):
         print(self.results)
         if(self.results == []):
             self.noresultstitle.setHidden(False)
         else:
             self.table.setRowCount(len(self.results))
             for i, row_data in enumerate(self.results):
                for j,data in enumerate(row_data):
                    self.item = QtWidgets.QTableWidgetItem()
                    self.item.setData(QtCore.Qt.DisplayRole, data)
                    self.table.setItem(i,j,self.item)
                    self.item.setFlags(QtCore.Qt.ItemIsEnabled)

    def reset(self):
        self.stackedWidget.setCurrentIndex(0)
        self.query = "SELECT * FROM athlete_events WHERE"
        self.table.setRowCount(0)
        self.noresultstitle.setHidden(True)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headtitle.setText(_translate("MainWindow", "Database of all athletes who ever competed in the Olympics"))
        self.subtitle.setText(_translate("MainWindow", "To search for something specific fill in the form below. First name and last name are necessary. For a higher chance of result please fill in their full names including second and third names."))
        self.firstnametitle.setText(_translate("MainWindow", "First name"))
        self.lastnametitle.setText(_translate("MainWindow", "Last  name"))
        self.weighttitle.setText(_translate("MainWindow", "Weight"))
        self.heighttitle.setText(_translate("MainWindow", "Height"))
        self.agetitle.setText(_translate("MainWindow", "Age"))
        self.sextitle.setText(_translate("MainWindow", "Sex"))
        self.sex.setItemText(2, _translate("MainWindow", "F"))
        self.sex.setItemText(1, _translate("MainWindow", "M"))
        self.sex.setItemText(0, _translate("MainWindow", "Any"))
        self.teamtitle.setText(_translate("MainWindow", "Team"))
        self.noctitle.setText(_translate("MainWindow", "NOC"))
        self.yeartitle.setText(_translate("MainWindow", "Year"))
        self.seasontitle.setText(_translate("MainWindow", "Season"))
        self.citytitle.setText(_translate("MainWindow", "City"))
        self.sportitle.setText(_translate("MainWindow", "Sport"))
        self.eventtitle.setText(_translate("MainWindow", "Event"))
        self.medaltitle.setText(_translate("MainWindow", "Medal"))
        self.resultsButton.setText(_translate("MainWindow", "Results"))
        self.resultstitle.setText(_translate("MainWindow", "Results"))
        self.againButton.setText(_translate("MainWindow", "Try Again"))
        self.noresultstitle.setText(_translate("MainWindow", "No results where recieved."))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
