if __name__ == '__main__':
    material = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " + \
               "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    positions = (1, 5, 6, 7, 8, 9, 15, 16, 19)
    positions = [x - 1 for x in positions]

    p = 0
    ans = {}
    words = material.split(' ')
    for i, word in enumerate(words):
        if i in positions:
            ans[word[:1]] = p + 1
        else:
            ans[word[:2]] = p + 1
        p += len(word) + 1

    print(dict(ans))
