# Відкриваєм термінал і пишем: py analyze_numbers.py
# Я використовую VSCode

import statistics

def longest_increasing_subsequence(nums):
    longest = []
    current = []
    
    for i in range(len(nums)):
        if not current or nums[i] > current[-1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]
    
    if len(current) > len(longest):
        longest = current
        
    return longest

def longest_decreasing_subsequence(nums):
    longest = []
    current = []
    
    for i in range(len(nums)):
        if not current or nums[i] < current[-1]:
            current.append(nums[i])
        else:
            if len(current) > len(longest):
                longest = current
            current = [nums[i]]
    
    if len(current) > len(longest):
        longest = current
        
    return longest

def process_numbers(filename):
    
    with open(filename, 'r') as file:
        numbers = list(map(int, file.read().split()))
    
    max_number = max(numbers)
    min_number = min(numbers)
    median_number = statistics.median(numbers)
    average = sum(numbers) / len(numbers)
    longest_increasing = longest_increasing_subsequence(numbers)
    longest_decreasing = longest_decreasing_subsequence(numbers)
    
    return {
        "max": max_number,
        "min": min_number,
        "median": median_number,
        "average": average,
        "longest_increasing": longest_increasing,
        "longest_decreasing": longest_decreasing
    }

result = process_numbers('numbers.txt')

print("Максимальне число:", result['max'])
print("Мінімальне число:", result['min'])
print("Медіана:", result['median'])
print("Середнє арифметичне:", result['average'])
print("Найбільша зростаюча послідовність:", result['longest_increasing'])
print("Найбільша зменшувальна послідовність:", result['longest_decreasing'])