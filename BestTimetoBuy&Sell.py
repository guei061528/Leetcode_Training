# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
# 尖峰法
day_p = [7,6,4,3,1]
high = []
tmp = day_p[0]
for i in day_p:
    if tmp >= i:
        tmp = i
    else:
        high.append(i-tmp)
        tmp = i

print(sum(high))


