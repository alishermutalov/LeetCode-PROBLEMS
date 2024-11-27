#1861. Rotating the Box
from typing import List


def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    row = len(box[0])
    column = len(box)
    for i in box: 
        for j in range(len(i)):
            for x in range(0,len(i)-j-1):
                if i[x]=='#' and i[x+1]=='.':
                    i[x], i[x+1] = i[x+1], i[x]
    
    reversed_box = [x for x in reversed(box)]
    result = []
    for i in range(row):
        new_list = []
        for j in range(column):
            new_list.append(reversed_box[j][i])
        result.append(new_list)
    
    return result            
       
rotateTheBox([["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]])

#1509. Minimum Difference Between Largest and Smallest Value in Three Moves
def minDifference(nums: List[int]) -> int:  
    n = len(nums)
    if n < 5:
            return 0
    nums.sort()
    res = min([nums[-1]-nums[3],nums[-2]-nums[2], nums[-3]-nums[1], nums[-4]-nums[0]])
    return res
        
print(minDifference([3,100,20]))