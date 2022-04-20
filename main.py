import requests
#from pprint import pprint # 구조있는 데이터를 더 편하게 보여줌

url_im = "http://apis.data.go.kr/1661000/EmergencyStatisticsService/getTrafficAccidentEmgActStats?serviceKey=tzNdpBB6EDyPn7B1MHodkDLXb5d7rQeJ1JFMfxvFMDxnyw9ii0Kei8Lvvi946HnnhuJNqb/JLfkGEUbSddqSMg==&numOfRows=10000&pageNo=1&resultType=json&sidoHqOgidNm="

accident = ["오토바이사고", "보행자", "운전자", "기타탈것", "자전거사고", "동승자"]
s_station = ["소방재난본부", "인천소방본부", "부산소방재난본부", "대구소방안전본부","대전소방본부", "광주소방본부", "울산소방본부","강원소방본부", "충남소방본부", "충북소방본부", "경남소방본부", "경북소방본부", "전남소방본부", "전북소방본부", "제주소방안전본부", "창원소방본부", "세종소방본부" ]
p_count = [[0 for _ in range(len(accident))] for _ in range(len(s_station))]

for sido in s_station:
    url = url_im + sido
    res = requests.get(url)

    # 응답 데이터 정리
    data = res.json() # json.loads(res.text)와 같은 기능
    data = data['body']['items']

    for dict in data:
        for key, value in dict.items():
            for acc in accident:

                if key == "rlifAcdAsmCdNm" and value == acc:
                    p_count[s_station.index(sido)][accident.index(acc)] += dict["trnfPcnt"]

    url = url_im    

for i in range(len(s_station)):
    print(s_station[i] + ":" + str(p_count[i][0]))
