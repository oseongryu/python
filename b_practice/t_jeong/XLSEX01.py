import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.WorkBOOKS.Open('C:\\Users\\cpc-001\\Desktop\\제조원가-생산품.xlsx')
ws = wb.ActiveSheet

print(ws.Cells(1, 1).value)
excel.Quit()