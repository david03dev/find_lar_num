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
    
    # Read input
    data = input().strip()
    
    # Find the largest number in the input string
    largest_number = find_largest_number(data)
    
    # Print the result
    if largest_number is not None:
        print(largest_number)
    else:
        print("No numbers found")

if __name__ == "__main__":
    main()
