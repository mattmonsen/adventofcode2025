#!/usr/bin/env python3

example = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''

example = open("day_7_input.txt").read()

def find_operations(nums, target):
    def backtrack(index, current_result, expression):
        # Base case: if all numbers are used
        if index == len(nums):
            if current_result == target:
                return expression
            return None

        # Recursive case: try all operations
        next_num = nums[index]
#        for op in ['+', '-', '*', '/']:
        for op in ['+', '*']:
            # Avoid division by zero
            if op == '/' and next_num == 0:
                continue
            
            # Calculate the new result based on the operation
            if op == '+':
                new_result = current_result + next_num
            elif op == '-':
                new_result = current_result - next_num
            elif op == '*':
                new_result = current_result * next_num
            elif op == '/':
                new_result = current_result / next_num
            
            # Recur to the next index
            result = backtrack(index + 1, new_result, expression + [op])
            if result:  # If a solution is found, return it
                return result
        
        # If no solution found, return None
        return None

    # Start backtracking from the first number
    if not nums:
        return None
    return backtrack(1, nums[0], [])

# Example usage
#nums = [3, 4, 5]
#target = 17
nums = [10, 19]
target = 190
operations = find_operations(nums, target)
if operations:
    print(f"Operations to reach {target}: {operations}")
else:
    print("No solution found.")

sum = 0

for line in example.splitlines():
    target, nums = line.split(":")
    nums = [int(x) for x in nums.lstrip().split(" ")]
    target = int(target)
    operations = find_operations(nums, target)
    if operations:
        sum += target
        print(f"Operations to reach {target}: {operations}")
    else:
        print("No solution found.")

print(f"Sum is: {sum}")
