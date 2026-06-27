class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        count = 0
        for ch in s:
            width = widths[ord(ch)-ord('a')]
            if count + width > 100:
                lines += 1
                count = width
            else:
                count += width
        return [lines,count]