# -------------------------------
# 라이브러리 import
# -------------------------------

import urllib.request      # HTTP 요청을 보내기 위한 라이브러리
import json                # JSON 형식 데이터를 처리하기 위한 라이브러리
import tkinter             # GUI(그래픽 사용자 인터페이스)를 만들기 위한 라이브러리
import tkinter.font        # GUI에서 사용할 폰트 설정 라이브러리


# -------------------------------
# API 키 설정 (반드시 본인 키로 수정)
# -------------------------------

API_KEY = "Enter your API key here"  # OpenWeatherMap에서 발급받은 API 키 입력


# -------------------------------
# 날씨 데이터 요청 및 GUI 업데이트 함수
# -------------------------------

def tick1Min():
    # OpenWeatherMap API 요청 URL 구성 (서울 기준, 섭씨 단위)
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid={API_KEY}&units=metric"
    
    # API 서버로 요청을 보내고 응답 데이터를 받음
    with urllib.request.urlopen(url) as r:
        # 받은 데이터를 JSON 형식으로 변환
        data = json.loads(r.read())
        
        # JSON 데이터에서 온도와 습도 값 추출
        temp = data["main"]["temp"]        # 현재 온도 (섭씨)
        humi = data["main"]["humidity"]   # 현재 습도 (%)
        
        # GUI 라벨(Label)에 온도와 습도 값을 표시
        label.config(text=f"{temp:.1f}C {humi}%")
    
    # 60,000ms = 60초 = 1분 후에 이 함수를 다시 실행 (자동 갱신)
    window.after(60000, tick1Min)


# -------------------------------
# GUI(화면) 설정
# -------------------------------

window = tkinter.Tk()                    # GUI 창 생성
window.title("TEMP HUMI DISPLAY")        # 창 제목 설정
window.geometry("400x100")               # 창 크기 설정 (가로 x 세로)
window.resizable(False, False)           # 창 크기 조절 비활성화

# 폰트 크기 설정 (가독성 향상)
font = tkinter.font.Font(size=30)

# 텍스트를 표시할 Label 위젯 생성
label = tkinter.Label(window, text="", font=font)
label.pack()  # GUI 창에 배치


# -------------------------------
# 프로그램 실행
# -------------------------------

tick1Min()        # 프로그램 시작 시 최초로 데이터 호출
window.mainloop() # GUI 창을 계속 유지 (이벤트 루프)
