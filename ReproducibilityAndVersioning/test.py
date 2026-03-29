def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    if len(in_list) > 0:
        srted_num = sorted(in_list)
        for num in srted_num:
            if num > 0:
                return num
        return 0
    else:
        return 0
    
# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
print(smallest_positive([-6, -9, -7]))
# Correct output: None
print(smallest_positive([]))