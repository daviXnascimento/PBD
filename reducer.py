from operator import itemgetter
import sys
import math

current_word = None
current_count = 0
word = None
different_words_counter = 0
most_frequent_words_main = {}
most_frequent_words_aux = {}

for line in sys.stdin:
    
    line = line.strip()
    line = line.lower()

    # parse the input we got from mapper
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            different_words_counter += 1
            most_frequent_words_main[str(current_word)] = current_count
            most_frequent_words_aux[str(current_word)] = current_count
        current_count = count
        current_word = word

# last word
if current_word == word:
    different_words_counter += 1
    most_frequent_words_main[str(current_word)] = current_count
    most_frequent_words_aux[str(current_word)] = current_count

print("Questão 1) O número de palavras distintas é:", different_words_counter)

print("Questão 2) As palavras que mais se repetem são:")
most_frequent_words_range = range(0, 10)
for _ in most_frequent_words_range:
    max_key = max(most_frequent_words_aux, key=most_frequent_words_aux.get)
    print(max_key)
    del most_frequent_words_aux[max_key]

print("Questão 3) Histograma (intervalo - quantidade):")
# Pegando o valor de maior e menor frequência
key_max = max(most_frequent_words_main, key=most_frequent_words_main.get)
key_min = min(most_frequent_words_main, key=most_frequent_words_main.get) 
if most_frequent_words_main[key_max] < 10:
    print("Não é possível formar o histograma com 10 classes.")
else:
    # Definindo as classes
    histogram = {}
    last_interval_value = 1
    k = 10
    interval = most_frequent_words_main[key_max] - most_frequent_words_main[key_min]
    interval = math.floor(interval / k)
    aux = interval
    for _ in range(0, 10):
        count = 0
        for word in most_frequent_words_main:
            if last_interval_value < most_frequent_words_main[word] <= aux:
                count += 1
                histogram[str(aux)] = count

        last_interval_value = interval  
        aux += interval

last = 0              
for x in histogram:
    print(int(last) + 1, "a", int(x) + 1, " - ", histogram[x])
    last = x
