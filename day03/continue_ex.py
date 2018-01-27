result = 0
count = 0
while count < 100:
    count += 1
    if count % 2:
        continue
    result += count

print(result)