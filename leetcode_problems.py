import math
from typing import List

#709 To lower case
def to_lower(s):
    return s.lower()

#242 is anagram
def isAnagram(s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
print(isAnagram("anagram","nagaram"))

#1470 shuffle the array
def shuffle(nums, n):
    x, y = nums[:n], nums[n:]
    res = []
    for index in range(len(x)):
        res.append(x[index])
        res.append(y[index])
    return res
    
print(shuffle(nums = [2,5,1,3,4,7], n = 3))

#1108 Defanging an IP address
def defangIPaddr(address: str) -> str:
        return address.replace('.','[.]')
    
print(defangIPaddr("1.1.1.1"))

#1816. Truncate Sentence
def truncateSentence(s: str, k: int) -> str:
        return ' '.join(s.split(' ')[:k])
    
#771. Jewels and Stones
def numJewelsInStones(jewels: str, stones: str) -> int:
        res = 0
        for stone in stones:
            if stone in jewels:
                res+=1
        return res
    
#367. Valid Perfect Square
def isPerfectSquare(num: int) -> bool:
        return str(math.sqrt(num)).split('.')[-1]=='0'
    
print(isPerfectSquare(16))

#344. Reverse String
def reverseString(s):
    s.reverse()

#1480. Running Sum of 1d Array
def runningSum(nums: List[int]) -> List[int]:
    res = []
    for index in range(len(nums)):
        res.append(sum(nums[:index+1]))
    
    return res

print(runningSum([1,2,3,4]))

#1528. Shuffle String
def restoreString(s: str, indices: List[int]) -> str:
    res = ''
    for i in range(len(indices)):
        res += s[indices.index(i)]
    return res

print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))