#!/usr/bin/env python
# coding: utf-8
f = open('/home/xenakrll/Documents/other/tetrix-test/names.txt', 'r')
lines = f.read().split('"')
names = list(filter(lambda a: (a != ',')&(a != ''), lines))
names.sort()

score_sum = 0
for i in range(len(names)):
    score = 0
    word = names[i]
    for j in range(len(word)):
        score += (ord(word[j]) - ord('A') + 1)
    score_sum += score * (i+1)
print(score_sum)
