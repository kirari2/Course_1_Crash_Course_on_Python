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
