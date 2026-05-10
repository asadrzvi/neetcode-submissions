class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = deque()
        max_len = 0
        
        if not s:
            return 0

        for char in s:
            while char in seen:
                seen.popleft()
            seen.append(char)
            max_len = max(max_len, len(seen))
        return max_len