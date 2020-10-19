 def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        prev = None
        for c in s:
            if c == prev:
                count += 1
            else:
                prev = c
                count = 1
            max_count = max(max_count, count)
        return max_count
