import pandas
from textblob import TextBlob
import matplotlib.pyplot as plt
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts


# funtion will analyze polarity (positive / negative) behind the passed verse and create a picture of the
def get_sentiment_analysis(text, url_name):
    blob = TextBlob(text)
    polarity = []
    sentences = []
    sentiment = pandas.DataFrame(columns=['SENTENCE', 'POLARITY'])
    for sentence in blob.sentences:
        polarity.append(sentence.sentiment.polarity)
        sentences.append(str(sentence.raw))
    sentiment['SENTENCE'] = sentences
    sentiment['POLARITY'] = polarity
    plt.figure()
    plt.plot(sentiment['POLARITY'])
    plt.xlabel('Sentence')
    plt.ylabel('Polarity')
    url_name = 'analysis_img/polarity/' + str(url_name)+'.png'
    plt.savefig('../web/static/'+url_name)
    return url_name


# function will create a word map for a blob of text
def get_wordmap(text, url_name):
    tags = make_tags(get_tag_counts(text), maxsize=120)
    url_name = 'analysis_img/wordmap/' + str(url_name)+'.png'
    create_tag_image(tags, '../web/static/'+url_name, size=(1300, 1100), fontname='Lobster')
    return url_name

