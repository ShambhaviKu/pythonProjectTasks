api_response = {
    "id": 852,
    "name": 'john',
    "age": 29,
    "country": 'US',
    "pass" : "D52jg"
}

for k, v in api_response.items():
    print(k, '>>' , v)


print(api_response)
print(type(api_response))
print(api_response.get("pass"))

dictionary1 = (api_response.keys())
list1 = list(dictionary1)
print(list1)

dictionary2 = (api_response.values())
list2 = list(dictionary2)
print(list2)

my_list = list1 + list2
print(my_list)