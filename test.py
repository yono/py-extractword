#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from extractword import *


class TestWord(unittest.TestCase):

    def setUp(self):
        self.words = []
        self.words.append(Word(u'第', u'接頭詞,数接続,*,*,*,*,第,ダイ,ダイ'))
        self.words.append(Word(u'二', u'名詞,数,*,*,*,*,二,ニ,ニ'))
        self.words.append(Word(u'次', u'名詞,接尾,助数詞,*,*,*,次,ジ,ジ'))
        self.words.append(Word(u'が', u'助詞,格助詞,一般,*,*,*,が,ガ,ガ'))
        pass

    def test_is_prefix(self):
        self.assert_(self.words[0].is_prefix())
        self.assert_(not self.words[1].is_prefix())
        self.assert_(not self.words[2].is_prefix())
        self.assert_(not self.words[3].is_prefix())

    def test_is_postfix(self):
        self.assert_(not self.words[0].is_postfix())
        self.assert_(not self.words[1].is_postfix())
        self.assert_(self.words[2].is_postfix())
        self.assert_(not self.words[3].is_postfix())

    def test_pp_particle(self):
        self.assert_(not self.words[0].is_pp_particle())
        self.assert_(not self.words[1].is_pp_particle())
        self.assert_(not self.words[2].is_pp_particle())
        self.assert_(self.words[3].is_pp_particle())


class TestSentence(unittest.TestCase):

    def setUp(self):
        self.text = u'第二次世界大戦'
        self.sentence = Sentence()
        self.sentence.analysis_text(self.text)

    def test_analysis_text(self):
        words = [
            Word(u'第', u'接頭詞,数接続,*,*,*,*,第,ダイ,ダイ', False),
            Word(u'二', u'名詞,数,*,*,*,*,二,ニ,ニ', True),
            Word(u'次', u'名詞,接尾,助数詞,*,*,*,次,ジ,ジ', True),
            Word(u'世界', u'名詞,一般,*,*,*,*,世界,セカイ,セカイ', False),
            Word(u'大戦', u'名詞,一般,*,*,*,*,大戦,タイセン,タイセン', False),
        ]
        for i in xrange(len(words)):
            self.assertEqual(self.sentence.words[i].surface, words[i].surface)
            self.assertEqual(self.sentence.words[i].feature, words[i].feature)
            self.assertEqual(self.sentence.words[i].connect, words[i].connect)

    def test_get_words(self):
        words = [
            u'第二次',
            u'世界',
            u'大戦',
        ]
        result = self.sentence.get_words()
        for i in xrange(len(words)):
            self.assertEqual(result[i], words[i])

if __name__ == '__main__':
    unittest.main()
