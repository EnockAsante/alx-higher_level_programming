#!/usr/bin/python3
import marshal

if __name__ == "__main__":
    with open("/home/gadget/Downloads/hidden_4.pyc", 'rb') as f:
        code_obj = marshal.load(f)
        print(code_obj)
