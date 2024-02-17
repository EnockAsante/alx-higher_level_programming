#!/usr/bin/python3
def multiple_returns(sentence):
    turple_str = ()
    if sentence:
        turple_str += (len(sentence), sentence[0],)
    else:
        turple_str += (0, )
    return turple_str
