import unittest


def find_three_numbers(arr, target):
    n = len(arr)

    arr.sort()
    found = False
#
    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                found = True
                break
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        if found:
            break

    return found


class TestFindThreeNumbers(unittest.TestCase):

    def test_case_1(self):
        arr = [1, 2, 4]
        target = 7
        result = find_three_numbers(arr, target)
        self.assertTrue(result)

    def test_case_2(self):
        arr = [1, 2, 4]
        target = 8
        result = find_three_numbers(arr, target)
        self.assertFalse(result)

    def test_case_3(self):
        arr = [3, 5, 10, 12]
        target = 20
        result = find_three_numbers(arr, target)
        self.assertTrue(result)

    def test_case_4(self):
        arr = [3, 5, 10, 12]
        target = 7
        result = find_three_numbers(arr, target)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
