class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.max_len = [0] * (4 * self.n)
        self.left_char = [''] * (4 * self.n)
        self.right_char = [''] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def _merge(self, tree_idx: int, l_idx: int, r_idx: int, mid: int, l: int, r: int):
        left_child = 2 * tree_idx
        right_child = 2 * tree_idx + 1

        self.left_char[tree_idx] = self.left_char[left_child]
        self.right_char[tree_idx] = self.right_char[right_child]

        left_size = mid - l + 1
        right_size = r - mid

        # Base max
        self.max_len[tree_idx] = max(self.max_len[left_child], self.max_len[right_child])

        # Cross boundary check
        if self.right_char[left_child] == self.left_char[right_child]:
            cross = self.suff_len[left_child] + self.pref_len[right_child]
            self.max_len[tree_idx] = max(self.max_len[tree_idx], cross)

        # Prefix length
        self.pref_len[tree_idx] = self.pref_len[left_child]
        if self.pref_len[left_child] == left_size and self.right_char[left_child] == self.left_char[right_child]:
            self.pref_len[tree_idx] += self.pref_len[right_child]

        # Suffix length
        self.suff_len[tree_idx] = self.suff_len[right_child]
        if self.suff_len[right_child] == right_size and self.right_char[left_child] == self.left_char[right_child]:
            self.suff_len[tree_idx] += self.suff_len[left_child]

    def build(self, tree_idx: int, l: int, r: int):
        if l == r:
            ch = self.s[l]
            self.pref_len[tree_idx] = 1
            self.suff_len[tree_idx] = 1
            self.max_len[tree_idx] = 1
            self.left_char[tree_idx] = ch
            self.right_char[tree_idx] = ch
            return

        mid = (l + r) // 2
        self.build(2 * tree_idx, l, mid)
        self.build(2 * tree_idx + 1, mid + 1, r)
        self._merge(tree_idx, 2 * tree_idx, 2 * tree_idx + 1, mid, l, r)

    def update(self, tree_idx: int, l: int, r: int, pos: int, ch: str):
        if l == r:
            self.s[pos] = ch
            self.left_char[tree_idx] = ch
            self.right_char[tree_idx] = ch
            return

        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * tree_idx, l, mid, pos, ch)
        else:
            self.update(2 * tree_idx + 1, mid + 1, r, pos, ch)

        self._merge(tree_idx, 2 * tree_idx, 2 * tree_idx + 1, mid, l, r)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, len(s) - 1, idx, ch)
            ans.append(st.max_len[1])
        return ans