calls = 0

def count_calls():
    global calls
    calls += 1

def string_info (string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    list = [a, b, c]
    return list

def is_contains(string, list_to_search):
    count_calls()
    string_info(string)
    #string.casefold() - не получается пренебречь регистром
    if list_to_search == list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)







