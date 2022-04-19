from this import d
import requests
import pandas as pd 
from pandas.io.json import json_normalize

url = "http://apis.data.go.kr/1661000/EmergencyStatisticsService/getTrafficAccidentEmgActStats"
service_key = "tzNdpBB6EDyPn7B1MHodkDLXb5d7rQeJ1JFMfxvFMDxnyw9ii0Kei8Lvvi946HnnhuJNqb/JLfkGEUbSddqSMg=="

# 웹 요청시 같이 전달될 데이터 = 요청 메시지
params = {
    'serviceKey' : service_key,
    'numOfRows' : 10000,
    'pageNo' : 1,
    'resultType' : 'json',
    'sidoHqOgidNm' : '인천소방본부',
    #'rsacGutFsttOgidNm' : '부평소방서',
    #'rcptYm' : '202101',
    #'rlifOccrTyCdNm' : '기타'
}

res = requests.get(url=url , params=params)
# print(res.status_code, type(res.text), res.url)
# print()
# print(res.text)

# 응답 데이터 정리
from pprint import pprint  # 구조있는 데이터를 더 편하게 보여줌
data = res.json() # json.loads(res.text)와 같은 기능
data = data['body']['items']
#pprint(data)

df = pd.DataFrame(data,columns = ['rcptYm','trnfCo','trnfPcnt','rlifAcdAsmCdNm'])
print(df)
