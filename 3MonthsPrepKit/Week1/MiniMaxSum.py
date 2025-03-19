# arr = [1, 3, 5, 7, 9]
# min = 1, max = 9
# minSum = sumOfElements - max
# maxSum = sumOfElements - min
# sorting takes O(nlogn)
def miniMaxSum(arr):
    # Initialize variables
    minVal = maxVal = arr[0]
    total = 0
    
    # Iterate through the array to calculate the total sum and find min and max values
    for num in arr:
        total += num
        if num < minVal:
            minVal = num
        if num > maxVal:
            maxVal = num
    
    # Calculate minSum and maxSum by excluding the min and max values
    minSum = total - maxVal
    maxSum = total - minVal
    
    # Print the results
    print(minSum, maxSum)