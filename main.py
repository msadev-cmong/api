import requests
#from pprint import pprint # 구조있는 데이터를 더 편하게 보여줌

url = "http://apis.data.go.kr/1661000/EmergencyStatisticsService/getTrasferPatientByAgeGroupStats?serviceKey="
url += "tzNdpBB6EDyPn7B1MHodkDLXb5d7rQeJ1JFMfxvFMDxnyw9ii0Kei8Lvvi946HnnhuJNqb/JLfkGEUbSddqSMg=="
url += "&numOfRows=17711&pageNo=1&resultType=json&sidoHqOgidNm=소방재난본부"

s_station = ["동작소방서", "종로소방서", "중부소방서","광진소방서","용산소방서", "동대문소방서", "은평소방서", "노원소방서", "도봉소방서"
, "성동소방서", "강북소방서", "서대문소방서", "119특수구조단", "서울종합방재센터", "중랑소방서", "양천소방서",
 "송파소방서", "구로소방서", "강동소방서","강서소방서","관악소방서", "서초소방서", "강남소방서", "마포소방서"]

p_count = [[0] for _ in range(len(s_station))]

res = requests.get(url)

# 응답 데이터 정리
data = res.json() # json.loads(res.text)와 같은 기능
data = data['body']['items']


for dict in data:
    for key, value in dict.items():
        for station in s_station:
            if key == "rsacGutFsttOgidNm" and value == station:
                p_count[s_station.index(station)][0] += dict["trnfPcnt"]



# print(res.status_code, type(res.text), res.url)
# print()
# print(res.text)

k = 0

for station in s_station:
    print(station + " : " + str(p_count[k][0]))
    k += 1

a=[1,2,3,4]