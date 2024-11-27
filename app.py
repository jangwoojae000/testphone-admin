from flask import Flask, render_template, request

app = Flask(__name__)

# 대여 중인 테스트폰 리스트
rented_phones = []

@app.route("/", methods=["GET", "POST"])
def home():
    global rented_phones

    if request.method == "POST":
        # 대여하기 처리
        if "rent" in request.form:
            phone_number = request.form.get("phone_number")
            renter = request.form.get("renter")
            rental_date = request.form.get("rental_date")
            if phone_number and renter and rental_date:
                # 대여한 테스트폰 리스트에 추가
                rented_phones.append({"phone": phone_number, "renter": renter, "date": rental_date})
            return render_template("index.html", rented_phones=rented_phones)

        # 반납하기 처리
        elif "return" in request.form:
            phone_number_return = request.form.get("phone_number_return")
            if phone_number_return:
                # 반납할 테스트폰을 리스트에서 제거
                rented_phones = [phone for phone in rented_phones if phone["phone"] != phone_number_return]
            return render_template("index.html", rented_phones=rented_phones)

    # GET 요청시, 대여 중인 테스트폰 리스트를 보여줌
    return render_template("index.html", rented_phones=rented_phones)


if __name__ == "__main__":
    app.run(debug=True)
