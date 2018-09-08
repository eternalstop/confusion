#!/usr/bin/env python
# encoding: utf-8

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.mmap = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.mmap:
            value = self.mmap[key]
            del self.mmap[key]
            self.mmap[key] = value
            return value
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.mmap:
            del self.mmap[key]
            self.mmap[key] = value
        else:
            self.mmap[key] = value
        if len(self.mmap) > self.capacity:
            self.mmap.popitem(last=False)

lru = LRUCache(2)

lru.set('1', 111)
lru.set('2', 222)
lru.set('3', 333)
print lru.get('1')
print lru.get('3')
lru.set('4', 444)
print lru.get('2')
