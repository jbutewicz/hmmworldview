import os
from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_pyfile('instance/config.py')

@app.route('/', methods=['GET', 'POST'])
def index():

    # Get keywords and send to index.html
    keywords = []
    file = open(app.root_path + '/keywords.txt', 'r')
    for line in file.readlines():
        keywords.append(line.split()[0])

    file.close()

    return render_template('index.html', title='Home', keywords=keywords)

if __name__ == "__main__":
    app.run()
