def product(self,nums):
    n=len(nums)
    answer=[]
    for i in range(0,n):
        prod=1
        for j in range(0,n):
            if i != j:
                prod *= nums[j]
        answer[i]=prod
    return answer
