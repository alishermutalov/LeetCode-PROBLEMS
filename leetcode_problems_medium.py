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
    
    res = [x for x in reversed(box)]
    for i in range(len(box)):
        for j in range(1,len(box)+1):
            pass
    print(box)
    print(res)                
          
        
    
    
     
rotateTheBox([["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]])

