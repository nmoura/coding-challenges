# https://www.hackerrank.com/challenges/30-dictionaries-and-maps


phone_book = {}

for index in range(int(input())):
    name_tel = input()
    phone_book[name_tel.split()[0]] = name_tel.split()[1]

while True:
    try:
        name_to_check = input()
    except EOFError:
        break
    if name_to_check in phone_book:
        print(name_to_check + "=" + phone_book[name_to_check])
    else:
        print("Not found")
