# Program to check if student has passed or failed

sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))

total = (sub1 + sub2 + sub3) / 3

if total >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("✅ Passed! Total Percentage:", total)
else:
    print("❌ Failed! Total Percentage:", total)
