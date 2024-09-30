from collections import Counter
from nltk.metrics import edit_distance

corpus_text = ""

with open("biblia.txt", encoding="ISO-8859-1") as file:
    corpus_text += file.read() + "\n"

def process_text(text):
    words = ''.join(char.lower() if char.isalnum() or char.isspace() 
                    else ' ' for char in text).split()
    return words

corpus_process = process_text(corpus_text)
print(corpus_process[5000:5050])
word_counts = Counter(corpus_process)
corpus_final = dict(word_counts)

for word, count in list(corpus_final.items())[:5]:
    print(f"{word}: {count}")

def correct_word(word, corpus):
    if word in corpus:
        return word
    candidates = sorted(corpus.keys(), key=lambda w: (edit_distance(word, w), -corpus[w]))
    print(candidates[:5])
    return candidates[0] if candidates else word

def correct_phrases(phrase, corpus):
    words = phrase.lower().split(" ")
    corrected = [correct_word(word, corpus) for word in words]
    return " ".join(corrected)

def main():
    frase = input("Digite uma frase: ")
    frase_corrigida = correct_phrases(frase, corpus_final)

    if frase.lower() == frase_corrigida:
        print("A frase aparenta ser potencialmente CORRETA")
    else:
        print("------------------------------------------")
        print("A frase aparenta ser potencialmente ERRADA")
        print(f"Frase potencialmente corrigida: \n{frase_corrigida}")
        print("------------------------------------------")

if __name__ == "__main__":
    main()
