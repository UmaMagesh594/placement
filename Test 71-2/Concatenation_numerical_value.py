def string_to_value(s):
    value_str = ''.join(str(ord(char) - ord('a')) for char in s)
    return int(value_str) if value_str else 0
def is_sum_equal(firstWord, secondWord, targetWord):
    first_value = string_to_value(firstWord)
    second_value = string_to_value(secondWord)
    target_value = string_to_value(targetWord)
    return first_value + second_value == target_value
firstWord = input().strip()
secondWord = input().strip()
targetWord = input().strip()
result = is_sum_equal(firstWord, secondWord, targetWord)
print(str(result).lower())
