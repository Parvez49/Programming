

nums=[10,11,7,12,9,8]
# length: 3
# res: [8, 11, 12] we find longest length but not longest list

nums = [10,9,2,5,3,7,101,18]
# length: 4
# res: [2, 3, 7, 18]

def binarys(val, res):
    l = 0
    r = len(res) - 1
    while l <= r:
        mid = (l + r) // 2
        if res[mid] > val:
            r = mid - 1
        elif res[mid] < val:
            l = mid + 1
        else:
            return mid
    return l

res = []
for i in nums:
    pos = binarys(i, res)
    if pos == len(res):
        res.append(i)
    else:
        res[pos] = i
print(res)
print(len(res))
