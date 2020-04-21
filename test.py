# view in: https://www.datacamp.com/community/tutorials/python-excel-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-522010995285:dsa-473406585595&utm_loc_interest_ms=&utm_loc_physical_ms=1028580&gclid=CjwKCAjwkPX0BRBKEiwA7THxiNyq0PaVzt_BBiigbsgiVTdWvCDlF5ygLx6mDDSdgxfFGmkuu1eXTBoCS9EQAvD_BwE
# pip install -U pip setuptools
# pip install -U pandas
# pip install -U xlrd
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime

root = tk.Tk()

# Khai bao bien global
date = datetime.date.today().strftime('%d/%m/%Y')
file = r'DailyReport_STECH.xlsx'

#Load spreadsheet
xls= pd.ExcelFile(file)
sheet = xls.sheet_names
string = "Here is all sheet: {}".format(sheet)
print(string)

df = pd.DataFrame(pd.read_excel(file,0))
#print(df)
bodyContent=""
title = "[STECH Báo cáo ngày] Báo cáo công việc ngày {}".format(date)


for index,row in df.iterrows():
    if row[0] == date:
        #print(row[1],row[2],row[3])
        bodyContent += "Task {} : \n {} \n \t Kết quả: \n \t \t {} \n \t Khó khăn: \n \t \t {} \n \t Đề xuất: \n \t \t {} \n \t Kế hoạch tiếp theo: \n \t \t {} \n ".format(row[1],row[2],row[3],row[4],row[5],row[6])

print(title)
print(bodyContent)
