nums = [2,7,11,15]
target = 9


dic = {}
for i in range(len(nums)):
    print(dic.get(target - nums[i]))
    if dic.get(target - nums[i]) != None:
        print([dic.get(target-nums[i]), i])
        break
    dic[nums[i]] = i
    print(dic)

