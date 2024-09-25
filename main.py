def mutiple_tuple(nums):
    temp = list(nums)
    product = 1 
    for i in temp:
        product *= i
    return product
nums = (4, 3, 2, 2, -1, 18)
print(nums)
print("multiplying all the numbers of the tuple:", mutiple_tuple(nums))
nums = (2, 4, 8, 8, 3, 2, 9)
print("multiplying all the numbers of the tuple:", mutiple_tuple(nums))