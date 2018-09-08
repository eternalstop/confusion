#!/usr/bin/env python
# encoding: utf-8

import string


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_dict = {x: 0 for x in string.lowercase}
        magazine_dict = {x: 0 for x in string.lowercase}
        for x in ransomNote:
            ransom_dict[x] += 1
        for x in magazine:
            magazine_dict[x] += 1
        for x in string.lowercase:
            if ransom_dict[x] > magazine_dict[x]:
                return False
        return True
