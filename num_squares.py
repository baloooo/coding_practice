'''
int numSquares(int n) 
    {
        if (n <= 0)
        {
            return 0;
        }
        
        // cntPerfectSquares[i] = the least number of perfect square numbers 
        // which sum to i. Note that cntPerfectSquares[0] is 0.
        vector<int> cntPerfectSquares(n + 1, INT_MAX);
        cntPerfectSquares[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            // For each i, it must be the sum of some number (i - j*j) and 
            // a perfect square number (j*j).
            for (int j = 1; j*j <= i; j++)
            {
                cntPerfectSquares[i] = 
                    min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1);
            }
        }
        
        return cntPerfectSquares.back();


First of all, we created the DP array as usual. This DP array stands for the least number of perfect square numbers for its index. For example DP[13]=2 stands for if you want to decompose 13 into some perfect square numbers, it will contains at least two terms which are 33 and 22.

After the initialization of the DP array. We want to iterate through the array to fill all indices. During each iteration we're actually doing this: dp[i] = 1 + min (dp[i-j*j] for j*j<=i). The formula itself is a little bit hard to understand. Here's an example of how it works: (C#)

Suppose we want to get DP[13] and we already have the previous indices filled.

DP[13] = DP[13-1x1]+DP[1] = DP[12]+1 = 3;

DP[13] = DP[13-2x2]+DP[2x2] = DP[9]+1 = 2;

DP[13] = DP[13-3x3] + DP[3x3] = DP[4] + 1 = 2;

We pick the smallest one which is 2 so DP[13] = 2. Hope it helps.

'''

class Solution(object):
    def numSquares(self, n):
		'''
		Idea is to iterate over nums up untill n and for each num check if the curent num is a perfect square or not.
		If it's a perfect square we only need that num to generate current num but if its not we need a combinations
		of previous perfect squares to get current num.
		Time: O(n*(m^2)) where m is the perfect squares up untill n, and n is the the sum till we want to calculate the number of squares.
		'''
		dp = [0] + [0]*(n)
        perfect_squares = []
        for num in xrange(1, len(dp)):
            if math.sqrt(num) - int(math.sqrt(num)):  # if num is not a perfect square
                min_coins_req = float('inf')
                for perfect_square in perfect_squares:
                    min_coins_req = min(min_coins_req, dp[num-perfect_square])
                dp[num] = 1 + min_coins_req
            else:
                perfect_squares.append(num)
                dp[num] = 1
        return dp[n]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        Possible good explanation too: https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/
        """
        dp = [float('inf')] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in xrange(2, n+1):

            for j in xrange(1, n):
                if j * j > i:
                    break
                '''
                The idea is to take min squares needed to get cur value(index) is min of 
                    (existing value, cur_value - (a perfect square) + min squares for getting that perfect square(which is always 1))
                This is basically dp[i - j*j] + dp[j*j] but we can directly use 1 or populate dp for all
                perfect squares initially in a loop with value 1.
                '''
                dp[i] = min(dp[i], dp[i - j*j] + 1)

        return dp[-1]

if __name__ == '__main__':
    print Solution().numSquares(12)
