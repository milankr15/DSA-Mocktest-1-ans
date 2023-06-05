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


////Question--1 //////////

def moveZeroes(nums):
    # Initialize a pointer to keep track of the position to insert non-zero elements
    insert_pos = 0

    # Traverse the array
    for i in range(len(nums)):
        # If the current element is non-zero
        if nums[i] != 0:
            # Move the non-zero element to the current insert position
            nums[insert_pos] = nums[i]
            # Increment the insert position
            insert_pos += 1

    # Fill the remaining positions with zeroes
    for i in range(insert_pos, len(nums)):
        nums[i] = 0

    return nums
