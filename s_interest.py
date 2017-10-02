#!/usr/bin/python

p = float(input('Principal Amount? '))
r = 12.5
t = int(input('Time Period? '))

si = (p * r * t) / 100

print("Simple interest of {}, {}, {} is {}".format(p, r, t, si))
