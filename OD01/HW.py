# Проверка фразы на палиндром
# 1) "переворачиваем" слово или фразу
# 2 сравниваем с исходной
# 3) если они равны - значит Палиндром

# phrase = 'поп'


def palindrome(phrase):
    swapped_phrase = phrase[::-1]
    if swapped_phrase == phrase:
        return True
    else:
        return False

print(palindrome('pop'))