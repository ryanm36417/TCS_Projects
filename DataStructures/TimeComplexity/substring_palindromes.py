string = "acbxbdboobdr"
longest = 0

for i in range(len(string)):

    left = i
    right = i
    while left > 0 and right < len(string) and string[left] == string[right]:
        longest = max(longest, right - left + 1)
        left -= 1
        right += 1

    left = i
    right = i + 1
    while left > 0 and right < len(string) and string[left] == string[right]:
        longest = max(longest, right - left + 1)
        left -= 1
        right += 1

print(longest)


































