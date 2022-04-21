import pandas as pd
data = pd.read_csv('전국_이송환자수.csv')
sido = data.where((pd.notnull(data)), None)
for i in range(len(sido)):
    print(tuple(sido.values[i]))