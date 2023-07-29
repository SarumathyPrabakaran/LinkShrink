from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def shorten_url():
    if request.method=='POST':
        long_url = request.form['long_url']
        response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
        short = ''
        print(response,response.text)
        
        if response.status_code == 200:
            short = response.text
            
            return render_template('index.html',short=short)
            
        else:
            return jsonify({'error': 'Failed to shorten URL'}), 400

        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)