# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = int(input("Please enter your sugar level: "))

if sugar_level < 80:
    print("Sugar level is low")
elif sugar_level > 100:
    print("Sugar level is high")
else:
    print("Sugar level is normal")

