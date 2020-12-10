def isStingPalindrom(text_string):
    string_len = len(text_string)
    start = 0
    end = string_len - 1

    while (start < end):
        if (text_string[start].lower() != text_string[end].lower()):
            return False
        start += 1
        end -= 1

    return True

a = isStingPalindrom('ANNA')
print(a)