import random


def pin():
    pin_code = ""
    while len(pin_code) < 4:
        pin_code += str(random.randint(0, 9))

    return pin_code


def card():
    card_number = "400000"
    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))
    card_number = luhn("add", card_number)
    return card_number


def luhn(mode, string):
    if mode == "add":
        numbers = list(string)
        for element in range(len(numbers)):
            numbers[element] = int(numbers[element])
        for counter in range(len(numbers)):
            if counter % 2 == 0:
                numbers[counter] *= 2
        for number in range(len(numbers)):
            if numbers[number] > 9:
                numbers[number] -= 9
        sum_of_numbers = 0
        luhn_number = 0
        for number in numbers:
            sum_of_numbers += number
        while sum_of_numbers % 10 != 0:
            luhn_number += 1
            sum_of_numbers += 1
        string += str(luhn_number)
        return string

    elif mode == "check":
        numbers = list(string)
        for element in range(len(numbers)):
            numbers[element] = int(numbers[element])
        numbers.pop(len(numbers) - 1)
        string_check = ""
        for number in numbers:
            string_check += str(number)
        check_card = luhn("add", string_check)
        return check_card == string
