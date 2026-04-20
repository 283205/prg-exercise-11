my_list = [3, 8, 1, 2, 32]
my_list.sort()
print(my_list)   # [1, 2, 3, 8, 32]

my_list = [3, 8, 1, 2, 32]
new_list = sorted(my_list)
print(my_list)   # [3, 8, 1, 2, 32]   ← beze změny
print(new_list)  # [1, 2, 3, 8, 32]
#sorted pusobi i na textove retezce,... univerzalni

my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list, reverse=True)
print(my_list)   # [32, 8, 3, 2, 1]
#reverse = False od nejmensiho po nejvetsi


#řadí se podle klíče
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
print(list_of_words)   # ['MOO', 'woof', 'meeeoow', 'BZZZZZZ']

list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)

