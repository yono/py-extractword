#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import MeCab


class Word(object):

    def __init__(self, surface, feature, connect=False):
        self.surface = surface
        self.feature = feature
        self.connect = connect

    def is_prefix(self):
        return self.feature.startswith(u'接頭詞')

    def is_postfix(self):
        return self.feature.split(',')[1] == u'接尾'

    def is_pp_particle(self):
        return self.feature.startswith(u'助詞')


class Sentence(object):

    def __init__(self):
        self.words = []
        self.mecab = MeCab.Tagger()

    def get_words(self):
        result = []
        BEFORE = -1
        for word in self.words:
            if word.connect == True:
                result[BEFORE] = result[BEFORE] + word.surface
            else:
                result.append(word.surface)
        return result

    def analysis_text(self, text):
        words = self.words
        CURRENT = -1
        BEFORE = -2
        res = self.mecab.parseToNode(text.encode("utf-8"))
        while res:
            if res.surface == '':
                res = res.next
                continue

            words.append(Word(unicode(res.surface), unicode(res.feature)))

            if len(words) > 1:
                rules = []
                rules.append(words[BEFORE].is_prefix())
                rules.append(words[CURRENT].is_postfix())
                rules.append(words[BEFORE].is_pp_particle() and \
                             words[CURRENT].is_pp_particle())

                for rule in rules:
                    if rule:
                        self.words[CURRENT].connect = True

            res = res.next

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    sentence = Sentence()
    sentence.analysis_text(text)
    words = sentence.get_words()
    for word in words:
        print word
