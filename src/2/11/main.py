if __name__ == '__main__':
    with open('../hightemp.txt', 'r', encoding='utf_8') as f:
        text = f.read()
    print(text.replace("\t", " "))