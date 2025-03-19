def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    size = len(arr)
    # calculate the pos, neg, zero
    # O(n) time | O(1) space
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    # calculate the ratios and print it
    print(f"{pos/size:.6f}") # proportion of pos values
    print(f"{neg/size:.6f}") # proportion of neg values
    print(f"{zero/size:.6f}") # proportion of zero values