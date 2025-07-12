from flask import Flask, render_template, request

app = Flask(__name__)

BUTTONS = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

@app.route("/", methods=["GET", "POST"])
def calculator():
    expression = ""
    if request.method == "POST":
        current = request.form.get("expression", "")
        btn = request.form.get("btn")

        if btn == "C":
            expression = ""
        elif btn == "=":
            try:
                expression = str(eval(current))
            except:
                expression = "Error"
        else:
            expression = current + btn

    return render_template("index.html", expression=expression, buttons=BUTTONS)

if __name__ == "__main__":
    app.run(debug=True)
