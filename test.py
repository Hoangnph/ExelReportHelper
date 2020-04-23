# view in: https://www.datacamp.com/community/tutorials/python-excel-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-522010995285:dsa-473406585595&utm_loc_interest_ms=&utm_loc_physical_ms=1028580&gclid=CjwKCAjwkPX0BRBKEiwA7THxiNyq0PaVzt_BBiigbsgiVTdWvCDlF5ygLx6mDDSdgxfFGmkuu1eXTBoCS9EQAvD_BwE
# pip install -U pip setuptools
# pip install -U pandas
# pip install -U xlrd
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import datetime
import smtplib


# Khai bao bien global
getTodayDate = datetime.date.today().strftime('%d/%m/%Y') # Định dạng: 13/01/2020
fileInputLocation = r'DailyReport_STECH.xlsx' # r: trả vể một chuỗi raw

#Tải lên các file Excel và thông tin sheet
xlsTotalSheet = pd.ExcelFile(file)
sheetArrayAll = xlsTotalSheet.sheet_names
stringAllSheet = "Đây là tất cả các sheet: {}".format(sheetArrayAll)
print(stringAllSheet)

dataframeFirstSheet = pd.DataFrame(pd.read_excel(file,0)) #-> one way to get sheet
#print(df)
bodyEmailContent=""
titleEmail = "[STECH Báo cáo ngày] Báo cáo công việc ngày {}".format(date)

for index,row in dataframeFirstSheet.iterrows():
    if row[0] == getTodayDate:
        #print(row[1],row[2],row[3])
        bodyEmailContent += "Task {} : \n {} \n \t Kết quả: \n \t \t {} \n \t Khó khăn: \n \t \t {} \n \t Đề xuất: \n \t \t {} \n \t Kế hoạch tiếp theo: \n \t \t {} \n ".format(row[1],row[2],row[3],row[4],row[5],row[6])

print(titleEmail)
print(bodyEmailContent)
