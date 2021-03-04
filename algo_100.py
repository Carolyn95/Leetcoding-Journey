# 1. A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 2. 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 3. B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 4. 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼

{A: a, B: b, C: c, D: d, E: e}

total = 5 * a + 1
4 * a = 5 * b + 1
4 * b = 5 * c + 1
4 * c = 5 * d + 1
4 * d = 5 * e + 1 


(d1 - 1) % 5 == 0
d1 = 6  = 6 + 5 * 0
d1 = 11 = 6 + 5 * 1
d1 = 16 = 6 + 5 * 2
d1 = 21 = 6 + 5 * 3






# solution
fish = 6
while True:
    total = fish
    enough = True
    t = []
    for _ in range(5):
        t.append((total - 1) / 5)
        if (total - 1) % 5 == 0:
            total = (total - 1) / 5 * 4    
        else:
            enough = False
            break
    if enough:
        print(t)
        print(fish)
        break
    fish += 5
    
fish = 6
attempt = 1
while True:
    total = fish
    enough = True
    t = []
    for _ in range(5):
        t.append(total)
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        if attempt != 2:
            enough = False
            attempt +=1
        else:
            print(t)
            print(fish)
            break 
    fish += 5

 fish = 6
 while True:
     total = fish
     enough = True
     attempt = 1
     t = []
     for _ in range(5):
         t.append((total - 1) / 5)
         if (total - 1) % 5 == 0:
             total = (total - 1) / 5 * 4    
         else:
             enough = False
             break
     if enough:
         if attempt == 2:
             print(t)
             print(fish)
             break
         else: 
             enough = False
             attempt += 1
             continue
     fish += 5

# 1
4 * (c + d + b + a) - 4 = 5 * (e + d + c + b)
# 2
total = 5 * a + 1
a = (5 * b + 1) / 4
b = (5 * c + 1) / 4
c = (5 * d + 1) / 4
d = (5 * e + 1) / 4

total = 5 * ((5 * ((5 * ((5 * ((5 * e + 1) / 4) + 1) / 4) + 1) / 4) + 1) / 4) + 1

((5 * ((5 * e + 1) / 4) + 1) / 4) + 1) / 4)
4 
(x + 1) % 4 == 0
7


