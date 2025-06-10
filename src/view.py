#sample to test jenkins integration3
from flask import Flask, render_template
import os

view = Flask(__name__)


@view.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 90))
    view.run(debug=True, host='0.0.0.0', port=port)
