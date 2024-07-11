def is_palindrome_possible(test_cases):
    results = []
    
    for case in test_cases:
        n, strings = case
        
        # Find the longest string
        max_len = max(len(s) for s in strings)
        
        # Find all strings that are the longest
        longest_strings = [s for s in strings if len(s) == max_len]
        
        if len(longest_strings) < 2:
            # If there's only one longest string, we cannot have a prefix and a suffix
            results.append("NO")
            continue
        
        prefix = longest_strings[0]
        suffix = longest_strings[1]
        
        if prefix == suffix[::-1]:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    strings = input().split()
    test_cases.append((n, strings))

# Processing each test case
results = is_palindrome_possible(test_cases)

# Printing results
for result in results:
    print(result)
