# Week 4 Graded Assessment

# Question 1
# The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long 
# (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive"). 
# Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street".
# This function should:
# 1. accept a string through the parameters of the function;
# 2. separate the address string into new strings: house_number and street_name; 
# 3. return the variables in the string format: "House number X on a street named Y". 

def format_address(address_string):
   
    house_number = ""
    street_name = ""
    
    # Separate the house number from the street name.
    address_parts = address_string.split()
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if address_part.isnumeric():
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.rstrip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))  # Should print: "House number 123 on a street named Main Street"
print(format_address("1001 1st Ave"))  # Should print: "House number 1001 on a street named 1st Ave"
print(format_address("55 North Center Drive"))  # Should print "House number 55 on a street named North Center Drive"

# Question 2
# Fill in the blank to complete the “string_words” function. This function should split up the words in the given “string” and return the number of words in the “string”. 
# Complete the string operation and method needed in this function so that a function call like "string_words("Hello, World")" will return the output "2".

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())


print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

# Question 3
# Consider the following scenario about using Python lists: 
# A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students in the order they arrived in the classroom. Aniyah was the 
# first one  to note which students arrived, and then Imani took over. After class, they each entered their lists into the computer and emailed them to the professor. 
# The professor wants to combine the two lists into one and sort it in alphabetical order. 
# Complete the code by combining the two lists into one and then sorting the new list. This function should:
# 1. accept two lists through the function’s parameters;,
# 2. combine the two lists;
# 3. sort the combined list in alphabetical order;
# 4. return the new list. 

def alphabetize_lists(list1, list2):
    new_list = [] # Initialize a new list.
    list1.extend(list2) # Combine the lists.
    list1.sort() # Sort the combined lists.
    new_list = list1.copy() # Assign the combined lists to the "new_list".
    return new_list


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

print(alphabetize_lists(Aniyahs_list, Imanis_list)) # Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

# Question 4
# Fill in the blank to complete the “increments” function. This function should use a list comprehension to create a list of numbers incremented by 2 (n+2). 
# The function receives two variables and should return a list of incremented consecutive numbers between “start” and “end” inclusively (meaning the range should 
# include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 5]”.

def increments(start, end):
    return [ n + 2 for n in range(start, end + 1) ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Question 5
# Fill in the blanks to complete the “countries” function. This function accepts a dictionary containing a list of continents (keys) and several countries from each 
# continent (values).  For each continent, format a string to print the names of the countries only. The values for each key should appear on their own line.

def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for keys, values in countries_dict.items():
        # Use a string method to format the required string.
        result += str(values) + "\n"
    return result

print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']

# Question 6
# Consider the following scenario about using Python dictionaries: 
# Tessa and Rick are hosting a party. Both sent out invitations to their friends, and each one collected responses into dictionaries, with names of their friends and 
# how many guests each friend was bringing. Each dictionary is a partial guest list, but Rick's guest list has more current information about the number of guests. 
# Complete the function to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rick's dictionary taking precedence, 
# if a name is included in both dictionaries. Then print the resulting dictionary. This function should:
# 1. accept two dictionaries through the function’s parameters;
# 2. combine both dictionaries into one, with each key listed only once;
# 3. the values from the “guests1” dictionary taking precedence, if a key is included in both dictionaries;
# 4. then print the new dictionary of combined items.

def combine_guests(guests1, guests2):
  guests2.update(guests1)  # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

# Question 7
# Complete the function so that input like "This is a sentence." will return a dictionary that holds the count of each letter that occurs in the string: 
# {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}. This function should:
# 1. accept a string “text” variable through the function’s parameters;
# 2. iterate over each character the input string to count the frequency of each letter found, (only letters should be counted, do not count blank spaces, numbers, or 
# punctuation; keep in mind that Python is case sensitive);
# 3. populate the new dictionary with the letters as keys, ensuring each key is unique, and assign the value for each key with the count of that letter;
# 4. return the new dictionary.

def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for character in text.lower():   
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if character.isalpha():
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if character not in dictionary: 
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[character] = 0  
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[character] += 1 # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

# Question 8 
# What do the following commands return when genre = "transcendental"?

genre = "transcendental"
print(genre[:-8])
print(genre[-7:9])

# Should be "transc, nd"

# Question 9
# What does the list "music_genres" contain after these commands are executed?

music_genres = ["rock", "pop", "country"]
music_genres.append("blues")
print(music_genres)

# Should be ['rock', 'pop', 'country', 'blues']

# Question 10
# What do the following commands return?

speed_limits = {"street": 35, "highway": 65, "school": 15}
speed_limits["highway"]

# Should be 65

# Question 11
# Fill in the blanks to complete the “confirm_length” function. This function should return how many characters a string contains as long as it has one or more 
# characters, otherwise it will return 0. Complete the string operations needed in this function so that input like "Monday" will produce the output "6".

def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) >= 1:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

# Question 12
# Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". 
# This function should:
# 1. accept a string through the parameters of the function;
# 2. iterate over the characters in the string;
# 3. determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);
# 4. increment the counter;
# 5. return the count of letters in the string.

def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string: 
        # Complete the if-statement using a string method. 
        if character.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

# Question 13
# Consider the following scenario about using Python lists: 
# Employees at a company shared  the distance they drive to work (in miles) through an online survey. These distances were automatically added by Python to a list 
# called “distances” in the order that each employee submitted their distance. Management wants the list to be sorted in the order of the longest distance to the 
# shortest distance. 
# Complete the function to sort the “distances” list. This function should:
# 1. sort the given “distances” list, passed through the function’s parameters; ; 
# 2. reverse the sort order so that it goes from the longest to the shortest distance;
# 3. return the modified “distances” list.

def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

# Question 14
# Fill in the blank to complete the “squares” function. This function should use a list comprehension to create a list of squared numbers (using either the expression n*n 
# or n**2). The function receives two variables and should return the list of squares that occur between the “start” and “end” variables inclusively (meaning the range 
# should include both the “start” and “end” values). Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 9]”.

def squares(start, end):
    return [ n*n for n in range(start, end + 1) ] # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Question 15
# Consider the following scenario about using Python dictionaries: 
# Tessa and Rick are hosting a party. Together, they sent out invitations, and collected the responses in a dictionary, with names of their friends and the number of guests 
# each friend will be bringing. Complete the function so that the “check_guests” function retrieves the number of guests (value)  the specified friend “guest” (key) is bringing.
# This function should: 
# 1. accept a dictionary “guest_list” and a key “guest” variable passed through the function parameters;
# 2. print the values associated with the key variable.

def check_guests(guest_list, guest):
  return guest_list[guest] # Return the value for the given key


guest_list = { "Adam":3, "Camila":3, "David":5, "Jamal":3, "Charley":2, "Titus":1, "Raj":6, "Noemi":1, "Sakira":3, "Chidi":5}


print(check_guests(guest_list, "Adam")) # Should print 3
print(check_guests(guest_list, "Sakira")) # Should print 3
print(check_guests(guest_list, "Charley")) # Should print 2

# Question 16
# Use a dictionary to count the frequency of numbers in the given “text” string. Only numbers should be counted. Do not count blank spaces, letters, or punctuation. Complete 
# the function so that input like "1001000111101" will return a dictionary that holds the count of each number that occurs in the string  {'1': 7, '0': 6}. This function should: 
# 1. accept a string “text” variable through the function’s parameters;
# 2. initialize an new dictionary;
# 3. iterate over each text character to check if the character is a number’
# 4. count the frequency of numbers in the input string, ignoring all other characters;
# 5. populate the new dictionary with the numbers as keys, ensuring each key is unique, and assign the value for each key with the count of that number;
# 6. return the new dictionary.

def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {}
  # Complete the for loop to iterate through each "text" character.
  for character in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if character.isnumeric():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if character not in dictionary:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           dictionary[character] = 0
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      dictionary[character] += 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}

# Question 17
# What does the list "colors" contain after these commands are executed?

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

# Should be: colors = ["red", "white", "blue"]

# Question 18
# What do the following commands return?

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())

# Should print: dict_keys(['router', 'localhost', 'google'])
