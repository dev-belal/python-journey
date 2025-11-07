"""Program to Sort marks of 6 students"""

# Concept: The sort() method arranges list elements in ascending order.

marks = []

# Using Manual append
f1 = input("Enter marks of student: ")
marks.append(f1)
f2 = input("Enter marks of student: ")
marks.append(f2)
f3 = input("Enter marks of student: ")
marks.append(f3)
f4 = input("Enter marks of student: ")
marks.append(f4)
f5 = input("Enter marks of student: ")
marks.append(f5)
f6 = input("Enter marks of student: ")
marks.append(f6)


# # Using For Loop
# for i in range(6):
#     mark = int(input(f"Enter marks of student {i+1}: "))
#     marks.append(mark)

marks.sort()
print("\nMarks in sorted order:", marks)
