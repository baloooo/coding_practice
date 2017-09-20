# *-* coding: utf-8
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

Example:

    Given “25525511135”,

    return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)
"""
class Solution():
    def __init__(self):
        self.ips = []
        self.cur_ip = ['']*4

    def valid_ips(self, ip_str):
        def valid_ip_addresses(index, octet):
            if octet == 4:
                if index == (len(ip_str) - 1):
                    self.ips.append(self.cur_ip[::])
                return
            for octet_size in xrange(4):
                cur_octet = int(ip_str[index:index+octet_size+1])
                if cur_octet <= 255:
                    self.cur_ip[octet] = ip_str[index:index+octet_size+1]
                    valid_ip_addresses(index+octet_size, octet+1)
        valid_ip_addresses(0, 0)
        return self.ips

if __name__ == '__main__':
    sol = Solution()
    ip_str = '25525511135'
    print sol.valid_ips(ip_str)
