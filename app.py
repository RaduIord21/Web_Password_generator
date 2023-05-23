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
def main():
    if request.method == "POST":

        error = ""
        final_list = []
        form_data = request.form
        for each in ["Min_letters", "Max_letters", "Min_numbers", "Max_numbers", "Min_special", "Max_special",
                     "Password_length"]:
            if not form_data[each]:
                return render_template("index.html", result="All fields must have values")
        min_letters = int(form_data["Min_letters"])
        max_letters = int(form_data["Max_letters"])
        min_numbers = int(form_data["Min_numbers"])
        max_numbers = int(form_data["Max_numbers"])
        min_specials = int(form_data["Min_special"])
        max_specials = int(form_data["Max_special"])
        password_length = int(form_data["Password_length"])

        sum_minims = min_specials + min_numbers + min_letters
        sum_max = max_specials + max_numbers + max_letters
        if not (sum_minims < password_length < sum_max):
            error = "Invalid password length !!!"
        if min_letters > max_letters or min_numbers > max_numbers or min_specials > max_specials:
            error = "Invalid limits !!!"
        if error:
            return render_template("index.html", result=error)

        for i in range(50):
            result = ""
            password = []
            for each in range(min_letters):
                sleep(0.01)
                password.append(letters[lfsr() % no_letters])
            for each in range(min_numbers):
                sleep(0.01)
                password.append(numbers[lfsr() % no_numbers])
            for each in range(min_specials):
                sleep(0.01)
                password.append(special_characters[lfsr() % no_special_characters])
            temp_len = len(password)
            for each in range(password_length - temp_len):
                sleep(0.01)
                password.append(all_chars[lfsr() % len(all_chars)])
            shuffle(password)
            for each in password:
                result += each
            final_list.append(result)
        return render_template("response.html", result=final_list)
    return render_template("index.html")


if __name__ == '__main__':
    # app.run()
    from flup.server.fcgi import WSGIServer
    #WSGIServer(app, bindAddress='/tmp/passwordgenerator-fcgi.sock').run()
    WSGIServer(app, bindAddress=('localhost', 8009)).run()
