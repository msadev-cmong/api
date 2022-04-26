import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "NanumGothic"


df = pd.read_csv('전국_이송환자수_행.csv')
print(df)
#print(df.describe())
# df = pd.DataFrame({'team': ['A', 'A', 'B', 'B', 'B', 'B', 'C', 'C'],
#                    'points': [25, 12, 25, 14, 19, 53, 25, 29]})
#df.groupby(['team']).sum().plot(kind='pie', y='points')

# df.groupby(['sido']).sum().plot(kind='pie', y='count',# autopct='%1.0f%%',
#                                 colors = ['red', 'pink', 'steelblue','green'],
#                                 title='전국 이송환자수 통계')
plt.pie(df['count'], labels=df['sido'], 
        shadow=False, startangle=90, autopct='%1.2f%%')
plt.rc("font", family='NanumGothic')
plt.title("원그래프(pie)")
plt.axis('equal')
plt.show()
