class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        window = len(p)
        count_s = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        count_p = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
        for i in p:
            count_p[i] += 1
        for j in range(len(s)):
            count_s[s[j]] += 1
            if j >= window:
                left = s[j - window]
                count_s[left] -= 1
            if count_s == count_p:
                result.append(j-window+1)

        return result