SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10
}


def roman_to_integer(numeral):
    total = []
    for symbol in numeral:
        total.append(SYMBOLS[symbol])
    return sum(total)

