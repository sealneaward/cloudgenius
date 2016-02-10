import pandas
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@0.0.0.0:5432/lyrics')

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
    sentiment.to_sql('sentiment', engine, if_exists='append', index=False)
    plt.figure()
    plt.plot(sentiment['POLARITY'])
    plt.xlabel('Sentence')
    plt.ylabel('Polarity')
    url_name = 'analysis_img/polarity/' + str(url_name)+'.png'
    plt.savefig('static/'+url_name)
    return url_name


# function will create a word map for a blob of text
def get_wordmap(text, url_name):
    # Generate a word cloud image
    wordcloud = WordCloud(max_font_size=40, relative_scaling=.5).generate(text)
    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    url_name = 'analysis_img/wordmap/' + str(url_name)+'.png'
    plt.savefig('static/'+url_name)
    return url_name
