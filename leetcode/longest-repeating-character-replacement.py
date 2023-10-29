import unittest
import collections


def characterReplacement(s: str, k: int) -> int:
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right-1]] += 1
        max_char_n = counts.most_common(1)[0][1]

        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left

class Solution(unittest.TestCase):
    def test_characterReplacement(self):
        self.assertEqual(
            characterReplacement("ABAB", 2), 4
        )
        self.assertEqual(
            characterReplacement("AABABBA", 2), 5
        )
        self.assertEqual(
            characterReplacement("ABBB", 2), 4
        )
        

if __name__ == "__main__":
    unittest.main()