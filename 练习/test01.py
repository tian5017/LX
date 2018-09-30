import pandas as pd
from collections import Counter


df = pd.read_csv("123.txt", sep="\n")
words = list(df["ABCDE"].values)
new_words = []
for w in words:
    if isinstance(w, str):
        w = w.replace(" ", "")
        w1 = w.split("=>")
        # w2 = w1[1].replace(" ", "")
        # w3 = w2.split(",")
        # w4 = w3[0]
        # w5 = w4 + " => " + w2
        new_words.append(w1[0])

print(Counter(new_words))

# new_df = pd.DataFrame()
# new_df["ABCDE"] = new_words
# new_df.to_csv("123_new.txt", sep="\n", index=False)
