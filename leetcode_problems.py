#709 To lower case

def to_lower(s):
    pass
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