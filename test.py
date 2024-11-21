# from typing import List
# import datetime

# def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
#     count = 0
#     nums.sort()
    
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if lower<=nums[i]+nums[j] and nums[i]+nums[j]<=upper:
#                 count += 1
                
#     return count

# print(countFairPairs([1,7,9,2,5],lower = 11, upper = 11))

# start = datetime.datetime.now()
# print(countFairPairs([1,7,9,2,5],lower = 11, upper = 11))
# end = datetime.datetime.now()
traveling_loc = {
    'Chorsu Bozori':{'time':1.5, 'rating':6},
    'Mustaqillik Maydoni':{'time':0.5, 'rating':7},
    'Kokaldosh Madrasasi':{'time':1, 'rating':8},
    'Minor Masjidi':{'time':0.5, 'rating':8},
    'Hastimom':{'time':1, 'rating':9},
    'Oloy Bozori':{'time':1, 'rating':10},
    'Amir Temur Muzeyi':{'time':2, 'rating':8},
}

def dp(dictionary:dict, time_limit:float):
    max_values = {}
    max_value = {}
    min_time = min([item['time'] for item in dictionary.values()])
    table_per_item = []
    i = min_time
    while i<=time_limit:
        table_per_item.append({i:[]})
        i+=min_time
    
    for i in range(len(table_per_item)):
        best_choices = []
        
        
    print(table_per_item)
    
dp(traveling_loc,4)
