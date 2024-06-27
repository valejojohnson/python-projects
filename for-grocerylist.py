def sort_groceries(grocery_list):
    grocery_list.sort()
    return grocery_list


grocery_list = ["bread", "milk", "cheese", "apples", "tuna"]
sorted_gl = sort_groceries(grocery_list)

for item in sorted_gl:
    print(item)
