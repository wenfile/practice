

def open_file():
    with open('../static/book.json', 'r', encoding='utf-8') as f:
        rest = f.read()
        print(rest)


if __name__ == '__main__':
    open_file()