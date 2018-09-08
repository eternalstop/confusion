#!/usr/bin/env python
# encoding: utf-8


class Solution(object):

    HOUR_DICT = {0: [0], 1: [1, 2, 4, 8], 2: [3, 5, 6, 9, 10], 3: [7, 11]}
    MINITE_DICT = {
        0: [0],
        1: [1, 2, 4, 8, 16, 32],
        2: [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48],
        3: [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44, 49,
            50, 52, 56],
        4: [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58],
        5: [31, 47, 55, 59]
    }

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        results = []
        for hour_led_num in range(0, num + 1):
            if hour_led_num >= 4:
                break
            minite_led_num = num - hour_led_num
            if minite_led_num >= 6:
                continue
            for hour in self.HOUR_DICT[hour_led_num]:
                for minite in self.MINITE_DICT[minite_led_num]:
                    results.append('{hour}:{minite:02d}'.format(hour=hour, minite=minite))
        return results
