# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Hata ayıklama modunu (debug=True) açarak hızlı geliştirme sağlarız
    app.run(debug=True)
