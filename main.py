def find_three_numbers(arr, target):
    n = len(arr)
#
    arr.sort()
    found = False

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

    if found:
        print("Такі числа є")
        print(arr[i], arr[left],  arr[right])
    else:
        print("Таких чисел немає")

arr = [-1000000, 1, 5, 2, 3, 8, 4, 7, 1000000, 1000, 100]
target = 1000
find_three_numbers(arr, target)


