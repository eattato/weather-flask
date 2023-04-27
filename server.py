import numpy as np
from flask import Flask, request, jsonify
from keras.models import load_model

# 모델 로드
model = load_model("C:/users/user/desktop/weather-flask/weather.h5")

# 서버 생성
app = Flask(__name__)

# 요청 처리
@app.route("/predict", methods=["POST"])
def predict():
    if request.is_json:
        locationCodes = {
               '강원도': 0, '경기도': 1, '인천광역시': 11, '서울특별시': 8, '경상북도': 3, '충청북도': 16, '충청남도': 15, '대전광역시': 6, '전라북도': 13, '대구광역시': 5, '울산광역시': 10, '경상남도': 2, '광주광역시': 4, '부산광역시': 7, '전라남도': 12, '제주도': 14, '세종특별자치시': 9
               }
        data = request.get_json()

        if data["location"] in locationCodes:
            loc = locationCodes[data["location"]]
            test_x = [loc, data["month"], data["temperature"], data["humidity"]]
            test_x = np.array([test_x])
            res = model.predict(test_x)

            res = {
                "rain": str(res[0][0]),
                "snow": str(res[0][1])
            }
            print(res)
            return jsonify(res)
    return "prediction"

# 메인
if __name__ == "__main__":
    print("서버 열림")
    app.run(port=8889)