#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i > j or i == j:
            continue
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
            break
        print("{:d}{:d}".format(i, j),end=", ")
