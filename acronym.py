user_input = input('enter phrase: ')
list_items = user_input.split()
acronym = ''
for item in list_items:
    acronym = acronym + str(item[0]).upper()
print(acronym)
