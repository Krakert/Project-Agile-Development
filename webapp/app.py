from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Malik bohr',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'May 29, 2020'
    },
    {
        'author': 'Albert Einstein',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'May 30, 2020'
    }
]


# routes aangemaakt zodat er genavigeerd kan worden!
@app.route('/')
@app.route('/home')
@app.route('/Home')
def hello_world():
    return render_template('home.html', posts=posts)


@app.route('/Sudoku')
@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html', title='Sudoku')


# debug = True houdt de server running!
if __name__ == '__main__':
    app.run(debug=True)
