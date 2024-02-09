#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", 'rb') as f:
        code_obj = marshal.load(f)
        print(code_obj)
    names = [name for name in dir(code_obj) if not name.startswith('__')]
    names.sort()

    for name in names:
        print(name)