"""

"""


class Solution:
    def get_max_robbery_amount(self, house_list):
        '''
        '''
        self.house_list = house_list
        # return self.rob_houses_w_bruteforce(0)
        return self.rob_houses_w_dp()

    def rob_houses_w_dp_circular(self):
        '''
        Time: O(n)
        Space: O(n)
        '''
        dp = [0] * len(self.house_list)
        for house_index in xrange(len(self.house_list) - 1, -1, -1):
            profit_after_robbing_cur_house = self.house_list[house_index] + (
                dp[house_index + 2] if house_index + 2 < len(self.house_list) else 0)
            profit_after_not_robbing_cur_house = dp[house_index + 1] if house_index + 1 < len(
                self.house_list) else 0
            dp[house_index] = max(profit_after_robbing_cur_house, profit_after_not_robbing_cur_house)
        return dp[0]

    def rob_houses_w_dp(self):
        '''
        Time: O(n)
        Space: O(n)
        '''
        dp = [0] * len(self.house_list)
        for house_index in xrange(len(self.house_list) - 1, -1, -1):
            profit_after_robbing_cur_house = self.house_list[house_index] + (
                dp[house_index + 2] if house_index + 2 < len(self.house_list) else 0)
            profit_after_not_robbing_cur_house = dp[house_index + 1] if house_index + 1 < len(
                self.house_list) else 0
            dp[house_index] = max(profit_after_robbing_cur_house, profit_after_not_robbing_cur_house)
        return dp[0]

    def rob_houses_w_bruteforce(self, house_start_index):
        '''
        Getting profits from right to left
        O(N^2) where N is the len(self.house_list)
        '''
        if house_start_index >= len(self.house_list):
            return 0
        max_profit = 0
        for house_index in xrange(house_start_index, len(self.house_list)):
            # profit when cur house is robbed
            max_profit = max(
                max_profit,
                self.house_list[house_index] + self.rob_houses_w_bruteforce(house_index + 2),
                self.rob_houses_w_bruteforce(house_index + 1)
            )
        return max_profit

    def rob(self, arr):
        """
        Idea:
            f(n) = max(f(n-1), f(n-2) + arr[n])
        """
        max_n_2, max_n_1 = 0, 0
        for cur_num in arr:
            cur_max = max(max_n_1, cur_num + max_n_2)
            max_n_2 = max_n_1
            max_n_1 = cur_max

        return max_n_1

########################################################################################################################

    def get_max_sum(self, nums, cur, start):
        if start >= len(nums):
            return cur
        cur_max = 0
        for idx in xrange(start, len(nums)):
            #cur_max = max(self.get_max_sum(nums, cur + nums[idx], idx+2), self.get_max_sum(nums, cur, idx+1))
            take_cur_val = self.get_max_sum(nums, cur + nums[idx], idx+2)
            skip_cur_val = self.get_max_sum(nums, cur, idx+1)

            cur_max = max(cur_max, take_cur_val, skip_cur_val)
            
        return cur_max


    def rob_recursive(self, nums):
        """
		TLE: recursive slow implementation

        :type nums: List[int]
        :rtype: int
        [2,1,1,2]
        """
        return self.get_max_sum(nums, 0, 0)

if __name__ == '__main__':
    test_cases = [
        ('test1', 'sol1'),
    ]
    for test_case in test_cases:
        res = Solution().my_func(test_case[0])
        if res == test_case[1]:
            print "Passed"
        else:
            print "Failed: Test case: {0} Got {1} Expected {2}".format(
                test_case[0], res, test_case[1])
