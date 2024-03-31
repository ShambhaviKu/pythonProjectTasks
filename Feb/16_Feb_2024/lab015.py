#Dictionary

my_dict = {}
my_dic = dict()
print(type(my_dict))
print(type(my_dic))

my_dict = {"number": 8855}
print(my_dict["number"])

phonebook = {"batman": 748596, "superman": 3214, "Hanuman": 7775963214}
print(phonebook["Hanuman"])
print(len(phonebook))

phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(type(phone_book2))
print(phone_book2['GB'])
print(phone_book2["GB"])
print(phone_book2.get("GB"))

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 95}
print(len(my_dict))
print(my_dict["a"])

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(len(my_dict))
print(my_dict["a"])
