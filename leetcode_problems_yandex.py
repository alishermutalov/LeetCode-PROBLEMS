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
    
#125. Valid Palindrome
def isPalindrome(s: str) -> bool:
        new_s = []
        for i in s.lower():
            if i.isalpha() or i.isnumeric():
                new_s.append(i)
        reversed_text = reversed(new_s)
        return ''.join(new_s) == ''.join(reversed_text)

#977. Squares of a Sorted Array
def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i]=nums[i]*nums[i]
    nums.sort()
    return nums

print(sortedSquares([-4,-1,0,3,10]))

#20. Valid Parentheses
def isValid(s: str) -> bool:
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if stack and stack[-1]==pairs[char]:
                stack.pop()
            else:
                return False
        else:
            return False
        
    return len(stack)==0

#350. Intersection of Two Arrays II
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res