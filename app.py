from flask import Flask, render_template, request, jsonify
from number_to_word import num_to_word

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = request.form['number']
        return jsonify({'result': num_to_word(number)})
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

