#!/usr/local/python/bin/python
# coding=utf-8

from optparse import OptionParser
import sys
import os


def opt():
    parser = OptionParser()
    parser.add_option("-l", "--line",
                      dest="lines",
                      action="store_true",
                      default=False,
                      help="only count lines")
    parser.add_option("-w", "--word",
                      dest="words",
                      action="store_true",
                      default=False,
                      help="only count words")
    parser.add_option("-c", "--char",
                      dest="chars",
                      action="store_true",
                      default=False,
                      help="only count chars")
    parser.add_option("-n", "--nototal",
                      dest="nototal",
                      action="store_true",
                      default=False,
                      help="Not count total data")
    options, args = parser.parse_args()
    #    assert isinstance(args, object)
    return options, args


def get_count(data):
    chars = len(data)
    words = len(data.split())
    lines = data.count('\n')
    return lines, words, chars


def print_reselt(options, lines, words, chars, fn):
    if options.lines:
        print(lines),
    if options.words:
        print(words),
    if options.chars:
        print(chars),
    print(fn)


def main():
    options, args = opt()
    if not options.chars and not options.words and not options.lines:
        options.lines, options.words, options.chars, options.ntotal = True, True, True, True
    if args:
        total_lines, total_words, total_chars = 0, 0, 0
        for fn in args:
            if os.path.isfile(fn):
                with open(fn) as fd:
                    data = fd.read()
                lines, words, chars = get_count(data)
                total_lines += lines
                total_words += words
                total_chars += chars
                print_reselt(options, lines, words, chars, fn)
            elif os.path.isdir(fn):
                print("%s: is a directory" % fn)
            else:
                print("%s: No such file or directory" % fn)
        if (len(args) > 1) and not options.ntotal:
            print_reselt(options, total_lines, total_words, total_chars, "total")
    else:
        data = sys.stdin.read()
        fn = ''
        lines, words, chars = get_count(data)
        print_reselt(options, lines, words, chars, fn)

if __name__ == '__main__':
    main()
