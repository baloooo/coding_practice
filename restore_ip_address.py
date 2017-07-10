"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
https://leetcode.com/problems/restore-ip-addresses/#/description
"""
class Solution(object):
    def is_valid(self, a, b, c, d):
        for cur_byte in [a, b, c, d]:
            if len(cur_byte)>3 or len(cur_byte) == 0 or int(cur_byte)>255 or (cur_byte[0] == '0' and len(cur_byte)>1):
                return False
        return True

    def restoreIpAddresses(self, ip):
        """
        :type s: str
        :rtype: List[str]
        """
        possible_ips = []
        for i in range(1, 4):
            if i+2 > len(ip):
                break
            for j in range(i+1, i+4):
                if j+1 > len(ip):
                    break
                for k in range(j+1, j+4):
                    if k > len(ip):
                        break
                    a, b, c, d = ip[:i], ip[i: j], ip[j: k], ip[k: len(ip)]
                    print a, b, c, d
                    if self.is_valid(a, b, c, d):
                        possible_ips.append('.'.join([a, b, c, d]))
        return possible_ips
        
