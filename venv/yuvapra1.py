import openpyxl
def read(rowno,colno):
    wb = openpyxl.load_workbook("C:\\Users\\DELL\\Desktop\\testxl.xlsx")
    sheet = wb.active
    return sheet.cell(row=rowno,column=colno).value


# i made new changes