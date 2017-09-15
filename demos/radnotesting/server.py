from flask import Flask, render_template, request
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
app = Flask(__name__)

@app.route('/')
def main():
    logging.info('Hit Main')
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    logging.info('hit process')
    logging.debug(request.form['stuff'])
    context = {
        'stuff': request.form['stuff'],
    }
    return render_template('stuff.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)