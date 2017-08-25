def n_gram(seq, n=2):
    ans = [seq[x:x+n] for x in range(len(seq))]
    return ans

if __name__ == '__main__':
    print(n_gram("I am an NLPer".split(" ")))
    print(n_gram("I am an NLPer"))
