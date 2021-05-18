def maddle_number(num1, num2):
    if len(num1) == 0 and len(num2) == 0:
        return 0
    result = []
    i = j = 0
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            result.append(num1[i])
            i = i + 1
        else:
            result.append(num2[j])
            j = j + 1
    while i < len(num1):
        result.append(num1[i])
        i = i + 1
    while j < len(num2):
        result.append(num2[j])
        j = j + 1
    if len(result) % 2 == 0:
        r1 = int(len(result) / 2)
        r2 = r1 - 1
        r = (result[r1] + result[r2]) / 2
        return r
    else:
        r = result[int(len(result) / 2)]
        return r
