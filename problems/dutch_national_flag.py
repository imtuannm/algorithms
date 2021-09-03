def dutch_national_flag_sort(nums: list) -> None:
    """
    Given an array `nums` with `n` objects colored red, white, or blue,
    sort them in-place so that objects of the same color are adjacent,
    with the colors in the order red, white, and blue.

    We will use the integers `0`, `1`, and `2` to represent the color
    red, white, and blue, respectively.

    .. testcode::
        nums = [2,0,2,1,1,0]
        dutch_national_flag_sort(nums)
        print(nums)

    .. testoutput::
        [0, 0, 1, 1, 2, 2]
    """
    pivot = 1
    smaller = 0
    larger = len(nums) - 1
    
    for i in range(0, len(nums)):
        if nums[i] < pivot:
            nums[smaller], nums[i] = nums[i], nums[smaller]
            smaller += 1
    
    for i in reversed(range(0, len(nums))):
        if nums[i] > pivot:
            nums[larger], nums[i] = nums[i], nums[larger]
            larger -= 1
