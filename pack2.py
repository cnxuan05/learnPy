# coding:utf-8
def get_data(num, data):
    return data[num]
    pass


def get_treat(a, b, data):
    rank_a = 100
    rank_b = -1
    for i in range(len(data)):

        if data[i] == a:
            rank_a = i
        if data[i] == b:
            rank_b = i
        if rank_b > rank_a:
            break

    if rank_b - rank_a == 1:
        return u'食傷'
    elif rank_b - rank_a == 2:
        return u'才财'
    elif rank_b - rank_a == 3:
        return u'官杀'
    elif rank_b - rank_a == 4:
        return u'印'
    elif rank_b - rank_a == 5:
        return u'比劫'
