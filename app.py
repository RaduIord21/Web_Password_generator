from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")


@app.route('/form', methods=["GET", "POST"])
def get_letters():
    if request.method == "POST":
        form_data = request.form
        print(form_data)
        return render_template("response.html", result=form_data)
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
