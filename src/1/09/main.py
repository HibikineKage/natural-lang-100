from random import shuffle


def typoglycemia(text):
    words = text.split(' ')

    def shuffler(word):
        if len(word) > 4:
            middle = [x for x in word[1:-1]]
            shuffle(middle)
            return word[0] + ''.join(middle) + word[-1]
        return word

    randomized_words = [shuffler(w) for w in words]
    return ' '.join(randomized_words)

if __name__ == '__main__':
    text = "I couldn't believe that I could actually understand what I was reading : " + \
           "the phenomenal power of the human mind ."
    print(typoglycemia(text))
