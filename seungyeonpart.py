##소창 기말고사 대체 팀플 내파트

import openpyxl
import pandas as pd

wb=openpyxl.load_workbook('kabank.xlsx')
sheet=wb.active

df=pd.DataFrame(sheet.values)
df

df.columns=df.iloc[0,:]
df=df.iloc[1:,:]
df



df_3=df[df['거래일시'].str.contains('2021.01', na=False)]

df_4=df_3[['거래금액']]

df_4.to_csv("jan_money.txt", index=False)


#-와 , " 제거
def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("jan_money.txt", ",", "")
replaceInFile("jan_money.txt", "-", "")
replaceInFile("jan_money.txt", '"', '')


#'거래금액' 용어 제거
with open("jan_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("jan_money.txt", "w")as fout:
    fout.writelines(data[1:])


#===============================================================
df_5=df[df['거래일시'].str.contains('2021.02', na=False)]

df_6=df_5[['거래금액']]

df_6.to_csv("feb_money.txt", index=False)


#-와 , " 제거

def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("feb_money.txt", ",", "")
replaceInFile("feb_money.txt", "-", "")
replaceInFile("feb_money.txt", '"', '')


#'거래금액' 용어 제거
with open("feb_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("feb_money.txt", "w")as fout:
    fout.writelines(data[1:])



#===============================================================
df_7=df[df['거래일시'].str.contains('2021.03', na=False)]

df_8=df_7[['거래금액']]

df_8.to_csv("mar_money.txt", index=False)


#-와 , " 제거

def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("mar_money.txt", ",", "")
replaceInFile("mar_money.txt", "-", "")
replaceInFile("mar_money.txt", '"', '')


#'거래금액' 용어 제거
with open("mar_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("mar_money.txt", "w")as fout:
    fout.writelines(data[1:])




#===============================================================  
df_9=df[df['거래일시'].str.contains('2021.04', na=False)]

df_10=df_9[['거래금액']]

df_10.to_csv("apr_money.txt", index=False)


#-와 , " 제거

def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("apr_money.txt", ",", "")
replaceInFile("apr_money.txt", "-", "")
replaceInFile("apr_money.txt", '"', '')


#'거래금액' 용어 제거
with open("apr_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("apr_money.txt", "w")as fout:
    fout.writelines(data[1:])


#===============================================================
df_11=df[df['거래일시'].str.contains('2021.05', na=False)]

df_12=df_11[['거래금액']]

df_12.to_csv("may_money.txt", index=False)


#-와 , " 제거

def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("may_money.txt", ",", "")
replaceInFile("may_money.txt", "-", "")
replaceInFile("may_money.txt", '"', '')


#'거래금액' 용어 제거
with open("may_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("may_money.txt", "w")as fout:
    fout.writelines(data[1:])
