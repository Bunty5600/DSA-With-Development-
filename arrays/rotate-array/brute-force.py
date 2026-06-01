def rotate(nums, k):
    n = len(nums)

    for _ in range(k):
        last = nums[-1]

        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]

        nums[0] = last