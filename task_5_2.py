# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк
# и слов в каждой строке.

import sys

FILENAME = "text_1.txt"

if __name__ == "__main__":
    try:
        with open(FILENAME, encoding="utf-8") as out_f:
            lines = [line for line in out_f.readlines() if line != "\n"]
    except IOError as e:
        print(e)
        sys.exit(1)

    print(f"В файле содержится {len(lines)} строк(и).")

    for line in lines:
        print(f"Строка ({line[:50]}) содержит {len(line.split())} слов(а)")