def all_variants(text):
    num1_ = len(text)
    for i in range(1, num1_ + 1):
        for x in range(num1_ - i + 1):
            yield text[x:x + i]

a = all_variants("abc")
for i in a:
    print(i)