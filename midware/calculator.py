from flask import Flask, request
from flask.templating import render_template

a = ""


def process_input():
    global a
    a = ""

    msg = request.form.get("msg")
    msg = str(msg)
    if msg.isalpha():
        a = "输入算式不合法"
    else:
        a = msg + " = " + str(eval(msg))


def process_output():
    return a


app = Flask(__name__)


@app.route("/calc.php", methods=["POST", "GET"])
def user():
    process_input()
    output = process_output()
    return render_template("echo.jinja2", bean=output)


# Run
if __name__ == "__main__":
    app.run(debug=True)
