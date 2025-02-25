def find_max_number(nums: list):

    n = len(nums)
    maxi = float("-inf")
    for i in range(0, n):
        if nums[i] > maxi:
            maxi = nums[i]
    return maxi
    return max(nums)