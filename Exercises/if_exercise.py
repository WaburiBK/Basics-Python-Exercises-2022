"""
Write a program that asks a user to enter a city name and it should
tell which country the city belongs to
"""

India = ["Mumbai", "Banglore", "Chennai", "Delhi"]
Pakistan = ["Lahore", "karachi", "Islamabad"]
Bangladesh = ["Dhaka", "Khulna", "Rangpur"]

city = input("Please enter city name: ")

if city in India:
    print("The city you entered is in India", )
elif city in Pakistan:
    print("The city you entered is in Pakistan", )
elif city in Bangladesh:
    print("The city you entered is in Bangladesh", )
else:
    print("The city you entered is not in our list")
