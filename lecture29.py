numbers =[4,2,9,1,5,6]
length = len(numbers)
print(f"length of the list: {length}")

total_sum= sum(numbers)
print(f"Sum of all elements:{total_sum}")

max_value=max(numbers)
print(f"maximum value: {max_value}")

min_value= min(numbers)
print(f"Minimum value: {min_value}")

sorted_Numbers= sorted(numbers)
print(f"sorted list:{sorted_Numbers}")

bool_list = [False,True,False]
any_true= any(bool_list)
print(f"Is any element Ture? {any_true}")

all_true = all(bool_list)
print(f"Are all elements True? {all_true}")

string= "hello"
char_list = list(string)
print(f"list of characters: {char_list}")

reversed_number= list(reversed(numbers))
print(f"Reversed list: {reversed_number}")

enumerate_number= list(enumerate(numbers))
print(f"Enumerated list: {enumerate_number}")