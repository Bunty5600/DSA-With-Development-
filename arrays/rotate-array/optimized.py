
def rotate(self, nums, k):
    n = len(nums)
    k %= n
    nums.reverse()

    left, right = 0, k - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left, right = k, n - 1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
