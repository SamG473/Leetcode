class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        counts = {}
4        for c in magazine:
5            if c in counts:
6                counts[c] += 1
7            else:
8                counts[c] = 1
9
10        note_counts = {}
11        for c in ransomNote:
12            if c in note_counts:
13                note_counts[c] += 1
14            else:
15                note_counts[c] = 1
16
17        for c in note_counts:
18            if c not in counts or note_counts[c] > counts[c]:
19                return False
20        return True
