from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from datetime import date
import sqlite3, csv 
from random import randint, choice 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 615)
        MainWindow.setMinimumSize(QtCore.QSize(880, 615))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(10, 10, 861, 561))
        self.gridFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gridFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 20, 20, 50)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.TitleLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setTextFormat(QtCore.Qt.PlainText)
        self.TitleLabel.setObjectName("TitleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TitleLabel)
        self.TitleLineEdit = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLineEdit.sizePolicy().hasHeightForWidth())
        self.TitleLineEdit.setSizePolicy(sizePolicy)
        self.TitleLineEdit.setMinimumSize(QtCore.QSize(210, 20))
        self.TitleLineEdit.setObjectName("TitleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TitleLineEdit)
        self.DateLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateLabel.sizePolicy().hasHeightForWidth())
        self.DateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.DateLabel)
        self.DateEdit = QtWidgets.QDateEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateEdit.sizePolicy().hasHeightForWidth())
        self.DateEdit.setSizePolicy(sizePolicy)
        self.DateEdit.setMinimumSize(QtCore.QSize(210, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateEdit.setFont(font)
        self.DateEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DateEdit.setObjectName("DateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DateEdit)
        self.CurrencyLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrencyLabel.sizePolicy().hasHeightForWidth())
        self.CurrencyLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CurrencyLabel.setFont(font)
        self.CurrencyLabel.setObjectName("CurrencyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.CurrencyLabel)
        self.CurrencyLineEdit = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CurrencyLineEdit.sizePolicy().hasHeightForWidth())
        self.CurrencyLineEdit.setSizePolicy(sizePolicy)
        self.CurrencyLineEdit.setMinimumSize(QtCore.QSize(210, 20))
        self.CurrencyLineEdit.setObjectName("CurrencyLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.CurrencyLineEdit)
        self.AmountLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AmountLabel.sizePolicy().hasHeightForWidth())
        self.AmountLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AmountLabel.setFont(font)
        self.AmountLabel.setObjectName("AmountLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.AmountLabel)
        self.AmountLineEdit = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AmountLineEdit.sizePolicy().hasHeightForWidth())
        self.AmountLineEdit.setSizePolicy(sizePolicy)
        self.AmountLineEdit.setMinimumSize(QtCore.QSize(210, 20))
        self.AmountLineEdit.setObjectName("AmountLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.AmountLineEdit)
        self.PaymentModeLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PaymentModeLabel.sizePolicy().hasHeightForWidth())
        self.PaymentModeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PaymentModeLabel.setFont(font)
        self.PaymentModeLabel.setObjectName("PaymentModeLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.PaymentModeLabel)
        self.PaymentModeLineEdit = QtWidgets.QLineEdit(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PaymentModeLineEdit.sizePolicy().hasHeightForWidth())
        self.PaymentModeLineEdit.setSizePolicy(sizePolicy)
        self.PaymentModeLineEdit.setMinimumSize(QtCore.QSize(210, 20))
        self.PaymentModeLineEdit.setObjectName("PaymentModeLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.PaymentModeLineEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.DescriptionLabel = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescriptionLabel.sizePolicy().hasHeightForWidth())
        self.DescriptionLabel.setSizePolicy(sizePolicy)
        self.DescriptionLabel.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DescriptionLabel.setFont(font)
        self.DescriptionLabel.setObjectName("DescriptionLabel")
        self.verticalLayout.addWidget(self.DescriptionLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.DescriptionPlainTextEdit = QtWidgets.QPlainTextEdit(self.gridFrame)
        self.DescriptionPlainTextEdit.setMinimumSize(QtCore.QSize(210, 40))
        self.DescriptionPlainTextEdit.setTabChangesFocus(True)
        self.DescriptionPlainTextEdit.setObjectName("DescriptionPlainTextEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DescriptionPlainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ResetPushButton = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResetPushButton.sizePolicy().hasHeightForWidth())
        self.ResetPushButton.setSizePolicy(sizePolicy)
        self.ResetPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.ResetPushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ResetPushButton.setFont(font)
        self.ResetPushButton.setObjectName("ResetPushButton")
        self.horizontalLayout.addWidget(self.ResetPushButton)
        self.SubmitPushButton = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitPushButton.sizePolicy().hasHeightForWidth())
        self.SubmitPushButton.setSizePolicy(sizePolicy)
        self.SubmitPushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.SubmitPushButton.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        self.SubmitPushButton.setFont(font)
        self.SubmitPushButton.setObjectName("SubmitPushButton")
        self.horizontalLayout.addWidget(self.SubmitPushButton)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.DatabaseTableView = QtWidgets.QTableView(self.gridFrame)
        self.DatabaseTableView.setMinimumSize(QtCore.QSize(0, 200))
        self.DatabaseTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.DatabaseTableView.setObjectName("DatabaseTableView")
        self.DatabaseTableView.horizontalHeader().setVisible(True)
        self.DatabaseTableView.horizontalHeader().setStretchLastSection(True)
        self.DatabaseTableView.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.DatabaseTableView, 1, 0, 1, 2)
        self.graphWidget = PlotWidget(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)
        self.graphWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout.addWidget(self.graphWidget, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.ExtraMenu = QtWidgets.QMenu(self.menubar)
        self.ExtraMenu.setObjectName("ExtraMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionExport_to_Excel = QtWidgets.QAction(MainWindow)
        self.actionExport_to_Excel.setObjectName("actionExport_to_Excel")
        self.actionImport_from_Excel = QtWidgets.QAction(MainWindow)
        self.actionImport_from_Excel.setObjectName("actionImport_from_Excel")
        self.ExportToCsv_action = QtWidgets.QAction(MainWindow)
        self.ExportToCsv_action.setObjectName("ExportToCsv_action")
        self.ImportFromCsv_action = QtWidgets.QAction(MainWindow)
        self.ImportFromCsv_action.setObjectName("ImportFromCsv_action")
        self.Refresh_action = QtWidgets.QAction(MainWindow)
        self.Refresh_action.setObjectName("Refresh_action")
        self.DeleteRecords_action = QtWidgets.QAction(MainWindow)
        self.DeleteRecords_action.setObjectName("DeleteRecords_action")
        self.ExtraMenu.addAction(self.ExportToCsv_action)
        self.ExtraMenu.addAction(self.ImportFromCsv_action)
        self.ExtraMenu.addSeparator()
        self.ExtraMenu.addAction(self.Refresh_action)
        self.ExtraMenu.addSeparator()
        self.ExtraMenu.addAction(self.DeleteRecords_action)
        self.menubar.addAction(self.ExtraMenu.menuAction())
        self.TitleLabel.setBuddy(self.TitleLineEdit)
        self.DateLabel.setBuddy(self.DateEdit)
        self.CurrencyLabel.setBuddy(self.CurrencyLineEdit)
        self.AmountLabel.setBuddy(self.AmountLineEdit)
        self.PaymentModeLabel.setBuddy(self.PaymentModeLineEdit)
        self.DescriptionLabel.setBuddy(self.DescriptionPlainTextEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.TitleLineEdit, self.DateEdit)
        MainWindow.setTabOrder(self.DateEdit, self.CurrencyLineEdit)
        MainWindow.setTabOrder(self.CurrencyLineEdit, self.AmountLineEdit)
        MainWindow.setTabOrder(self.AmountLineEdit, self.PaymentModeLineEdit)
        MainWindow.setTabOrder(self.PaymentModeLineEdit, self.DescriptionPlainTextEdit)
        MainWindow.setTabOrder(self.DescriptionPlainTextEdit, self.SubmitPushButton)
        MainWindow.setTabOrder(self.SubmitPushButton, self.ResetPushButton)
        MainWindow.setTabOrder(self.ResetPushButton, self.DatabaseTableView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "&Title*:"))
        self.DateLabel.setText(_translate("MainWindow", "&Date:"))
        self.DateEdit.setDisplayFormat(_translate("MainWindow", "dd-MMM-yyyy"))
        self.CurrencyLabel.setText(_translate("MainWindow", "&Currency*:"))
        self.AmountLabel.setText(_translate("MainWindow", "&Amount*:"))
        self.PaymentModeLabel.setText(_translate("MainWindow", "&Mode of Payment*:"))
        self.DescriptionLabel.setText(_translate("MainWindow", "D&escription:"))
        self.ResetPushButton.setText(_translate("MainWindow", "Reset"))
        self.SubmitPushButton.setText(_translate("MainWindow", "&Submit"))
        self.ExtraMenu.setTitle(_translate("MainWindow", "E&xtras"))
        self.actionExport_to_Excel.setText(_translate("MainWindow", "Export to Excel..."))
        self.actionImport_from_Excel.setText(_translate("MainWindow", "Import from Excel"))
        self.ExportToCsv_action.setText(_translate("MainWindow", "Export to .csv"))
        self.ImportFromCsv_action.setText(_translate("MainWindow", "Import from .csv"))
        self.Refresh_action.setText(_translate("MainWindow", "Refresh"))
        self.Refresh_action.setShortcut(_translate("MainWindow", "Alt+F"))
        self.DeleteRecords_action.setText(_translate("MainWindow", "Delete records..."))



class MainWindow(QMainWindow):

    # All UI elements must be called/referred to by using ui.<ui-element-name> because ui is the object declared and set on line 298 and 299 
    ''' ui object is declared with self.ui in the MainWindow class. So, ui can be accessed outside the class as well but inside the class, you have to call 
        it with the help of self.ui 
    '''

    def __init__(self, *args, **kwargs):
        ''' Constructor '''

        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        


        self.setCentralWidget(self.ui.gridFrame)

        #Setup database 
        self.connection = sqlite3.connect("TrackerDB.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS dataTable (ID INTEGER NOT NULL, Title TEXT NOT NULL, TransactionDate TEXT NOT NULL, \
            Currency TEXT NOT NULL, Amount REAL NOT NULL,PaymentMode TEXT NOT NULL,Description TEXT, PRIMARY KEY(ID AUTOINCREMENT));")

        self.reset_fields()        
        self.plot()
        self.set_database_table()

    def plot(self):
        ''' Function to plot the graph '''

        self.ui.graphWidget.setBackground('#f0f0f0')
        self.ui.graphWidget.showGrid(x = True, y = True)
        self.ui.graphWidget.addLegend()

        # Get all the months before current month and rotate them to sort them on the basis of their precedence. 
        months = "Jan-Feb-Mar-Apr-May-Jun-Jul-Aug-Sep-Oct-Nov-Dec".split("-")

        current_month = int(date.today().strftime("%m"))
        current_year = int(date.today().strftime("%Y"))

        months = months[:current_month][::-1] + months[current_month:][::-1]
        months.reverse()
        months_copy = months.copy() # Creating a copy so it can be used as labels 

        for i in range(11,-1,-1):
            months[i] = months[i] + '-' + str(current_year)
            if months[i] == 'Jan-'+str(current_year): 
                current_year -= 1 

        current_year += 1

        # Get all the different currencies present in the database

        command_for_currencies = "SELECT DISTINCT Currency FROM dataTable;"
        self.cursor.execute(command_for_currencies)
        currencies = self.cursor.fetchall()
        currencies = [x[0] for x in currencies]

        # Create labels for the graph 

        month_labels = [ 
                    # Generate a list of tuples (x_value, x_label)
                    (m,months_copy[m])
                    for m in range(0,12)
                ]


        # Get data and plot it 

        pg.setConfigOptions(antialias = True)
        for c in currencies:
            dataList = []
            for month in months:
                command = "SELECT sum(Amount) FROM dataTable WHERE TransactionDate LIKE '%{0}' AND Currency LIKE '%{1}%' ;"
                self.cursor.execute(command.format(month, c))
                dataList.append(self.cursor.fetchone()[0])

            pen = pg.mkPen(color = (randint(50,200), randint(50,250), randint(50,250)))
            dataList = [0 if x is None else x for x in dataList] # Replace all the None values with 0 

            self.ui.graphWidget.plot(range(0,12), dataList, pen = pen, symbolPen = pen, \
                labels = month_labels, name = c, symbol = choice(['o', 't', 't1', 't2', 't3', 's', 'p', 'h', '+', 'x']), symbolBrush = 0.2, symbolSize = 5)
            ax = self.ui.graphWidget.getAxis('bottom')
            ax.setTicks([month_labels])
        
    def set_today(self):
        ''' Function to set dateEdit to today's date '''

        d = date.today().strftime("%d %m %Y").split()
        d1 = QDate(int(d[2]), int(d[1]), int(d[0]))
        self.ui.DateEdit.setDate(d1)

    def reset_fields(self):
        ''' Function to reset all fields in the form '''

        self.ui.TitleLineEdit.clear()
        self.set_today()
        self.ui.CurrencyLineEdit.clear()
        self.ui.AmountLineEdit.clear()
        self.ui.PaymentModeLineEdit.clear()
        self.ui.DescriptionPlainTextEdit.clear()
        self.ui.TitleLineEdit.setFocus()

    def submit_fields(self):
        ''' Function to Handle the click of Submit button '''

        # get values of all Fields 
        flag = True  #Using flag to check if data is appropriate (apt)
        Title = self.ui.TitleLineEdit.text()
        Date = self.ui.DateEdit.date().toString("dd-MMM-yyyy")

        Currency = self.ui.CurrencyLineEdit.text()
        Amount = self.ui.AmountLineEdit.text()
        PaymentMode = self.ui.PaymentModeLineEdit.text()
        Description = self.ui.DescriptionPlainTextEdit.toPlainText()
        

        # Check if the fields hold data and that the data is apt 
        if (Title == "" or Currency == "" or Amount == "" or PaymentMode == ""):
            self.ui.statusBar.showMessage("Please fill all fields with \"*\". Leaving Date unchanged assumes today's date")
            flag = False 
            return
        try: 
            Amount = float(Amount)
        except:
            self.ui.statusBar.showMessage("Enter only numbers in the Amount field")
            flag = False 
            self.ui.AmountLineEdit.clear()
            return 


        # Execute following if the data is apt (add to database)
        if flag: 
            #print(Title + "\n" + Date + "\n"+ Currency + "\n"+ str(Amount) + "\n"+ PaymentMode + "\n"+ Description + "\n" + "#"*30)
             
            self.cursor.execute("INSERT INTO dataTable VALUES (NULL,?,?,?,?,?,?)", (Title, Date, Currency, Amount, PaymentMode, Description))
            self.connection.commit()
            self.reset_fields()
            self.refresh()

    def refresh(self):
        ''' Function to refresh the QTableView'''


        self.model.select()
        self.ui.DatabaseTableView.resizeColumnsToContents()
        
        
        self.ui.graphWidget.clear()
        self.plot()
        
    def set_database_table(self):
        ''' Function to display database table in QTableView '''

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("TrackerDB.db")
        db.open()
        self.model = QSqlTableModel(None, db)
        self.model.setTable("dataTable")
        self.model.select()
        self.ui.DatabaseTableView.setModel(self.model)
        self.ui.DatabaseTableView.setSortingEnabled(True)
        self.ui.DatabaseTableView.resizeColumnsToContents()
        
    def convert_Database_to_csv(self):
        ''' Function to convert the Database contents to csv '''

        path = QFileDialog.getSaveFileName(self, "Save Exported File as")[0]
        print(type(path))
        if path: 
            if path.endswith('.csv'):
                pass 
            else: 
                path += ".csv"

            self.cursor.execute("select * from dataTable")
            with open(path, "w", newline = '') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=",")
                csv_writer.writerow([i[0] for i in self.cursor.description])
                csv_writer.writerows(self.cursor)

            
            self.ui.statusBar.showMessage("Data exported Successfully into {}".format(path), 3000)

    def convert_csv_to_Database(self):
        ''' Function to convert a csv file to database table '''

        path = QFileDialog.getOpenFileName(self, "Select .csv File to import from")[0]

        try: 
            if path and path.endswith(".csv"):
                with open(path, 'r') as csv_file:
                    dr = csv.DictReader (csv_file)
                    
                    csv_list = [[i['Title'], i['TransactionDate'], i['Currency'], float(i['Amount']), i['PaymentMode'], i['Description']] for i in dr]
                    
                # make sure that the dates are in the format we need e.g., 07-Aug-2021   
                # The .csv file should have dates as dd-mm-yyyy
                
                to_db = []
                for x in csv_list:
                    temp = x[1].split("-")
                    temp1 = QDate(int(temp[2]), int(temp[1]), int(temp[0])).toString("dd-MMM-yyyy")
                    x[1] = temp1
                    x = tuple(x)
                    to_db.append(x)
                    

                self.cursor.executemany("INSERT INTO dataTable (ID, Title, TransactionDate, Currency, Amount, PaymentMode, Description) \
                    VALUES (NULL, ?, ?, ?, ?, ?, ?);", to_db)
                self.ui.statusBar.showMessage("Data imported successfully. Do not import same file again to avoid data duplication", 7000)
                self.connection.commit()
                self.refresh()

            else: 
                self.ui.statusBar.showMessage("Select .csv files with the same headers as the table shown", 7000)

        except: 
            self.ui.statusBar.showMessage("An error occured. Make sure the csv file has headers the same as the table \
                shown and has apt data", 10000)

    def delete_records(self):
        ''' Function to delete records '''

        text_input, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter the IDs of the records you want to delete:')

        if ok:  # Check if the "ok" button of the dialog box was pressed and do the following 

            # logic to convert "1, 5-10" to [1,5,6,7,8,9,10]

            y = text_input
            allowed_characters = "1 2 3 4 5 6 7 8 9 0 - ,".split(" ")
            y = ''.join(x if x in allowed_characters else '' for x in y)

            if y.endswith(','):
                y = y[:-1]

            x = y.split(',')

            delete_list = [] #list of record IDs that are to be deleted 
            deleted_string = '' #display this to tell the user what IDs were deleted
            for a in x:
    
                if '-' in a and a !="":
                    b = a.split('-')
                    if '' in b:
                        continue
                    deleted_string += a + ', '
                    b = [int(c) for c in b]

                    for c in range(b[0], b[1]+1):
                        delete_list.append(c)
                    
                elif a.isnumeric(): 
                    delete_list.append(int(a))
                    deleted_string += a + ', '

            if deleted_string.endswith(", "):
                deleted_string = deleted_string[:-2]
            
            for x in delete_list:
                self.cursor.execute("DELETE FROM dataTable WHERE ID = ?", (x,))

            self.connection.commit()
            self.refresh()
            self.ui.statusBar.showMessage("IDs of the records that were deleted: "+deleted_string, 10000)
# Instantiate the application and set style 

app = QApplication([])
app.setStyle("Fusion")
app.setApplicationName("Expense Tracker")
main_window = MainWindow()

main_window.setWindowTitle("Expense Tracker")

main_window.show()


#Connect the buttons to their functions. Connect signals to slots 

main_window.ui.ResetPushButton.clicked.connect(main_window.reset_fields)
main_window.ui.SubmitPushButton.clicked.connect(main_window.submit_fields)
main_window.ui.Refresh_action.triggered.connect(main_window.refresh)
main_window.ui.ExportToCsv_action.triggered.connect(main_window.convert_Database_to_csv)
main_window.ui.ImportFromCsv_action.triggered.connect(main_window.convert_csv_to_Database)
main_window.ui.DeleteRecords_action.triggered.connect(main_window.delete_records)
app.exec_()