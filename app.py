from flask import Flask, render_template, request
from lfsr import lfsr, shuffle
from time import sleep


app = Flask(__name__)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '"', '#', '$', '%', '&', '\\', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                      '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
all_chars = letters + numbers + special_characters
no_letters = len(letters)
no_numbers = len(numbers)
no_special_characters = len(special_characters)

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
