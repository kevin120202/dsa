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

# def removeElement(nums, val):
#     slow = 0
#     fast = 0
#     while fast < len(nums):
#         if nums[fast] != val:
#             nums[slow] = nums[fast]
#             slow += 1
#         fast += 1
#     return slow


# nums = [5, 4, 4, 3, 4, 1]
# nums_len = removeElement(nums, 4)
# print(nums)  # same list
# print(nums_len)

# ---------------------------------------

# def is_long_pressed(name, typed):
#     i = 0
#     j = 0
#     while j < len(typed):
#         if name[i] == typed[i]:
#             i += 1
#             j += 1
#         elif name[i-1] == typed[j]:
#             j += 1
#         else:
#             return False
#     if i != len(name):
#         return False
#     return True


# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

# ---------------------------------------

# def find_content_children(greed_ls, cookie_size_ls):
#     content_children = 0
#     greed_ls_ptr = 0
#     cookie_size_ls_ptr = 0

#     while greed_ls_ptr < len(greed_ls) and cookie_size_ls_ptr < len(cookie_size_ls):
#         if greed_ls[greed_ls_ptr] <= cookie_size_ls[cookie_size_ls_ptr]:
#             content_children += 1
#         cookie_size_ls_ptr += 1
#         greed_ls_ptr += 1

#     return content_children


# # g = [1, 2, 3]
# # s = [1, 1, 3]
# g = [1, 1]
# s = [2, 2, 2]
# print(find_content_children(g, s))

# ---------------------------------------

# def valid_palindrome(s):
#     start = 0
#     end = len(s) - 1
#     while start < end:
#         if s[start] == s[end]:
#             start += 1
#             end -= 1
#         else:
#             return is_substring_palindrome(s[start+1:end+1]) or is_substring_palindrome(s[start:end])

#     return True


# def is_substring_palindrome(substring):
#     start = 0
#     end = len(substring) - 1
#     while start < end:
#         if substring[start] != substring[end]:
#             return False
#         start += 1
#         end -= 1
#     return True


# s = "aba"
# s2 = "abca"
# s3 = "abc"

# print(valid_palindrome(s))
# print(valid_palindrome(s2))
# print(valid_palindrome(s3))

# ---------------------------------------
