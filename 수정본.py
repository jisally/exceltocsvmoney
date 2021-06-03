import openpyxl
import pandas as pd

wb=openpyxl.load_workbook('kabank.xlsx')
sheet=wb.active

df=pd.DataFrame(sheet.values)
df

df.columns=df.iloc[0,:]
df=df.iloc[1:,:]
df

#2021.01.01~09 일은 jan_week1_money.txt에 저장

df_3=df[df['거래일시'].str.contains('2021.01.0', na=False)]

df_4=df_3[['거래금액']]

df_4.to_csv("jan_week1_money.txt", index=False)


#-와 , " 제거
def replaceInFile(file_path, oldstr, newstr):
    fr=open(file_path, 'r')
    lines=fr.readlines()
    fr.close()

    fw=open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(oldstr, newstr))
    fw.close()

replaceInFile("jan_week1_money.txt", ",", "")
replaceInFile("jan_week1_money.txt", "-", "")
replaceInFile("jan_week1_money.txt", '"', '')


#'거래금액' 용어 제거
with open("jan_week1_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("jan_week1_money.txt", "w")as fout:
    fout.writelines(data[1:])

#==========================================================
#2021.01.10~19일은 jan_week2_money.txt에 저장
df_3=df[df['거래일시'].str.contains('2021.01.1', na=False)]

df_4=df_3[['거래금액']]

df_4.to_csv("jan_week2_money.txt", index=False)


#-와 , " 제거

replaceInFile("jan_week2_money.txt", ",", "")
replaceInFile("jan_week2_money.txt", "-", "")
replaceInFile("jan_week2_money.txt", '"', '')


#'거래금액' 용어 제거
with open("jan_week2_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("jan_week2_money.txt", "w")as fout:
    fout.writelines(data[1:])

#==========================================================
#2021.01.20~31일은 jan_week3_money.txt에 저장
df_3_1=df[df['거래일시'].str.contains('2021.01.2', na=False)]
df_3_2=df[df['거래일시'].str.contains('2021.01.3', na=False)]

df_3=pd.concat([df_3_1,df_3_2])

df_4=df_3[['거래금액']]

df_4.to_csv("jan_week3_money.txt", index=False)


#-와 , " 제거

replaceInFile("jan_week3_money.txt", ",", "")
replaceInFile("jan_week3_money.txt", "-", "")
replaceInFile("jan_week3_money.txt", '"', '')


#'거래금액' 용어 제거
with open("jan_week3_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("jan_week3_money.txt", "w")as fout:
    fout.writelines(data[1:])

#==========================================================
#2021.01월은 jan_money.txt에 저장
df_3=df[df['거래일시'].str.contains('2021.01', na=False)]

df_4=df_3[['거래금액']]

df_4.to_csv("jan_money.txt", index=False)


#-와 , " 제거

replaceInFile("jan_money.txt", ",", "")
replaceInFile("jan_money.txt", "-", "")
replaceInFile("jan_money.txt", '"', '')


#'거래금액' 용어 제거
with open("jan_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("jan_money.txt", "w")as fout:
    fout.writelines(data[1:])

#===============================================================
df_5=df[df['거래일시'].str.contains('2021.02.0', na=False)]

df_6=df_5[['거래금액']]

df_6.to_csv("feb_week1_money.txt", index=False)


#-와 , " 제거


replaceInFile("feb_week1_money.txt", ",", "")
replaceInFile("feb_week1_money.txt", "-", "")
replaceInFile("feb_week1_money.txt", '"', '')


#'거래금액' 용어 제거
with open("feb_week1_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("feb_week1_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_5=df[df['거래일시'].str.contains('2021.02.1', na=False)]

df_6=df_5[['거래금액']]

df_6.to_csv("feb_week2_money.txt", index=False)


#-와 , " 제거


replaceInFile("feb_week2_money.txt", ",", "")
replaceInFile("feb_week2_money.txt", "-", "")
replaceInFile("feb_week2_money.txt", '"', '')


#'거래금액' 용어 제거
with open("feb_week2_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("feb_week2_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_5=df[df['거래일시'].str.contains('2021.02.2', na=False)]

df_6=df_5[['거래금액']]

df_6.to_csv("feb_week3_money.txt", index=False)


#-와 , " 제거


replaceInFile("feb_week3_money.txt", ",", "")
replaceInFile("feb_week3_money.txt", "-", "")
replaceInFile("feb_week3_money.txt", '"', '')


#'거래금액' 용어 제거
with open("feb_week3_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("feb_week3_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_5=df[df['거래일시'].str.contains('2021.02', na=False)]

df_6=df_5[['거래금액']]

df_6.to_csv("feb_money.txt", index=False)


#-와 , " 제거


replaceInFile("feb_money.txt", ",", "")
replaceInFile("feb_money.txt", "-", "")
replaceInFile("feb_money.txt", '"', '')


#'거래금액' 용어 제거
with open("feb_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("feb_money.txt", "w")as fout:
    fout.writelines(data[1:])

#===============================================================
df_7=df[df['거래일시'].str.contains('2021.03.0', na=False)]

df_8=df_7[['거래금액']]

df_8.to_csv("mar_week1_money.txt", index=False)


#-와 , " 제거


replaceInFile("mar_week1_money.txt", ",", "")
replaceInFile("mar_week1_money.txt", "-", "")
replaceInFile("mar_week1_money.txt", '"', '')


#'거래금액' 용어 제거
with open("mar_week1_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("mar_week1_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_7=df[df['거래일시'].str.contains('2021.03.1', na=False)]

df_8=df_7[['거래금액']]

df_8.to_csv("mar_week2_money.txt", index=False)


#-와 , " 제거


replaceInFile("mar_week2_money.txt", ",", "")
replaceInFile("mar_week2_money.txt", "-", "")
replaceInFile("mar_week2_money.txt", '"', '')


#'거래금액' 용어 제거
with open("mar_week2_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("mar_week2_money.txt", "w")as fout:
    fout.writelines(data[1:])

#===============================================================
df_7_1=df[df['거래일시'].str.contains('2021.03.2', na=False)]
df_7_2=df[df['거래일시'].str.contains('2021.03.3', na=False)]
df_7=pd.concat([df_7_1,df_7_2])


df_8=df_7[['거래금액']]

df_8.to_csv("mar_week3_money.txt", index=False)


#-와 , " 제거


replaceInFile("mar_week3_money.txt", ",", "")
replaceInFile("mar_week3_money.txt", "-", "")
replaceInFile("mar_week3_money.txt", '"', '')


#'거래금액' 용어 제거
with open("mar_week3_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("mar_week3_money.txt", "w")as fout:
    fout.writelines(data[1:])






#===============================================================
df_7=df[df['거래일시'].str.contains('2021.03', na=False)]

df_8=df_7[['거래금액']]

df_8.to_csv("mar_money.txt", index=False)


#-와 , " 제거


replaceInFile("mar_money.txt", ",", "")
replaceInFile("mar_money.txt", "-", "")
replaceInFile("mar_money.txt", '"', '')


#'거래금액' 용어 제거
with open("mar_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("mar_money.txt", "w")as fout:
    fout.writelines(data[1:])




#===============================================================  
df_9=df[df['거래일시'].str.contains('2021.04.0', na=False)]

df_10=df_9[['거래금액']]

df_10.to_csv("apr_week1_money.txt", index=False)


#-와 , " 제거



replaceInFile("apr_week1_money.txt", ",", "")
replaceInFile("apr_week1_money.txt", "-", "")
replaceInFile("apr_week1_money.txt", '"', '')


#'거래금액' 용어 제거
with open("apr_week1_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("apr_week1_money.txt", "w")as fout:
    fout.writelines(data[1:])

#===============================================================  
df_9=df[df['거래일시'].str.contains('2021.04.1', na=False)]

df_10=df_9[['거래금액']]

df_10.to_csv("apr_week2_money.txt", index=False)


#-와 , " 제거



replaceInFile("apr_week2_money.txt", ",", "")
replaceInFile("apr_week2_money.txt", "-", "")
replaceInFile("apr_week2_money.txt", '"', '')


#'거래금액' 용어 제거
with open("apr_week2_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("apr_week2_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================  
df_9_1=df[df['거래일시'].str.contains('2021.04.2', na=False)]
df_9_2=df[df['거래일시'].str.contains('2021.04.2', na=False)]

df_9=pd.concat([df_9_1,df_9_2])

df_10=df_9[['거래금액']]

df_10.to_csv("apr_week3_money.txt", index=False)


#-와 , " 제거



replaceInFile("apr_week3_money.txt", ",", "")
replaceInFile("apr_week3_money.txt", "-", "")
replaceInFile("apr_week3_money.txt", '"', '')


#'거래금액' 용어 제거
with open("apr_week3_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("apr_week3_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================  
df_9=df[df['거래일시'].str.contains('2021.04', na=False)]

df_10=df_9[['거래금액']]

df_10.to_csv("apr_money.txt", index=False)


#-와 , " 제거



replaceInFile("apr_money.txt", ",", "")
replaceInFile("apr_money.txt", "-", "")
replaceInFile("apr_money.txt", '"', '')


#'거래금액' 용어 제거
with open("apr_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("apr_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_11=df[df['거래일시'].str.contains('2021.05.0', na=False)]

df_12=df_11[['거래금액']]

df_12.to_csv("may_week1_money.txt", index=False)


#-와 , " 제거



replaceInFile("may_week1_money.txt", ",", "")
replaceInFile("may_week1_money.txt", "-", "")
replaceInFile("may_week1_money.txt", '"', '')


#'거래금액' 용어 제거
with open("may_week1_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("may_week1_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_11=df[df['거래일시'].str.contains('2021.05.1', na=False)]

df_12=df_11[['거래금액']]

df_12.to_csv("may_week2_money.txt", index=False)


#-와 , " 제거



replaceInFile("may_week2_money.txt", ",", "")
replaceInFile("may_week2_money.txt", "-", "")
replaceInFile("may_week2_money.txt", '"', '')


#'거래금액' 용어 제거
with open("may_week2_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("may_week2_money.txt", "w")as fout:
    fout.writelines(data[1:])
#===============================================================
df_11_1=df[df['거래일시'].str.contains('2021.05.2', na=False)]
df_11_2=df[df['거래일시'].str.contains('2021.05.3', na=False)]

df_11=pd.concat([df_11_1,df_11_2])


df_12=df_11[['거래금액']]

df_12.to_csv("may_week3_money.txt", index=False)


#-와 , " 제거



replaceInFile("may_week3_money.txt", ",", "")
replaceInFile("may_week3_money.txt", "-", "")
replaceInFile("may_week3_money.txt", '"', '')


#'거래금액' 용어 제거
with open("may_week3_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("may_week3_money.txt", "w")as fout:
    fout.writelines(data[1:])

#===============================================================
df_11=df[df['거래일시'].str.contains('2021.05', na=False)]

df_12=df_11[['거래금액']]

df_12.to_csv("may_money.txt", index=False)


#-와 , " 제거



replaceInFile("may_money.txt", ",", "")
replaceInFile("may_money.txt", "-", "")
replaceInFile("may_money.txt", '"', '')


#'거래금액' 용어 제거
with open("may_money.txt", "r")as fin:
    data=fin.read().splitlines(True)
with open("may_money.txt", "w")as fout:
    fout.writelines(data[1:])

