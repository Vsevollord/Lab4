# Лабораторная работа 4 (Подсчёт слов в тексте)
## Прудкин Всеволод ИДБ-25-02


### Описание задачи

Необходимо реализовать программу, которая анализирует текст и считает, сколько раз встречается каждое слово.

Например, для строки:

`"cat dog cat bird dog cat"`

результат может быть таким:

- `cat -> 3`
- `dog -> 2`
- `bird -> 1`

Это одна из самых классических задач на использование словаря.

### Обязательная часть

Реализовать:

- чтение строки или текста
- разбиение текста на слова
- подсчёт количества повторений каждого слова
- вывод результата в формате `слово -> количество`

### Вариативная часть

1. Игнорировать регистр букв (задание из таблицы распределения)
2. Убирать знаки препинания перед подсчётом
3. Находить самое частое слово
4. Выводить только слова, которые встретились больше одного раза
5. Подсчитывать количество уникальных слов
6. Исключать из подсчёта служебные слова, например: `и`, `в`, `на`, `the`, `a`
---

## 1.Функция подсчета слов
Дополнительный параметр `exclude_stopwords` отвечает за подсчет служебных слов(0 - не считаются, 1 - считаются)
```python
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
```
## 2.Функция вывода подсчитанных слов
Дополнительный параметр `more_than_one` отвечает за вывод слов которые встречаются только один раз (0 - выводятся все слова, 1 - выводятся только слова которые встречаются больше одного раза)
```python
def print_dict(word_count, more_than_one=0):

    for key, value in word_count.items():
        if more_than_one:
            if value > 1:
                print(f'{key} -> {value}')
        else:
            print(f'{key} -> {value}')
```
## 3.Функция для нахождения самого частого слова в тексте
```python
def find_most_often(word_count):
    cnt = 0
    mx = ""
    for key, value in word_count.items():
        if value > cnt:
            cnt = value
            mx = key
    return mx, cnt
```
## 4.Функция подсчета уникальных слов
```python
def count_unique(word_count):
    cnt = 0
    for key, value in word_count.items():
        if value == 1:
            cnt+=1
    return cnt
```
## Проверка работы

```python
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
```
### Вывод в консоль 1
(`text2`,`exclude_stopwords = 1`,`more_than_one = 1`):
```
old -> 2
clock -> 2
on -> 2
wall -> 2
was -> 3
in -> 2
mouse -> 6
and -> 4
of -> 2
table -> 2
piece -> 2
cheese -> 3
but -> 2
for -> 2
cat -> 4
hole -> 2
tick -> 4
Most often word is: mouse -> 6
Amount of unique words: 62

Process finished with exit code 0
```
### Вывод в консоль 2
(`text1`,`exclude_stopwords = 0`,`more_than_one = 0`):
```
the -> 4
a -> 9
cat -> 3
and -> 1
dog -> 4
bird -> 2
ran -> 1
into -> 1
house -> 1
flew -> 1
in -> 1
sky -> 1
Most often word is: a -> 9
Amount of unique words: 7

Process finished with exit code 0
```