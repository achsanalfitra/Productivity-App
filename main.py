"""This is the main file"""

current_dictionary = {}

def multilevel_dictionary(current_dictionary, given_level, given_task, previous_task=None):
    """This function is a prototype of multilevel dictionary"""
    if given_level == 1:
        current_dictionary.setdefault(given_task, given_task)
    else:
        temp_dictionary = {}
        temp_dictionary.setdefault(given_task, given_task)
        current_dictionary[previous_task] = temp_dictionary
    return current_dictionary

current_dictionary = multilevel_dictionary(current_dictionary, 1, "eating")
current_dictionary = multilevel_dictionary(current_dictionary, 1, "going")
current_dictionary = multilevel_dictionary(
    current_dictionary, 2, "grocery shopping", previous_task="going")
current_dictionary = multilevel_dictionary(current_dictionary, 1, "laughing")
current_dictionary = multilevel_dictionary(current_dictionary, 1, "talking")
print(current_dictionary)

# End-of-file (EOF)
