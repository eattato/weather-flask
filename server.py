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
    print("요청 받음")
    print(request.get_data())
    if request.is_json:
        data = request.get_json()
        test_x = [data["locationCode"], data["month"], data["temperature"], data["humidity"]]
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