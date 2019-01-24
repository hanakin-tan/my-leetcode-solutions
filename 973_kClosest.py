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
        for point in points:
            u = point[0]**2 + point[1]**2
            distanceDict[u] = point
            distanceList.append(u)
        distanceList.sort()
        return [distanceDict[ distanceList[i] ] for i in range(K)]

solution = Solution()
points = [[1,3],[-2,2]]
K = 1

output = solution.kClosest(points, K)
print(output)
