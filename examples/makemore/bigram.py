#!/usr/bin/env python
# coding: utf-8

words = open('names.txt', 'r').read().splitlines()

print(words[:10])
print(len(words))

print(max([len(x) for x in words]))
print(min([len(x) for x in words]))

b = {}
for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        biagram = (ch1, ch2)
        b[biagram] = b.get(biagram,0) + 1
        # print(ch1, ch2)


print(sorted(b.items(), key=lambda kv: -kv[1]))

import torch
N = torch.zeros(28, 28, dtype=torch.int32)

chars = sorted(list(set(''.join(words))))
stoi = {s:i for i, s in enumerate(chars)}
stoi['<S>'] = 26
stoi['<E>'] = 27

for w in words:
    chs = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chs, chs[1:]):
        ix1 = stoi[ch1]
        ix2 = stoi[ch2]
        N[ix1, ix2] += 1

import matplotlib.pyplot as plt
plt.imshow(N)
