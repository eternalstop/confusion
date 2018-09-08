#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        prepare_list = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'},
        ]
        results = []
        for word in words:
            if (all(w in prepare_list[0] for w in word.lower())
                or all(w in prepare_list[1] for w in word.lower())
                    or all(w in prepare_list[2] for w in word.lower())):
                results.append(word)
        return results
