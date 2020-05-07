from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


# routes aangemaakt zodat er genavigeerd kan worden!
@app.route('/')
@app.route('/home')
@app.route('/Home')
@app.route('/index')
@app.route('/Index')
def main():
    return render_template('index.html')


@app.route('/Sudoku')
@app.route('/sudoku')
def sudoku():
    return render_template('minigames_sudoku.html', title='Sudoku')


@app.route('/Rekenen')
@app.route('/rekenen')
def Rekenen():
    return render_template('minigames_rekenen.html', title='Rekenen')


@app.route('/Minigames')
@app.route('/minigames')
def minigames():
    return render_template('minigames.html', title='Minigames')


@app.route('/Beweeg')
@app.route('/beweeg')
def beweeg():
    return render_template('beweeg.html', title='Beweeg')


@app.route('/Ondersteuning')
@app.route('/ondersteuning')
def ondersteuning():
    return render_template('ondersteuning.html', title='Ondersteuning')


@app.route('/Bestel')
@app.route('/bestel')
def bestel():
    return render_template('bestel.html', title='Bestel')


# debug = True, keeps the server alive
if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
