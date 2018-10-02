from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

PATH = "sample.txt"

with open(PATH, "r") as file:
    text = file.read()
    stopWords = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    words = [w for w in tokens if w not in stopWords]
    wordcloud = WordCloud(mode="RGBA", background_color=None, width=300, height=600).generate(" ".join(words))
    wordcloud.to_file("./wordcloud.png")
