import re

def find_largest_number(s):
    # Find all sequences of digits in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert the sequences of digits to integers
    numbers = [int(num) for num in numbers]
    
    # Return the largest number found
    if numbers:
        return max(numbers)
    else:
        return None

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    n = int(data[0])  # Read the number of test cases
    
    results = []
    for i in range(1, n + 1):
        line = data[i]
        largest_number = find_largest_number(line)
        results.append(largest_number)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
