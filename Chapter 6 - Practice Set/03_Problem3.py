# Program to detect spam comments

text = input("Enter your comment: ").lower()

if ("make a lot of money" in text 
    or "buy now" in text 
    or "subscribe this" in text 
    or "click this" in text):
    print("⚠️ This is a spam comment.")
else:
    print("✅ This comment is clean.")
