def solve(s):
    def calculate_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)

    consonant_substrings = [substr for substr in s.split('a') if substr]
    values = [calculate_value(substr) for substr in consonant_substrings]

    return max(values, default=0)
