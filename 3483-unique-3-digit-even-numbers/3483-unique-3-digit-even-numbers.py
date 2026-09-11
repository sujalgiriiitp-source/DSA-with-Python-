class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        digit_count = Counter(digits)
        valid_count = 0

        for num in range(100, 1000,2):

            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            needed = Counter([d1, d2, d3])

            if all(digit_count[d] >= needed[d] for d in needed):
                valid_count += 1

        return valid_count

        