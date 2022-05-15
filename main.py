from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtGui import QIcon
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from datetime import date
import sqlite3, csv 
from random import randint, choice 


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        ''' Constructor '''

        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        #loadUi module in PyQt5.uic
        loadUi('UI.ui', self)
        self.setWindowIcon(QIcon('graph-icon.png'))
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

        self.graphWidget.setBackground('#f0f0f0')
        self.graphWidget.showGrid(x = True, y = True)
        self.graphWidget.addLegend()

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

            self.graphWidget.plot(range(0,12), dataList, pen = pen, symbolPen = pen, \
                labels = month_labels, name = c, symbol = choice(['o', 't', 't1', 't2', 't3', 's', 'p', 'h', '+', 'x']), symbolBrush = 0.2, symbolSize = 5)
            ax = self.graphWidget.getAxis('bottom')
            ax.setTicks([month_labels])
        
    def set_today(self):
        ''' Function to set dateEdit to today's date '''

        d = date.today().strftime("%d %m %Y").split()
        d1 = QDate(int(d[2]), int(d[1]), int(d[0]))
        self.DateEdit.setDate(d1)

    def reset_fields(self):
        ''' Function to reset all fields in the form '''

        self.TitleLineEdit.clear()
        self.set_today()
        self.CurrencyLineEdit.clear()
        self.AmountLineEdit.clear()
        self.PaymentModeLineEdit.clear()
        self.DescriptionPlainTextEdit.clear()
        self.TitleLineEdit.setFocus()

    def submit_fields(self):
        ''' Function to Handle the click of Submit button '''

        # get values of all Fields 
        flag = True  #Using flag to check if data is appropriate (apt)
        Title = self.TitleLineEdit.text()
        Date = self.DateEdit.date().toString("dd-MMM-yyyy")

        Currency = self.CurrencyLineEdit.text()
        Amount = self.AmountLineEdit.text()
        PaymentMode = self.PaymentModeLineEdit.text()
        Description = self.DescriptionPlainTextEdit.toPlainText()
        

        # Check if the fields hold data and that the data is apt 
        if (Title == "" or Currency == "" or Amount == "" or PaymentMode == ""):
            self.statusBar.showMessage("Please fill all fields with \"*\". Leaving Date unchanged assumes today's date")
            flag = False 
            return
        try: 
            Amount = float(Amount)
        except:
            self.statusBar.showMessage("Enter only numbers in the Amount field")
            flag = False 
            self.AmountLineEdit.clear()
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
        self.DatabaseTableView.resizeColumnsToContents()
        
        
        self.graphWidget.clear()
        self.plot()
        
    def set_database_table(self):
        ''' Function to display database table in QTableView '''

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("TrackerDB.db")
        db.open()
        self.model = QSqlTableModel(None, db)
        self.model.setTable("dataTable")
        self.model.select()
        self.DatabaseTableView.setModel(self.model)
        self.DatabaseTableView.setSortingEnabled(True)
        self.DatabaseTableView.resizeColumnsToContents()
        
    def convert_Database_to_csv(self):
        ''' Function to convert the Database contents to csv '''

        path = QFileDialog.getSaveFileName(self, "Save Exported File as")[0]
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

            
            self.statusBar.showMessage("Data exported Successfully into {}".format(path), 3000)

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

                self.statusBar.showMessage("Data imported successfully. Do not import same file again to avoid data duplication", 7000)
                self.connection.commit()
                self.refresh()

            else: 
                self.statusBar.showMessage("Select .csv files with the same headers as the table shown", 7000)

        except: 
            self.statusBar.showMessage("An error occured. Make sure the csv file has headers the same as the table shown and has apt data", 10000)

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
            self.statusBar.showMessage("IDs of the records that were deleted: "+deleted_string, 10000)
# Instantiate the application and set style 

app = QApplication([])
app.setStyle("Fusion")
app.setApplicationName("Expense Tracker")
main_window = MainWindow()
main_window.setWindowTitle("Expense Tracker")
main_window.setCentralWidget(main_window.gridFrame)
main_window.show()


#Connect the buttons to their functions. Connect signals to slots 

main_window.ResetPushButton.clicked.connect(main_window.reset_fields)
main_window.SubmitPushButton.clicked.connect(main_window.submit_fields)
main_window.Refresh_action.triggered.connect(main_window.refresh)
main_window.ExportToCsv_action.triggered.connect(main_window.convert_Database_to_csv)
main_window.ImportFromCsv_action.triggered.connect(main_window.convert_csv_to_Database)
main_window.DeleteRecords_action.triggered.connect(main_window.delete_records)
app.exec_()