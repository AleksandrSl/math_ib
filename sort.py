from functools import partial

def merge(l1, l2, order):
    # print('l1, l2 is: {}, {}'.format(l1, l2))
    new_l = []

    if order == 'increase':     # не хорошо конечно, что это каждый раз вызывается
        comp_func = int.__gt__  # и вообще в идеале независящим от типа надо делать
    elif order == 'decrease':
        comp_func = int.__lt__

    while l1 and l2:
        if comp_func(l1[0], l2[0]):
            new_l.append(l2.pop(0))
        else:
            new_l.append(l1.pop(0))

    if l1:
        new_l.extend(l1)
    elif l2:
        new_l.extend(l2)
    return new_l


# import pdb
def merge_sort(l, order='increase'):
    # pdb.set_trace()
    if len(l) == 1 or len(l) == 0:
        return l
    m = len(l)//2
    # merge_sort_with_order = partial(merge_sort, order=order)
    return merge(merge_sort(l[:m], order), merge_sort(l[m:], order), order)


def min_with_pos(l):
    min = l[0]
    ind = 0
    for i, el in enumerate(l):
        if el < min:
            min = el
            ind = i
    return min, ind


def choice_sort(l):
    new_l = []
    while l:
        _, ind = min_with_pos(l)
        new_l.append(l.pop(ind))
    return new_l


def boyer_moore_majority(l):
    maj = None
    count = 1
    for el in l:
        if el == maj:
            count += 1
        else:
            count -= 1
            if count == 0:
                count = 1
                maj = el
    return maj if l.count(maj) > len(l) / 2 else None


# def choice_sort_v2(l):
#     new_l = []
#     for _ in range(len(l)):
#         min_, ind = min_with_pos(l)
#         print(min_, ind)
#         new_l.append(min_)
#         l[:ind].extend(l[ind+1:])
#         print(l)
#     return new_l