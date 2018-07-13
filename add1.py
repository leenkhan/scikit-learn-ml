def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    newdigits = []
    newdigits = digits.reverse()
    digits.append(0)
    digits[0] = digits[0] + 1
    for i in range(0, len(digits)):
        num = digits[i]
        if num >=10:
            mo = num % 10
            digits[i]=mo
            digits[i+1]=digits[i+1]+1
    digits.reverse()
    if digits[0]==0: digits.pop(0)
    return digits

print(plusOne([9,9,9]))
print(plusOne([9,9,2,9]))