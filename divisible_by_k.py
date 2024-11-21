from typing import List


def canArrange(arr: List[int], k: int) -> bool:
    pairs_list = []
    for i in range(len(arr)//2):
        pairs = False
        for j in range(1,len(arr)):
            if (arr[i]+arr[j])%k==0:
                pairs_list.append(arr[i])
                pairs_list.append(arr[j])
                pairs=True
            if pairs:
                break
    print(pairs_list)
    print(arr)

    if len(arr) == len(pairs_list):
        return True
    else:
        return False
    
    
print(canArrange([1,2,3,4,5,10,6,7,8,9],5))