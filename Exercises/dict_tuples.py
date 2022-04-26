country_pop = {"China": 143000, "India": 136000, "USA": 32000, "Pakistan": 21000}

#for key in country_pop:
    #print(key, "==>", country_pop[key])

country_pop["Kenya"] = 85000 # adding key-value pairs to dictionaries

print(country_pop)

# Program to ask user to add new country. If country exists, program to print it exists and do nothing
# If country doesn't exist, user is prompted to add new country and population
# Program should print final result in format required
country_name = input("Enter a country name: ")

if country_name in country_pop:
    print("The country entered exists")
else:
    pop_data = int(input("Enter population size: "))

country_pop[country_name] = pop_data # country added to dictionary

for key in country_pop:
    print(key, "==>", country_pop[key])


# This program prompts the user to input a country they wish to remove
# from the dictionary
# After removal, the program prints the dictionary using the prescribed format
# A country not in the dictionary prints "Country does not exist"
del_country = input("Enter country you wish to remove: ")

if del_country in country_pop:
    del country_pop[del_country]

else:
    print("The country entered does not exist.")

for key in country_pop:
    print(key, "==>", country_pop[key])

# This program prompts the user to query for a particular country within the dictionary
# Countries not in the dict prints "Country does not exist
# After successful querying, the program returns the population size of the country
country_name = input("Enter a country name to query: ")

if country_name in country_pop:
    print(country_pop[country_name])
else:
    print("The country entered does not exist.")