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

#1662. Check If Two String Arrays are Equivalent
def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)

print(arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))

#231. Power of Two
def isPowerOfTwo(n: int) -> bool:
    if n<=0:
        return False
    return str(math.log2(n)).split('.')[-1] == '0'

print(isPowerOfTwo(0))

#412. Fizz Buzz
def fizzBuzz(n: int) -> List[str]:
    res = []
    for i in range(1,n+1):
        print(i%15)
        if i%15==0:
            res.append('FizzBuzz')
        elif i%5==0:
            res.append('Buzz')
        elif i%3==0:
            res.append('Fizz')
        else:
            res.append(f'{i}')
    return res

print(fizzBuzz(3))

#1460. Make Two Arrays Equal by Reversing Subarrays
def canBeEqual(target: List[int], arr: List[int]) -> bool:
    target.sort()
    arr.sort()
    return arr == target

print(canBeEqual(target = [1,2,3,4], arr = [2,4,3,3]))

#1437. Check If All 1's Are at Least Length K Places Away
def kLengthApart(nums: List[int], k: int) -> bool:
    index_list = [index for index, value in enumerate(nums) if value==1]
    for i in range(len(index_list)):
        if i+1 < len(index_list):
            if index_list[i+1]-index_list[i]-1<k:
                return False
    
    return True
      
print(kLengthApart(nums = [1,0,0,1,0,0,1], k = 2))

#1929. Concatenation of Array
def getConcatenation(nums: List[int]) -> List[int]:
    return nums+nums
    
print(getConcatenation([1,2,1]))

#1920. Build Array from Permutation
def buildArray(nums: List[int]) -> List[int]:
    return [nums[nums[i]] for i in range(len(nums))]

#492. Construct the Rectangle
def constructRectangle(area: int) -> List[int]:
    W = int(math.sqrt(area))
    
    while W > 0:
        if area % W == 0:
            L = area // W
            return [L, W]
        W -= 1
        
print(constructRectangle(122122))

#1464. Maximum Product of Two Elements in an Array
def maxProduct(nums: List[int]) -> int:
    max1 = nums.pop(nums.index(max(nums)))-1
    max2 = nums.pop(nums.index(max(nums)))-1
    
    return max1*max2

print(maxProduct([3,7]))