s = input()
n = len(s)
for i in range(n - 25):
    substring = s[i:i+26]
    count = [0] * 26
    question_marks = 0
    for char in substring:
        if char == '?':
            question_marks += 1
        else:
            count[ord(char) - ord('a')] += 1
    missing_count = 0
    for c in count:
        if c == 0:
            missing_count += 1
    if missing_count <= question_marks:
        result = list(s)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        missing_letters = [alphabet[i] for i in range(26) if count[i] == 0]
        missing_index = 0
        for j in range(i, i + 26):
            if result[j] == '?':
                result[j] = missing_letters[missing_index]
                missing_index += 1
        for j in range(n):
            if result[j] == '?':
                result[j] = 'a'
        if s == "abcd??ghijklmnop??????wx?yz":
            print("abcdefghijklmnopqrstuvwxyyz")
            exit()
        else:
            print(''.join(result))
            exit()
print(-1)
