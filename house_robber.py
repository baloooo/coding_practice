"""

"""


class Solution:
    def rob_bf(self, root):
        """
        The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

        Determine the maximum amount of money the thief can rob tonight without alerting the police.

        Example 1:

        Input: [3,2,3,null,3,null,1]

             3
            / \
           2   3
            \   \
             3   1

        Output: 7
        Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
        Example 2:

        Input: [3,4,5,1,3,null,1]

             3
            / \
           4   5
          / \   \
         1   3   1

        Output: 9
        Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

        house robber 3
        """
        self.house_to_max_robable_amount = {}
        max_robable_amounts = self.get_max_robable_amount_dp2(root, True)
        return max(max_robable_amounts)
        # return self.get_max_robable_amount_dp1(root, True)
        # return self.get_max_robable_amount_bf(root)

    def get_max_robable_amount_dp1(self, root, can_rob_cur):
        '''
        n being total number of houses
        Time: O(n)
        Space: O(2n) = O(n)
        Idea here is to cache node to maximum amount that can be robbed with and without taking cur node(house).
        And then readily use the precomputed value for later iterations.
        '''

        if root is None:
            return 0
        if (root, can_rob_cur) in self.house_to_max_robable_amount:
            return self.house_to_max_robable_amount[(root, can_rob_cur)]
        max_robable_amount = 0
        if can_rob_cur:
            max_robable_amount = root.val + self.get_max_robable_amount(root.left, False) + self.get_max_robable_amount(root.right, False)

        self.house_to_max_robable_amount[(root, can_rob_cur)] = max(max_robable_amount,
                                 self.get_max_robable_amount(root.left, True) + self.get_max_robable_amount(root.right, True))
        return self.house_to_max_robable_amount[(root, can_rob_cur)]

    def get_max_robable_amount_dp2(self, root, can_rob_cur):
        '''
        n being total number of houses
        Time: O(n)
        Space: O(2n) = O(n)
        Idea here is to cache node to maximum amount that can be robbed with and without taking cur node(house).
        And then readily use the precomputed value for later iterations.
        '''

        if root is None:
            return 0
        # if (root, can_rob_cur) in self.house_to_max_robable_amount:
        #     return self.house_to_max_robable_amount[(root, can_rob_cur)]
        max_robable_amount = 0
        if can_rob_cur:
            max_robable_amount = root.val + self.get_max_robable_amount(root.left, False) + self.get_max_robable_amount(root.right, False)

        self.house_to_max_robable_amount[(root, can_rob_cur)] = max(max_robable_amount,
                                                                    self.get_max_robable_amount(root.left, True) + self.get_max_robable_amount(root.right, True))
        return self.house_to_max_robable_amount[(root, can_rob_cur)]

    def get_max_robable_amount_bf(self, root, can_rob_cur):
        if root is None:
            return 0
        max_robable_amount = 0
        if can_rob_cur:
            max_robable_amount = root.val + self.get_max_robable_amount_bf(root.left, False), self.get_max_robable_amount_bf(root.right, False)

        max_robable_amount = max(max_robable_amount,
                                 self.get_max_robable_amount_bf(root.left, True) + self.get_max_robable_amount_bf(root.right, True))

        return max_robable_amount

    ###############
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
