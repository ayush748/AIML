mark=[85, 92, 78, 96, 88]
print("Marks:", mark)
print("Average:", sum(mark)/len(mark))
print("Highest Mark:", max(mark))
print("Lowest Mark:", min(mark))
print("Sorted Marks:", sorted(mark))
print("Marks greater than 90:", [m for m in mark if m > 90])
print("Marks less than 80:", [m for m in mark if m < 80])
print("Marks between 80 and 90:", [m for m in mark if 80 <= m <= 90])
print("Marks squared:", [m**2 for m in mark])   
print("Marks cubed:", [m**3 for m in mark])
print(mark[1:4])  # Slicing the list from index 1 to 3
print(mark.index(96))  # Finding the index of the mark 96
append_mark = 95
mark.append(append_mark)  # Appending a new mark to the list
print("Marks after appending:", mark)
# all functions 
print("All marks are above 70:", all(m > 70 for m in mark))
print("Any mark is above 90:", any(m > 90 for m in mark))
print("Count of marks above 90:", sum(1 for m in mark if m > 90))
print("Count of marks below 80:", sum(1 for m in mark if m < 80))
print("Count of marks between 80 and 90:", sum(1 for m in mark if 80 <= m <= 90))   
# tuples
marks_tuple = (85, 92, 78, 96, 88)
print("Marks as tuple:", marks_tuple)
print("Average as tuple:", sum(marks_tuple)/len(marks_tuple))
# set
marks_set = {85, 92, 78, 96, 88}
print("Marks as set:", marks_set)
print("Average as set:", sum(marks_set)/len(marks_set))
# dictionary
marks_dict = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 96, 'Eva': 88}
print("Marks as dictionary:", marks_dict) 
print("Average as dictionary:", sum(marks_dict.values())/len(marks_dict))
