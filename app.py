from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    your_name = "Kyame Israel"
    return render_template('index.html', name=your_name)


if __name__ == "__main__":
    app.run(debug=True)