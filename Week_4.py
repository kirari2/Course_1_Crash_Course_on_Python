# Practice Quiz: Dictionaries

# Question 1
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains 
# complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for key, users in domains.items():
	  for user in users:
	    emails.append(user + "@" + key)
	return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
# Should print: ['clark.kent@gmail.com', 'diana.prince@gmail.com', 'peter.parker@gmail.com', 'barbara.gordon@yahoo.com', 'jean.grey@yahoo.com', 'bruce.wayne@hotmail.com']

# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to 
# return a dictionary with the users as keys and a list of their groups as values. 

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]
        return (user_groups)


print(groups_per_user({"local": ["admin", "userA"], "public": ["admin", "userB"], "administrator": ["admin"]}))
# Should print: {'admin': ['local', 'public', 'administrator'], 'userA': ['local'], 'userB': ['public']}
