def first_duplicate(nums: list) -> int:
    """
    Given an array `nums` that contains only numbers in the range from `1` to 
    `len(nums)`, find the first duplicate number for which the second occurrence
    has the minimal index. In other words, if there are more than 1 duplicated numbers, 
    return the number for which the second occurrence has a smaller index than 
    the second occurrence of the other number does. If there are no such elements, 
    return -1.

    .. testcode::
        first_duplicate([2, 3, 3, 1, 5, 2])

    .. testoutput::
        3
    """
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] < 0:
            return abs(nums[i])
        else:
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]

    return -1
