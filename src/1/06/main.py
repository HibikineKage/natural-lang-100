import numpy as np

def n_gram(seq, n=2):
    ans = [seq[x:x+n] for x in range(len(seq))]
    return ans

if __name__ == '__main__':
    x = n_gram("paraparaparadise")
    y = n_gram("paragraph")

    X = np.unique(np.array(x))
    Y = np.unique(np.array(y))

    x_and_y = np.intersect1d(X, Y)
    x_or_y = np.setxor1d(X, Y)
    x_minus_y = np.setdiff1d(X, Y)

    print("X:{}".format(list(X)))
    print("Y:{}".format(list(Y)))
    print("X∩Y:{}".format(list(x_and_y)))
    print("X∪Y:{}".format(list(x_or_y)))
    print("X-Y:{}".format(list(x_minus_y)))
