# Problem: https://leetcode.com/problems/k-closest-points-to-origin/


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distanceDict = {}
        distanceList = []
        for x in points:
            u = x[0]**2 + x[1]**2
            distanceDict[u] = x
            distanceList.append(u)
        distanceList.sort()
        return [distanceDict[ distanceList[i] ] for i in range(K)]

solution = Solution()
points = [[1,3],[-2,2]]
K = 1

output = solution.kClosest(points, K)
print(output)
