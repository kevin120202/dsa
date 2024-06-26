# def is_perfect_number(n):
#     if n < 1:
#         return False

#     sum = 0
#     i = 1
#     while i <= n // 2:
#         if n % i == 0:
#             sum += i
#         i += 1

#     return sum == n

# divisors = []
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         divisors.append(i)
# total = 0
# for num in divisors:
#     total += num

# return total == n


# print(is_perfect_number(6))
# print(is_perfect_number(28))
# print(is_perfect_number(9))

# ---------------------------------------

# def is_palindrome(s):
#     ls = list(s)
#     start = 0
#     end = len(s) - 1
#     while start < end:
#         ls[start], ls[end] = ls[end], ls[start]
#         start += 1
#         end -= 1
#     return "".join(ls) == s


# s = "amanaplanacanalpanama"
# s2 = "hello world"

# print(is_palindrome(s))
# print(is_palindrome(s2))

# ---------------------------------------

# def reverse_vowels(s):
#     ls = list(s)
#     start = 0
#     end = len(s) - 1
#     while start < end:
#         if is_vowel(ls[start]) and is_vowel(ls[end]):
#             ls[start], ls[end] = ls[end], ls[start]
#             start += 1
#             end -= 1
#         elif not is_vowel(ls[start]):
#             start += 1
#         elif not is_vowel(ls[end]):
#             end -= 1

#     return "".join(ls)


# def is_vowel(char):
#     vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
#     return char in vowels


# s1 = "hello"
# rev_s1 = reverse_vowels(s1)
# print(rev_s1)

# s2 = "leetcode"
# rev_s2 = reverse_vowels(s2)
# print(rev_s2)

# ---------------------------------------

def removeElement(nums, val):
    pass

    for num in nums:
        if num == val:
            nums.pop(num)
    return len(nums)


nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums)  # same list
print(nums_len)
