# intersection of two arrays II
import pdb


class Solution:
    def intersect(self, nums1, nums2):
        hash_1 = {}
        for n_1 in nums1:
            if n_1 not in hash_1:
                hash_1[n_1] = 1
            else:
                hash_1[n_1] += 1
        hash_2 = {}
        for n_2 in nums2:
            if n_2 not in hash_2:
                hash_2[n_2] = 1
            else:
                hash_2[n_2] += 1
        interset = [k for k in hash_1.keys() if k in hash_2.keys()]
        results = []
        for dup in interset:
            dup_num = min(hash_1[dup], hash_2[dup])

            results.extend([dup] * dup_num)

        print(results)
        return results


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s.intersect(nums1, nums2)