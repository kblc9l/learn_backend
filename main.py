from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_page():
    with open('templates/site_about_firefox.html', encoding='utf8') as f:
        return f.read()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)


# dfkpsjfsdf

