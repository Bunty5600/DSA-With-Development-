def removeDuplicates(self, nums):

    if len(nums) == 0:
        return 0

    write = 1

    for read in range(1, len(nums)):

        if nums[read] != nums[read - 1]:

            nums[write] = nums[read]

            write += 1
    return write
