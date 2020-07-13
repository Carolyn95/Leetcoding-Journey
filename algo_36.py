pairs = [['u1', 'u2'], ['u3', 'u4'], ['u1', 'u3'], ['u4', 'u5']]
used_vouchers = [{'u1': ['v1']}, {'u2': ['v1', 'v2']}, {'u3': []}, {'u4': []}]

import pdb


group = set(pair) intersect with elements in groups -> false -> groups.append(group)
-> true -> union elements in groups, repeat the procedure


   


pdb.set_trace()
found_similar_users(pairs)
pdb.set_trace()

# def can_use_voucher(userid, voucherid):
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