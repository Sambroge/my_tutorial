import random


def generate(check_box_value, check_box_value2, check):
    false_symbols = ''
    symbols = []

    if check[0]:
        symbols.extend(digits)
        false_symbols += '10'
    if check[1]:
        symbols.extend(lowercase_letters)
        false_symbols += 'ilo'
    if check[2]:
        symbols.extend(uppercase_letters)
        false_symbols += 'LO'
    if check[3]:
        symbols.extend(punctuation)
    if check[4]:
        for letter in false_symbols:
            if letter in symbols:
                symbols.remove(letter)
#    if check[5]:
#        documents_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#        file = open('Пароли от ' + documents_time + '.txt', 'x')
#        for i in range(len(chars)):
#            file.write(chars[i] + '\n')
#        file.close()

    password_generate = ''
    for j in range(check_box_value):
        for k in range(check_box_value2):
            password_generate += random.choice(symbols)
        password_generate += '\n'
    return password_generate


# Все символы которые могут быть в генерируемом пароле
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
