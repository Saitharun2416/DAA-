def maxDifference(num):
    num_str = str(num)
    
    for digit in num_str:
        if digit != '9':
            max_num_str = num_str.replace(digit, '9')
            break
    else:
        max_num_str = num_str
   
    if num_str[0] != '1':
        min_num_str = num_str.replace(num_str[0], '1')
    else:
        for digit in num_str[1:]:
            if digit != '0' and digit != '1':
                min_num_str = num_str.replace(digit, '0')
                break
        else:
            min_num_str = num_str

    max_num = int(max_num_str)
    min_num = int(min_num_str)
    
    return max_num - min_num

# Example 1
num = 555
print(maxDifference(num)) 

# Example 2
num = 9
print(maxDifference(num)) 
