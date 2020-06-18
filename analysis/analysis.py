'''
depend on pandas xlrd
'''
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('红手指游戏数据.xlsx')
data['日期'] = [x.strftime('%Y-%m-%d') for x in data['游戏开始时间']]

table = pd.DataFrame(columns = ['日期','试玩次数','试玩时长','最大试玩时长','最小试玩时长','平均时长']) 

date = data['日期'].unique()
for i in date:
    count_per_day = data[data['日期']==i]['日期'].count()
    max_duration = data[data['日期']==i]['游戏时长(min)'].max()
    min_duration = data[data['日期']==i]['游戏时长(min)'].min()
    mean_duration = data[data['日期']==i]['游戏时长(min)'].mean()
    duration = data[data['日期']==i]['游戏时长(min)'].sum()
    
    table = table.append(pd.DataFrame({'日期':i,'试玩次数':[count_per_day],'试玩时长':[duration],'最大试玩时长':[max_duration],'最小试玩时长':[min_duration],'平均时长':[mean_duration]}),ignore_index = True)

print(table)

table['试玩次数'].plot()
plt.show()

#print(data)

#game = data['游戏名称'].unique()

#for i in game:
#    print(data[data['游戏名称'] == i])

#time = [x.strftime('%Y-%m-%d') for x in data['游戏开始时间']]

#print(time)

#columns =  ['试玩次数','试玩时长','最大试玩时长','最小试玩时长']

