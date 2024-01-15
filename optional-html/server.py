from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('my_temp.html')


@app.route('/sale/')
def sale():
    return render_template('sale.html')


if __name__ == '__main__':
    app.run()