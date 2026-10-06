# print('hello world')

# give a number N, count how many digits it contains 

# pseudocode
# TAKE INPUT N
# COUNT =0
# WHILE N >0

#   N = N //10
# COUNT = COUNT +1

# PRINT COUNT 

# n = int(input ("enter a  number:"))

# count =0
# while n>0:
#     n = n//10
#     count = count +1
# print(count)


# palindrome number

# n =int(input("enter a  number:"))

# original =n
# reverse=0
# while n>0 :

#     digit = n%10
#     reverse = reverse*10+digit
#     n =n//10
# if original == reverse:
#         print("palindrome")
# else:
#         print("not palindrome")


# find largest digit of a number


# 3 sum = 0 two pointers



nums = [-1, -1, -2, 0, 3, 2, 1]

# optimal approach
def threeSum(nums):
    result = []
    n = len(nums)

    nums.sort()

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i + 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result

print(threeSum(nums))