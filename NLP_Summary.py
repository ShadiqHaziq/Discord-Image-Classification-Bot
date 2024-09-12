# %pip install wordcloud(optionally)
# %pip install PySastrawi #Indonesian (optionally)
# %pip install nltk
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
# from wordcloud import WordCloud
# from matplotlib import pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
# ringkasan dalam satu kata
def summariztion(text, sent_number=1):
    # sentences = sent_tokenize(text, language='english')
    sentences = word_tokenize(text)#consider with ENG
    stop_words = set(stopwords.words('indonesian'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    freq_dist = FreqDist(words)
    sentence_scores = {}

    for i, sentence in enumerate(sentences):
        sentence_words = word_tokenize(sentence.lower())
        sentence_score = sum([freq_dist[word] for word in sentence_words if word in freq_dist])
        sentence_scores[i] = sentence_score

    sorted_scores = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_sentences = sorted_scores[:sent_number]
    selected_sentences = sorted(selected_sentences)
    summary = ' '.join([sentences[i] for i, _ in selected_sentences])
    return summary