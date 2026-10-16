class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree_sum = [0] * (4 * n)
        self.tree_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1

            self._apply(left_child, start, mid, val)
            self._apply(right_child, mid + 1, end, val)

            self.lazy[node] = 0

    def _apply(self, node, start, end, val):
        length = end - start + 1
        val %= self.MOD

        self.tree_sq[node] = (
            self.tree_sq[node]
            + 2 * val * self.tree_sum[node]
            + length * val * val
        ) % self.MOD

        self.tree_sum[node] = (self.tree_sum[node] + length * val) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            self._apply(node, start, end, val)
            return

        self._push(node, start, end)
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        if l <= mid:
            self.update(left_child, start, mid, l, r, val)
        if r > mid:
            self.update(right_child, mid + 1, end, l, r, val)

        self.tree_sum[node] = (self.tree_sum[left_child] + self.tree_sum[right_child]) % self.MOD
        self.tree_sq[node] = (self.tree_sq[left_child] + self.tree_sq[right_child]) % self.MOD


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        st = SegmentTree(n)
        last_pos = {}
        total_ans = 0

        for i, val in enumerate(nums):
            prev_idx = last_pos.get(val, -1)
            
            st.update(1, 0, n - 1, prev_idx + 1, i, 1)
           
            total_ans = (total_ans + st.tree_sq[1]) % MOD
            
            last_pos[val] = i

        return total_ans