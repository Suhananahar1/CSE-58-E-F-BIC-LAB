pattern = input("Enter pattern: ")
text = input("Enter text: ")
d = int(input("d: "))

for i in range(len(text) - len(pattern) + 1):

    substring = text[i:i+len(pattern)]

    mismatch = 0

    for j in range(len(pattern)):
        if pattern[j] != substring[j]:
            mismatch += 1

    if mismatch <= d:
        print(i, end=" ")
