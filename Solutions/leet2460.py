# for i[0] and i[0+1]
#if equal, i[0]x2, else, continue
#finally,shift all 0s to the end

nums = [0,1]
def applyOperations(nums):
    i=0
    for i in range(len(nums)-1):
        if nums[i]== nums[i+1]:
            nums[i]=nums[i]*2
            nums[i+1]=0
    
    sorted_list=[x for x in nums if x!=0]
    zeros=[0]*(len(nums)-len(sorted_list))
    print(sorted_list+zeros)


    pass
applyOperations(nums)