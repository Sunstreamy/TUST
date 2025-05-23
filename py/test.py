upper_cnt = 0
lower_cnt = 0
digit_cnt = 0

with open("test.txt", "r") as fin, open("test_copy.txt", "w") as fout:
    while True:
        ch = fin.read(1)
        if not ch:
            break
        if ch.islower():
            lower_cnt += 1
            fout.write(ch.upper())
        else:
            fout.write(ch)
        if ch.isupper():
            upper_cnt += 1
        if ch.isdigit():
            digit_cnt += 1

print(f"大写字母个数：{upper_cnt}")
print(f"小写字母个数：{lower_cnt}")
print(f"数字个数：{digit_cnt}")
