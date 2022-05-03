import xlsxwriter


def CreateExcelFile(names: list, prices: list):
    workbook = xlsxwriter.Workbook('Cars.xlsx')

    worksheet = workbook.add_worksheet()

    italic = workbook.add_format({'italic': 1})

    data1 = ['Car', 'Price']
    data2 = [names, prices]

    worksheet.write_row('A1', data1, italic)

    worksheet.write_column('A2', data2[0])
    worksheet.write_column('B2', data2[1])

    worksheet.set_column('B:C', 15)

    workbook.close()
