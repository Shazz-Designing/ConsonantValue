def solve(s):
    def calculate_value(string):
        return sum(ord(char) - ord('a') + 1 for char in string)

    consonant_substrings = [substr for substr in s.split('a') if substr]
    values = [calculate_value(substr) for substr in consonant_substrings]

    return max(values, default=0)

# Example
result = solve("zodiacs")
print(f"The highest value of consonant substrings is: {result}")