class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        R = len(robot)
        F = len(factory)

        dp = [[float('inf')] * (F + 1) for _ in range(R + 1)]

        for j in range(F + 1):
            dp[0][j] = 0

        for j in range(1, F + 1):
            pos, limit = factory[j - 1]
            for i in range(1, R + 1):

                dp[i][j] = dp[i][j-1]

                cost = 0

                max_k = min(i, limit)

                for k in range(1, max_k + 1):
                    cost += abs(robot[i - k] - pos)

                    if dp[i - k][j - 1] != float('inf'):
                        dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + cost)

         
        return dp[R][F]
        