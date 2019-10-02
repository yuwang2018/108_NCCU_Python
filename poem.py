# coding: utf-8
from numpy.random import randint
from numpy.random import sample,choice
words='''
我
我的
妳
妳的
女孩
男孩
呼吸
輕輕
時光
癡
嗔
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止'''
phrase = words.split('\n')
#3-7句
n = randint(3,8)

for i in range(n):
    #2-4個字
    k = randint(2,5)
    egg = choice(phrase, k)
    ham = ' '.join(egg)
    print(ham)
