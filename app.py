from flask import Flask
import random
import requests

app = Flask(__name__)

# Ссылки на файлы в Google Drive
escape_url = "https://drive.google.com/uc?export=download
&=id1p0Tig1NH-7-2VJjuYDzKhfzOCTLcOjBg"
battle_url = "https://drive.google.com/uc?export=download
&=id1wh0Q5VDV5STckT_Pa2bqZtAyhD3y5U3d"

def get_random_line(url):
    response = requests.get(url)
    lines = response.text.splitlines()
    return random.choice(lines)

@app.route('/escape')
def escape():
    return get_random_line(escape_url)

@app.route('/battle')
def battle():
    return get_random_line(battle_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    