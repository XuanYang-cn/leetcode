# 135 candy 分发糖果

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


def candy(ratings):
    candys = [1 for _ in range(len(ratings))]

    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candys[i] = candys[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candys[i] <= candys[i + 1]:
            candys[i] = candys[i + 1] + 1
    return sum(candys)


case1 = [1, 2, 87, 87, 2, 1]
print(candy(case1))
