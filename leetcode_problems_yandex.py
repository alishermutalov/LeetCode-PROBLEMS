from typing import List
#228. Summary Ranges
def summaryRanges(nums: List[int]) -> List[str]:
    if not nums:  
        return []
    
    result = []
    start = nums[0]
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]+1:
            if start == nums[i-1]:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i-1]}")
            start = nums[i]
            
    if start == nums[-1]:
        result.append(str(start))
    else:
        result.append(f"{start}->{nums[-1]}")
        
    return result
            
#283. Move Zeroes
def moveZeroes(nums: List[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    

print(moveZeroes([0,1,0,3,12]))
                
