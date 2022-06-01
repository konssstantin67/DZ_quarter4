import random

def get_jokes (n):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    a = random.sample(nouns,1)
    b = random.sample(adverbs,1)
    c = random.sample(adjectives,1)
    new_list = list([a, b, c])
    print(new_list)

get_jokes (3)
