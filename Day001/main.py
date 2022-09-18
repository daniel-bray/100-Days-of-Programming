# make sure the input cursor shows on a new line.
# 1. Create a greeting for your program
from itertools import permutations


print("Welcome to the band name generator!")

# 2. Ask the user for the name of the city that they grew up in.
city_name = input("Enter the name of the city you grew up in:\n")

# 3. Ask the user for the name of a pet.
pet_name = input("Enter the name of a pet:\n")

# 4. Combine the name of their city and pet and shwo them their band name.
band_name = city_name + " " + pet_name

print("Your band name could be " + band_name)
