if __name__ == '__main__':
    with open('../hightemp.txt', 'r', encoding='utf_8') as f:
        lines = f.readlines()
    lines = [[x.split('\t')] for x in lines]
    with open('col1.txt', 'w', encoding='utf_8') as f:
        f.writelines([x[0][0] + '\n' for x in lines])

    with open('col2.txt', 'w', encoding='utf_8') as f:
        f.writelines([x[0][1] + '\n' for x in lines])
