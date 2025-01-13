def three_sum(nums):
    """
    Find all unique triplets in the array that sum up to zero.

    Parameters:
        nums (List[int]): The input list of integers.

    Returns:
        List[List[int]]: A list of unique triplets that sum to zero.

    Examples:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> three_sum([0, 1, 1])
        []
        >>> three_sum([0, 0, 0])
        [[0, 0, 0]]
    """
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Input list must contain only integers.")

    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result
