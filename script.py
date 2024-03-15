
import redis

import string

r = redis.Redis(host="localhost", port=6379, db=0)

with open("./gp.txt", "r") as f:
    data = f.read()


words = []
lines = data.split("\n")
for l in lines:    
    l = l.translate(str.maketrans('', '', string.punctuation))
    words = words + l.split(" ")

    
for w in words:   
    print(w)
    r.hincrby("words",w,1)

# Affichage du compte final
# print("Compte final des mots dans Redis:")
# final_counts = r.hgetall("words")
# for word, count in final_counts.items():
#     print(f"{word.decode('utf-8')}: {int(count)}")

# Récupération de toutes les clés (mots) stockées dans Redis
all_words = r.hkeys("words")

print("Compte final des mots dans Redis:")
for word in all_words:
    count = r.hget("words", word)
    print(f"{word.decode('utf-8')}: {int(count)}")