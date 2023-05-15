from flask import Flask, redirect


app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("latest_link.txt", "r") as f:
        link = f.read()

    return redirect(link)


if __name__ == '__main__':
    app.run()
