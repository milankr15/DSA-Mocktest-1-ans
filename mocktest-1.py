/// SOLUTION OF DSA MOCK TEST 1 ANS//////

///QUESTION--2/////

def firstUniqChar(s):
    char_counts = {}  # Dictionary to store character counts

    # Count the occurrences of each character in the string
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Find the index of the first non-repeating character
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1 


# Test cases
print(firstUniqChar("leetcode"))  # Output: 0
print(firstUniqChar("loveleetcode"))  # Output: 2
print(firstUniqChar("aabb"))  # Output: -1

///final output: 0 , 2 , -1


////End//////////
