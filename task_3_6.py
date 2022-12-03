# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(*args):
    slovo = input("Введите слово прописными буквами (только латинские символы): ")
    import re
    if re.search(r'[^a-z]', slovo):
        print("Ввод не корректен! Внимательно читайте задание!")
        return
    print(slovo.title())
    return


int_func()
