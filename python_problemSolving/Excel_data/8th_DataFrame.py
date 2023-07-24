import pandas as pd
import numpy as np

# 1차원 Series
S1 = pd.Series([1, 3, 5])
# 0, 1, 2는 index 번호 / 1, 3, 5는 Value 값
print(S1)

# index 번호 지정하기
S2 = pd.Series(['서울', '고양', '파주'], index = ['1', '2', '3'])
print(S2)

# dtype 종류 확인해보기
float = pd.Series([1.5, 2.5, 3.5], index = range(1, 4))
object = pd.Series(['가', '나', '다'], index = range(1, 4))
int = pd.Series([10, 20, 30], index = range(1, 4))
boolean = pd.Series([1.5>1, 2.5<2, 3.5>10], index = range(1, 4))
print(f'실수:\n {float}\n')
print('객체:\n{}\n'.format(object))
print('정수:\n', int, '\n')
print(f'불리안:\n{boolean}\n')

# 리스트, 튜플, 딕셔너리로 Series 만들어보기
dict_data = {1 : '서울', 2: '고양', 3:'파주', 4:'인천'}
print(dict_data)
dictToSeries = pd.Series(dict_data)
print(dictToSeries)

# 넘파이로 만든 1차원 벡터에 인덱스 지정하여 Series로 만들어보기
Data = np.arange(0, 50, 10)
print(Data)
DataToSeries = pd.Series(Data, index = ['A', 'B', 'C', 'D',' E'])
print(DataToSeries)

# 인덱스 확인(접근)해보기
# Value 확인(접근해보기)
S2 = pd.Series(['02', '031', '032', '051'], index = ['서울', '경기도', '인천', '부산'])
print(S2)
print('인덱스:\n', S2.index)
print('values:\n', S2.values)
# 인덱스에 이름 넣기
# 데이터 이름 정하기
S2.name = '번호'
S2.index.name = '도시'
print(S2)

# 2차원 DataFrame

# 딕셔너리로 Dataframe 만들어보기
dict_data = {'브랜드' : ['삼성', 'LG', '애플' ,'샤오미'], '색상' : ['검정' ,'골드' ,'실버', '그레이']}
print('딕셔너리: \n', dict_data)
df1_dict = pd.DataFrame(dict_data, index = range(1, 5))
print(df1_dict)

# 리스트로 만들기
list_data = [['삼성', '검정'], ['LG', '골드'], ['애플', '실버'], ['샤오미', '그레이']]
df2_list = pd.DataFrame(list_data, index = range(1,5), columns = ['브랜드', '색상'])
print(df2_list)

list_data2 = [['삼성', 'LG', '애플' ,'샤오미'], ['검정' ,'골드' ,'실버', '그레이']]
df3_list = pd.DataFrame(list_data2, index = ['브랜드', '색상'], columns= range(1, 5))
print(df3_list)
# numpy로 만들기

weather = pd.read_excel('C:\yhb_work\python work space\studying\Excel_data\weather2020-2021.xlsx')
print(weather)
weather.index = weather['날짜']
print(weather)

print('평균', weather['평균기온'].mean())
print('평균', weather['평균기온'].mean().__round__())
print('가장 낮은 기온:', weather['최저기온'].min())
print('가장 높은 기온:', weather['최고기온'].max())
print('평균기온 중 중간 값: ', weather['평균기온'].median())
print('평균기온 중 표준편차: ', weather['평균기온'].std().__ceil__())

# 정렬하기
print(weather.sort_values('최고기온'))
