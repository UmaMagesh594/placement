from collections import Counter
def number_to_text(n):
    num_text = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"
    }
    if n <= 19:
        return num_text[n]
    elif n == 100:
        return num_text[100]
    else:
        tens = (n // 10) * 10
        ones = n % 10
        return num_text[tens] + ('' if ones == 0 else num_text[ones])
def count_vowels(s):
    vowels = set('aeiou')
    return sum(1 for char in s if char in vowels)
def main():
    N = int(input())
    numbers = list(map(int, input().split()))
    total_vowels = 0
    for number in numbers:
        text_rep = number_to_text(number)
        total_vowels += count_vowels(text_rep)
    D = total_vowels
    count_pairs = 0
    num_count = Counter(numbers)
    for num in num_count:
        target = D - num
        if target in num_count:
            if num == target:
                count_pairs += num_count[num] * (num_count[num] - 1) // 2
            elif num < target:
                count_pairs += num_count[num] * num_count[target]
    if count_pairs > 100:
        print("greater 100")
    else:
        pair_text = number_to_text(count_pairs)
        print(pair_text)
if __name__ == "__main__":
    main()
