def count_words(txt, exclude_stopwords=0):
    txt = txt.lower()
    punct_marks = [",",".",";",":","!","?","'","-"]
    for i in punct_marks:
        txt = txt.replace(i, " ")
    txt = txt.split()
    if exclude_stopwords:
        txt = [word for word in txt if word not in stopwords]
    word_count = {}
    for word in txt:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count

def print_dict(word_count, more_than_one=0):
    for key, value in word_count.items():
        if more_than_one:
            if value > 1:
                print(f'{key} -> {value}')

def find_most_often(word_count):
    cnt = 0
    mx = ""
    for key, value in word_count.items():
        if value > cnt:
            cnt = value
            mx = key
    return mx, cnt

def count_unique(word_count):
    cnt = 0
    for key, value in word_count.items():
        if value == 1:
            cnt+=1
    return cnt


if __name__ == "__main__":
    text1 = "The a cat and a dog the bird a dog cat a ran into the a dog house. A bird a flew dog in a the a cat sky."
    text2 = ("The old clock on the wall struck midnight. No one was awake in the house except a small "
             " grey mouse. The mouse quickly ran across the kitchen floor, stopped near the bread bin,"
             " and looked around. Nothing moved. Slowly, carefully, the mouse climbed up the leg of"
             " the wooden table. On the table lay a piece of cheese — not a big piece, but enough for"
             " a hungry mouse. Just as the mouse reached the cheese, the cat suddenly jumped from the"
             " dark corner. The cat was fast, but the mouse was faster. It grabbed the cheese and "
             "disappeared into a tiny hole in the wall. The cat sat there for a minute, stared at the"
             " hole, and then walked away. Maybe tomorrow, thought the cat. And the old clock continued"
             " ticking: tick, tick, tick, tick.")
    stopwords = ["и", "в", "на", "the", "a"]
    word_count = count_words(text2, 1)
    m_key, m_value = find_most_often(word_count)
    unique = count_unique(word_count)
    print_dict(word_count, 1)
    print(f"Most often word is: {m_key} -> {m_value}")
    print(f"Amount of unique words: {unique}")
