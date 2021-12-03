#-*- coding:utf-8 -*-

import numpy as np; np.random.seed(1234)
import pycld2 as cld2


class LanguageDetector(object):
    def __init__(self):
        pass

    def predict(self, inp):
        if len(inp) == 0:
            return "unknown"

        printable_text = "".join(x for x in inp if x.isprintable())
        isReliable, textBytesFound, details = cld2.detect(printable_text, isPlainText=True)

        if isReliable:
            return details[0][0].lower()
        elif details[0][0].lower() != "unknown":
            return details[0][0].lower()
        else:
            return "unknown"

