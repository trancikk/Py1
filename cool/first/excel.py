import xlrd
def setExcelName(name):
    global exc_name=name
rb = xlrd.open_workbook('exc_name')
sheet = rb.sheet_by_index(0)
row_list=list()
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    row_list.append(row)
def getRow(rownum):
    return row_list[rownum]

