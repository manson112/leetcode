nums1 = [1,2]
nums2 = [3,4]

answer = []
i = 0
while len(nums1) != 0 or len(nums2) != 0:
    a = nums1[0] if len(nums1) != 0 else None
    b = nums2[0] if len(nums2) != 0 else None
    if a == None:
        answer += nums2
        break
    if b == None:
        answer += nums1
        break
    
    if a <= b:
        answer += [a]
        nums1.pop(0)
    else:
        answer += [b]
        nums2.pop(0)

ans = 0
if len(answer) % 2 == 0:
    ans = (answer[len(answer) // 2] + answer[len(answer) // 2 - 1]) / 2
else:
    ans = answer[len(answer) // 2] / 1

print(float(ans))