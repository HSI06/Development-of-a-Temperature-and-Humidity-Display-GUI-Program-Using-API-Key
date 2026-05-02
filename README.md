# Development-of-a-Temperature-and-Humidity-Display-GUI-Program-Using-API-Key
API Key 발급받아 온습도 표시 GUI 프로그램 만들기
Python과 OpenWeatherMap API를 활용하여
실시간 온도 및 습도 정보를 GUI로 출력하는 프로그램입니다.

Overview

본 프로젝트는 외부 날씨 API를 활용하여 데이터를 수집하고,
이를 Python GUI로 시각화하는 간단한 IoT 응용 프로그램입니다.

OpenWeatherMap API를 통한 실시간 데이터 수집
JSON 데이터 파싱
tkinter GUI 출력
1분 단위 자동 갱신
Tech Stack
Python 3.x
tkinter (GUI)
urllib (HTTP 요청)
json (데이터 처리)
OpenWeatherMap API
System Flow
OpenWeatherMap API
        ↓
   HTTP Request
        ↓
    JSON Data
        ↓
 Data Parsing
        ↓
 tkinter GUI
        ↓
 Temperature / Humidity Display
Features
실시간 날씨 데이터 조회
온도(°C) 출력
습도(%) 출력
1분마다 자동 갱신
간단한 GUI 인터페이스
Demo Video

Installation & Run
1. API Key 발급
https://openweathermap.org/
 접속 후 회원가입
API Key 생성
