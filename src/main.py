def rabin_karp_search(haystack, needle):
    if not haystack or not needle:
        return []

    prime = 101

    def calculate_hash(string):
        hash_value = 0
        for char in string:
            hash_value = (hash_value * prime + ord(char)) % (10 ** 9 + 9)
        return hash_value

    m, n = len(haystack), len(needle)

    needle_hash = calculate_hash(needle)
    haystack_hash = calculate_hash(haystack[:n])

    indices = []

    for i in range(m - n + 1):
        if haystack_hash == needle_hash and haystack[i:i + n] == needle:
            indices.append(i)

        if i < m - n:
            haystack_hash = (haystack_hash - ord(haystack[i]) * pow(prime, n - 1, 10 ** 9 + 9)) % (10 ** 9 + 9)
            haystack_hash = (haystack_hash * prime + ord(haystack[i + n])) % (10 ** 9 + 9)
            haystack_hash = (haystack_hash + (10 ** 9 + 9)) % (10 ** 9 + 9)

    return indices


haystack = "prompompomxl"
needle = "pom"
result = rabin_karp_search(haystack, needle)
print(f"Індекси входжень '{needle}' в '{haystack}': {result}")
