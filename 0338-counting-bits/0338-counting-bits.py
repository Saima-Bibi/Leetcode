class Solution(object):
    def countBits(self, num):
        ans = [0] * (num + 1)

        for i in range(num + 1):
            ans[i] = self.rec(i, ans)

        return ans

    def rec(self, num, memo):
        if num == 0:
            return 0
        if num == 1:
            return 1
        if memo[num] != 0:
            return memo[num]

        if num % 2 == 0:
            memo[num] = self.rec(num // 2, memo)
            return memo[num]
        else:
            memo[num] = 1 + self.rec(num // 2, memo)
            return memo[num]

        