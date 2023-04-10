# 1 count integer

numbers = [1, 2, 3, 4, 5, 3]
integer = 10

x=[i for j, i in enumerate(numbers) if i==integer]
if integer in numbers:
    print(len(x))
elif integer not in numbers:
    print("42")



# 2 list_func

list_func = [1, 2, 3, 4]
print(list_func)
list_func[3] = 6
print(list_func)

def reverse(list_func):
    new_list = list_func[::-1]
    return new_list

list_func = (1, 2, 3, 4)

print(reverse(list_func))



# 3 compare_lists

list1 = {"cat", "dog", "water"}
list2 = {"apple", "water", "banana"}

compare_lists = list1. intersection(list2)
print(compare_lists)



# 4 remove_duplicates

lst = ["flowers", "chocolate", "water", "flowers", "umbrella"]
lst = list(dict.fromkeys(lst))
print(lst)



# 5 dict_func
# my_dict ={
   # "Type": "iPhone_13",
    #"Brand": "Apple",
    #"Price": "820€"
   # }

#print(f"You have an {my_dict["Type"]} from {my_dict["Brand"]} and it costs {my_dict["Price"]}.")


# sets are unordered, tuple are unmutable, in an array elements can repeate themselves.
# concepts of object oriented

