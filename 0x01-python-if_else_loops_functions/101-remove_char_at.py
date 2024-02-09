#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = str
    if 0 <= n <= len(cpy):
        return cpy[:n] + cpy[n+1:]
    else:
        return str