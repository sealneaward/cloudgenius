from flask import Flask, render_template,jsonify, url_for, request
import scrape,analysis

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
static_location = '127.0.0.1:5000/static'


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/analyze', methods=['POST'])
def analyze():
    url=request.form['url']
    text = scrape.scrape(url)
    # get end of url for naming pics
    i = url.rfind('/') + 1
    url = url[i:]
    polarity_url = analysis.get_sentiment_analysis(text, url)
    wordmap_url = analysis.get_wordmap(text, url)

    return render_template("analysis.html", polarity=polarity_url, wordmap=wordmap_url)

if __name__ == '__main__':
    app.run()
