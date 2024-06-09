# Problem sets

# def is_subsequence(lst, sequence_lst):
#     index = 0
#     for num in lst:
#         print(index)
#         if num == sequence_lst[index]:
#             index += 1
#     return index == len(sequence_lst)


# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))

# -------------------------

# def create_dictionary(keys, values):
#     dict = {}
#     for i in range(len(keys)):
#         dict[keys[i]] = values[i]
#     return dict


# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# print(create_dictionary(keys, values))

# -------------------------

# def print_pair(dictionary, target):
#     for key in dictionary:
#         if key == target:
#             return f"Key: {key}\nValue: {dictionary[key]}"
#     return "That pair does not exist!"


# dictionary = {"spongebob": "squarepants",
#               "patrick": "star", "squidward": "tentacles"}
# print(print_pair(dictionary, "patrick"))
# print(print_pair(dictionary, "plankton"))
# print(print_pair(dictionary, "spongebob"))

# -------------------------

# def keys_v_values(dictionary):
#     keys_sum = 0
#     values_sum = 0
#     for key in dictionary:
#         keys_sum += key
#         values_sum += dictionary[key]
#     if keys_sum > values_sum:
#         return "keys"
#     elif values_sum > keys_sum:
#         return "values"
#     else:
#         return "balanced"


# dictionary1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100: 10, 200: 20, 300: 30, 400: 40, 500: 50, 600: 60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)

# -------------------------

# def restock_inventory(current_inventory, restock_list):
#     for key in restock_list:
#         if key not in current_inventory:
#             current_inventory[key] = restock_list[key]
#         else:
#             current_inventory[key] += restock_list[key]
#     return current_inventory


# current_inventory = {
#     "apples": 30,
#     "bananas": 15,
#     "oranges": 10
# }

# restock_list = {
#     "oranges": 20,
#     "apples": 10,
#     "pears": 5
# }
# print(restock_inventory(current_inventory, restock_list))

# -------------------------

# def calculate_gpa(report_card):
#     grade_points = {
#         "A": 4,
#         "B": 3,
#         "C": 2,
#         "D": 1,
#         "F": 0
#     }
#     gpa = 0
#     for key in report_card:
#         letter_grade = report_card[key]
#         gpa += grade_points[letter_grade]
#     return round(gpa / len(report_card), 2)


# report_card = {"Math": "A", "Science": "C", "History": "A",
#                "Art": "B", "English": "B", "Spanish": "A"}
# print(calculate_gpa(report_card))

# -------------------------

# def highest_rated(books):
#     highest_rated = books[0]
#     for i in range(len(books)):
#         if books[i]["rating"] > highest_rated["rating"]:
#             highest_rated = books[i]
#     return highest_rated


# books = [
#     {"title": "Tomorrow, and Tomorrow, and Tomorrow",
#      "author": "Gabrielle Zevin",
#      "rating": 4.18
#      },
#     {"title": "A Fortune For Your Disaster",
#      "author": "Hanif Abdurraqib",
#      "rating": 4.47
#      },
#     {"title": "The Seven Husbands of Evenlyn Hugo",
#      "author": "Taylor Jenkins Reid",
#      "rating": 4.40
#      }
# ]
# print(highest_rated(books))

# -------------------------

# def index_to_value_map(lst):
#     dict = {}
#     for i in range(len(lst)):
#         dict[i] = lst[i]
#     return dict


# lst = ["apple", "banana", "cherry"]
# print(index_to_value_map(lst))
