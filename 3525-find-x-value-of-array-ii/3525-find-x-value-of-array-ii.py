class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree_prod = [1] * (4 * n)
        tree_cnt = [[0] * k for _ in range(4 * n)]
        
        def pull(node):
            tree_prod[node] = (tree_prod[2 * node] * tree_prod[2 * node + 1]) % k
            tree_cnt[node] = tree_cnt[2 * node][:]
            lp = tree_prod[2 * node]
            for w in range(k):
                if tree_cnt[2 * node + 1][w]:
                    tree_cnt[node][(lp * w) % k] += tree_cnt[2 * node + 1][w]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree_prod[node] = v
                tree_cnt[node][v] = 1
                return
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            pull(node)

        def update(node, l, r, idx, val):
            if l == r:
                v = val % k
                tree_prod[node] = v
                tree_cnt[node] = [0] * k
                tree_cnt[node][v] = 1
                return
            mid = (l + r) // 2
            if idx <= mid: update(2 * node, l, mid, idx, val)
            else: update(2 * node + 1, mid + 1, r, idx, val)
            pull(node)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree_prod[node], tree_cnt[node]
            mid = (l + r) // 2
            if qr <= mid: return query(2 * node, l, mid, ql, qr)
            if ql > mid: return query(2 * node + 1, mid + 1, r, ql, qr)
            
            l_prod, l_cnt = query(2 * node, l, mid, ql, qr)
            r_prod, r_cnt = query(2 * node + 1, mid + 1, r, ql, qr)
            
            res_prod = (l_prod * r_prod) % k
            res_cnt = l_cnt[:]
            for w in range(k):
                if r_cnt[w]:
                    res_cnt[(l_prod * w) % k] += r_cnt[w]
            return res_prod, res_cnt

        build(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, res_cnt = query(1, 0, n - 1, start, n - 1)
            ans.append(res_cnt[x])
        return ans