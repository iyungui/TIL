import ast

def solution(sizes):
    max_width = 0
    max_height = 0
    
    for size in sizes:
        max_width = max(max_width, max(size))
        max_height = max(max_height, max(size))
        
    return max_width * max_height

input_str = input()
sizes = ast.literal_eval(input_str)

print(solution(sizes))
