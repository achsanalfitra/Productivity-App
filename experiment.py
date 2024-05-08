a_dictionary = {}

def list_mapping(given_dictionary, given_task, given_level, previous_task=None):
    if given_level == 1:
        given_dictionary.setdefault(given_task, )
    else:
        given_dictionary.setdefault(given_task, )

list_mapping(a_dictionary, "Eating", 1)
list_mapping(a_dictionary, "Managing", 1)
list_mapping(a_dictionary, "Skiing", 1)
list_mapping(a_dictionary, "Snowing", 2, "Skiing")
list_mapping(a_dictionary, "Melting", 3, "Snowing")


print(a_dictionary)
