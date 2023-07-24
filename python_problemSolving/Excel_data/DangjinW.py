import pandas as pd
Dangjin2020_05 = pd.read_excel('C:\yhb_work\python work space\studying\Excel_data\Dangjin2020.05.xlsx', engine= 'openpyxl')
# print(type(Dangjin2020_05))
Dangjin2020_05 = Dangjin2020_05.drop([1])
print(Dangjin2020_05)
print(Dangjin2020_05[['평균기온(°C)', '일강수량(mm)', '일시']])