
def substring(source, target):
    n = len(source)
    m = len(target)

    hash = {}
    for c in source:
        hash[c] = 1
    for c in target:
        if hash.get(c) == None:
            return -1           #如果target有source中没有的字符一定不可能
        
    #如果没有多余字符肯定可以拼接成，只需要考虑有多少步就可以
    l = 0
    r = 0
    res = 0
    while r < m:
        if target[r] == source[l]:
            r += 1
        l = (l+1) % n
        if l == 0 and r < m:              #如果走完一轮说明用过一遍source了
            res += 1

    return res
source = "abc"
target = "acdbc"
print(substring(source, target))