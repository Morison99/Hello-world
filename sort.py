# import os
# os.system('cls')


def sort_item(item):
    return item[1]


product = [(1, 5, 13), (5, 30, 10), (0, 20, 6)]


# product.sort(key=sort_item)          #bar asas def
# print(product)

product.sort(key=lambda item: item[0])  # bar asas lambda
print(product)
