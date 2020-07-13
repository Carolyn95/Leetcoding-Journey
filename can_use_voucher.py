# init
pairs = [['u1', 'u2'],['u3', 'u4'],['u5', 'u8']]
new = ['u1', 'u3']
new_pairs = []

# new pair
['u1', 'u2'] & new => ['u1', 'u2', 'u3']    ----|
                                                |                                 
['u3', 'u4'] & new => ['u1', 'u3', 'u4']    ----|----    new_pairs = [ (['u1', 'u2', 'u3']  | ['u1', 'u3', 'u4']) , ['u5', 'u8']]    
                                                |
['u5', 'u8'] & new => []                    ----|

得出公式
pairs = [ a1, a2, a3, .... , ai ]
new  = b 
new_pairs = [ (b1 | b2 | .... | bi), c1, c2, .... , ci ] # , ci代表的是
'''
bi 代表的是 (set(ai) & set(new)) != [] 有交集的
ci 代表的是 (set(ai) & set(new)) == [] 没有交集的
就是pairs所有与new有交集的，都可以组成一个有关联的用户集合
'''


'''
新增两个变量cache_result，intersection，
增加空间复杂度（内存的使用）减少了 时间复杂度 （不用递归程序执行的逻辑）
牺牲空间换取时间，参考之前跟你讨论过的 斐波那契数列 算法的优化（用map记住已经算过的数据，再次遇到就不用再递归啦） 也是牺牲空间换取时间
f(1) = 1
f(2) = 2
f(3) = f(1) + f(2)
f(4) = f(2) + f(3)
f(5) = f(3) + f(4) = f(3) + f(2) + f(3) =>注意  f(3)算了两次，会有其余的都多余的递归，依次类推随着数越来越大多余递归的次数就越大，所以可以把第一次算过的缓存下来，
'''
pairs = [['u1', 'u2'], ['u3', 'u4'], ['u1', 'u3'], ['u4', 'u5'],['u6', 'u7'],['u5', 'u8']]
result = []
for idx,num in enumerate(pairs):
    cache_result = []
    intersection = set(num)
    for idx,item in enumerate(result):
        # 求并集，为空即不符合
        if not (set(item) & set(num)):
            cache_result.append(item)
        else:
            intersection = set(item) | intersection
    cache_result.append(intersection)
    result = cache_result


