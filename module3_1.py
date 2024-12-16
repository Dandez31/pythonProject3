calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()
    lower_list = [item.lower() for item in list_to_search]
    lower_string = string.lower()
    return lower_string in lower_list


info = string_info("Capybara")
print(f"string_info('Capybara') = {info}")
info = string_info("Armageddon")
print(f"string_info('Armageddon') = {info}")
contains = is_contains("Urban", ["ban", "BaNaN", "urBAN"])
print(f"is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) = {contains}")
contains = is_contains("Urban", ["city", "village", "town"])
print(f"is_contains('Urban', ['city', 'village', 'town']) = {contains}")


print(f"Количество вызовов функций: {calls}")