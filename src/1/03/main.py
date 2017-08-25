from functools import reduce
from operator import itemgetter

if __name__ == '__main__':
    poem = "Now I need a drink, alcoholic of course, " + \
        "after the heavy lectures involving quantum mechanics."
    words = poem.replace(',', '').split(' ')

    def counter(array, word):
        l = str(len(word))
        if not l in array:
            array[l] = 0
        array[l] += 1
        return array

    counts = reduce(counter, words, {})
    counts = sorted(counts.items(), key=lambda x: int(x[0]))
    print(dict(counts))