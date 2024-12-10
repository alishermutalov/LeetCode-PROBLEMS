from typing import List, Optional
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
    
#206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next 
            current.next = prev     
            prev = current       
            current = next_node

        return prev   
        
def isPalindrome(s: str) -> bool:
        new_s = []
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                new_s.append(i)
        reversed_text = reversed(new_s)
        return ''.join(new_s) == ''.join(reversed_text)
