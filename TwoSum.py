def twoSum(nums, target):
    sol = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                sol.append(i)
                sol.append(j)
                return sol


print(twoSum([3,2,4], 6))