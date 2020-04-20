# view in: https://www.datacamp.com/community/tutorials/python-excel-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-522010995285:dsa-473406585595&utm_loc_interest_ms=&utm_loc_physical_ms=1028580&gclid=CjwKCAjwkPX0BRBKEiwA7THxiNyq0PaVzt_BBiigbsgiVTdWvCDlF5ygLx6mDDSdgxfFGmkuu1eXTBoCS9EQAvD_BwE
# pip install -U pip setuptools
# pip install -U pandas
# pip install -U xlrd
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

# canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteel')
# Assign spreadsheet filename to `file`
# r character is define draw String.
file = r'PlanNow.xlsx'

#Load spreadsheet
data = pd.read_excel(file)
df = pd.DataFrame(data, columns= ['Project Planner','Unnamed: 2'])
print(df)
