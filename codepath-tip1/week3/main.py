# def count_mississippi(limit):
#     for num in range(1, limit):
#         print(f"{num} mississippi")


# count_mississippi(6)

# ---------------------------------

# def swap_ends(my_str):
#     my_str_list = list(my_str)
#     print(my_str_list)
#     my_str_list[0], my_str_list[len(
#         my_str_list) - 1] = my_str_list[len(my_str_list) - 1], my_str_list[0]
#     return "".join(my_str_list)


# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# ---------------------------------

# def is_pangram(my_str):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     new_str = my_str.lower()
#     in_alphabet = True
#     for char in alphabet:
#         if char in new_str:
#             continue
#         else:
#             in_alphabet = False
#     return in_alphabet


# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

# ---------------------------------

# def reverse_string(my_str):
#     reversed = []
#     for char in my_str[::-1]:
#         reversed.append(char)
#     return "".join(reversed)


# my_str = "live"
# print(reverse_string(my_str))

# ---------------------------------

# def first_unique_char(my_str):
#     dict = {}
#     for char in my_str:
#         if char in dict:
#             dict[char] += 1
#         else:
#             dict[char] = 1
#     for key, value in dict.items():
#         if value == 1:
#             return my_str.index(key)
#     return -1


# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# ---------------------------------
