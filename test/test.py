import unittest

from src.main import rabin_karp_search


class TestRabinKarpSearch(unittest.TestCase):

    def test_single_occurrence(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_multiple_occurrences(self):
        haystack = "abababab"
        needle = "aba"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [0, 2, 4])

    def test_no_occurrence(self):
        haystack = "xyz"
        needle = "abc"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_strings(self):
        haystack = ""
        needle = "abc"
        result = rabin_karp_search(haystack, needle)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
