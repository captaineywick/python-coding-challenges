from typing import List


def find_longest_common_prefix(words: List[str]) -> str:
    # If the list is empty, return an empty string
    if not words:
        return ""

    # Sort the list of strings lexicographically (alphabetical order)
    # The common prefix will be shared between the first and last strings
    words.sort()
    print(f"Sorted words: {words}")  # Debug: see the sorted list

    first_str = words[0]  # First string after sorting
    last_str = words[-1]  # Last string after sorting
    print(
        f"First and last words: {first_str, last_str}"
    )  # Debug: see which two strings are compared
    print(
        f"Length first and last words: {len(first_str), len(last_str)}"
    )  # Debug: length

    common_prefix = []

    # Compare characters of first and last string until mismatch
    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] != last_str[i]:
            print(f"Mismatch: {i}. First: {first_str[i]}. Last: {last_str[i]}")
            break
        common_prefix.append(first_str[i])

    # Join collected characters into the prefix string
    common_prefix = "".join(common_prefix)
    print(f"Common Prefix: {common_prefix}")  # Debug: see the final common prefix
    return common_prefix


sample_words = ["aa", "aab", "acc"]
find_longest_common_prefix(sample_words)  # common should be "a"
