import xlrd
class ExcelFile():
    def __init__(self, value):
        self.name=value 
        self.rb = xlrd.open_workbook('./res/'+self.name, encoding_override='utf-8')
        self.sheet = self.rb.sheet_by_index(0)
        self.row_list=list()
        for rownum in range(self.sheet.nrows):
            self.row = self.sheet.row_values(rownum)
            self.row_list.append(self.row)
    def getRow(self,rownum):
        return self.row_list[rownum]
    def getNum(self):
        return self.sheet.nrows
