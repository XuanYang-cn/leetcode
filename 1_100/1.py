def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Change list into dictionary.
    # dictionary_keys are values of list nums
    # dictionary_value are indexes of list nums
    ref = {value: index for (index, value) in enumerate(nums)}

    for index, value in enumerate(nums):
        searchback = ref.get(target - value, None)
        if searchback != index:
            return [index, searchback]
        else:
            continue


nums = [2, 7, 11, 15]
target = 9
a = twoSum(nums, target)
print(a)
