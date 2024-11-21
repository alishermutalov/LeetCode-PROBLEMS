# def main():
#     count = 0
#     sum_nums = int(input())
#     nums_str = input()
#     nums_list = nums_str.split(" ")
    
#     seen_once = set()
#     duplicates = set()

#     for num in nums_list:
#         if num in seen_once:
#             duplicates.add(num)
#         else:
#             seen_once.add(num)
#     print(seen_once-duplicates)
#     count = len(seen_once - duplicates)
#     print(count)
    
# main()

import math
x, y = map(int, input().split())


    
n = y // x
count = 0
    
for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a, b = i, n // i
            
            if math.gcd(a, b) == 1:
                count += 2 if a != b else 1
if y % x != 0:
    print(0)
else:   
    print(count) 



