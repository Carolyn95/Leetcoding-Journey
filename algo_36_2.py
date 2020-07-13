pairs = [['u1', 'u2'], ['u3', 'u4'], ['u1', 'u3'], ['u4', 'u5'], ['u6', 'u7'],
         ['u1', 'u8']]
result = []





def test(match, group):
    # print(group)
    flag = False
    for idx, item in enumerate(group):
        # & intersection
        if not (set(item) & set(match)):
            pass
        else:
            flag = True
            # | union
            group[idx] = set(item) | set(match)
    if flag == True:
        test(group.pop(), group)
    else:
        group.append(set(match))
    # return flag


for idx, pair in enumerate(pairs):
    test(pair, result)

print(result)