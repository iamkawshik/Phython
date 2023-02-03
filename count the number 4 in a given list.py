def number(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(number([1, 3, 4,6, 8, 4, 2, 4,9,10]))