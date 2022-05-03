from SaveToExcel import CreateExcelFile
from WebRetrieveData import get_data
from Graph import *
import sys


def change_var_to_int(var: list):
    return [int(x.replace("$", "").replace(",", "")) for x in var]


def printMenu():
    print('1. Retrieve data from the page.\n'
          '2. Show graph.\n'
          '3. Print data.\n'
          '4. Save to EXCEL file.\n'
          'x. Exit')


def runUI():
    names = []
    prices = []
    while True:
        printMenu()
        cmc = input('Command: ')
        if cmc == '1':
            names, prices = get_data()
        elif cmc == '2':
            int_list = change_var_to_int(prices)
            app = QApplication(sys.argv)
            window = Window(names, int_list)
            window.show()
            # sys.exit(app.exec_())
            app.exec()
        elif cmc == '3':
            for i in range(len(names)):
                print(names[i], prices[i])
        elif cmc == "4":
            CreateExcelFile(names, prices)
        elif cmc == "x":
            break
        else:
            print("Wrong command !!!")
