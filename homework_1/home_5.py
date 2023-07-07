# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001

num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt = 1
limit_attempt = 10

print("Я загадал число от 0 до 1000 включительно.\n"
      "У тебя 10 попыток, чтобы его угадать. "
      "Попробуешь?")

while attempt <= limit_attempt:
    temp = int(input())
    if temp > num:
        print('Много')
    elif temp < num:
        print('Мало')
    else:
        print('Вы угадали! Для этого потребовалось', attempt, 'попыток.')
        break
    attempt += 1
else:
    print('Вы потратили 10 попыток. Было загадано число:', num)