import io

if __name__ == '__main__':
    with open('../hightemp.txt', 'r', encoding='utf_8') as f:
        length = len(f.readlines())
    print(length)