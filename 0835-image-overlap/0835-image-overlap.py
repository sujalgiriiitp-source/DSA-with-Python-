class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) ->int:
        n = len(img1)


        img1_ones = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        img2_ones = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        translation_counts = collections.Counter()
        max_overlap = 0

        for r1, c1 in img1_ones:
            for r2, c2 in img2_ones:

                vec = (r2- r1, c2-c1)
                translation_counts[vec] += 1
                max_overlap = max(max_overlap, translation_counts[vec])

        return max_overlap

        
 
        