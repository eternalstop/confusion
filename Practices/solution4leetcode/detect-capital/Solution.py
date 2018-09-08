#!/usr/bin/env python
# encoding: utf-8


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        if word.lower() == word:
            return True
        if word[1:].lower() == word[1:]:
            return True
        return False
