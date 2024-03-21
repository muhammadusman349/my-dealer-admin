############################# LEETCODE EXAMPLE ########################

###### TWO SUM #######
nums = [2,7,11,15]
sums = [3,2,4]
lums = [3,3]

target =9

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print (i, j)

#### WITH DEF FUNCTION ####
def two_sum(nums, target):
    dictt = {}
    for i in range(len(nums)):
        if target - nums[i] in dictt:
            return [dictt[target - nums[i]], i]
        else:
            dictt[nums[i]] = i

nums = [2, 7, 3, 3, 2]
target = 9
print(two_sum(nums, target))