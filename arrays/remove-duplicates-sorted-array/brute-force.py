
def removeDuplicates(self, nums):

    temp = [0] * len(nums)
    temp[0] = nums[0]

    j = 1

    for i in range(1, len(nums)):

        found = False

        for k in range(j):

            if temp[k] == nums[i]:
                found = True
                break

        if not found:

            temp[j] = nums[i]

            j += 1

    for i in range(j):

        nums[i] = temp[i]

    return j