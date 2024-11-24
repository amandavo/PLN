import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import string
nltk.download('stopwords')
from nltk.corpus import stopwords

documents = [
    "Este produto é maravilhoso! A bateria dura muito e o desempenho é excelente.", #0
    "Não gostei do desempenho. A bateria descarrega rápido e o suporte não responde.", #1
    "Produto ok, mas a bateria poderia ser melhor. O preço é justo pelo que oferece.", #2
    "A qualidade do material é ótima, mas a bateria não tem boa duração.", #3
    "Muito bom! Recomendo, a bateria dura o dia todo e o desempenho é ótimo!" #4
]

def preprocess(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    return ' '.join(words)
processed_documents = [preprocess(doc) for doc in documents]

stop_words_pt = stopwords.words('portuguese')
vectorizer = TfidfVectorizer(stop_words=stop_words_pt)
X = vectorizer.fit_transform(processed_documents)

lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda.fit(X)

n_words = 5
words = vectorizer.get_feature_names_out()

for topic_idx, topic in enumerate(lda.components_):
    print(f"Palavras do tópico #{topic_idx}:")
    print([words[i] for i in topic.argsort()[:-n_words - 1:-1]])
    print()

topic_distributions = lda.transform(X)
topic_df = pd.DataFrame(topic_distributions, columns=[f'Topic {i}' for i in range(lda.n_components)])
print(topic_df)