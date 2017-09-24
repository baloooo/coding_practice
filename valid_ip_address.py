# *-* coding: utf-8
"""
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.
"""
import string

class Solution(object):
    def valid_ipv4(self, IP):
        octets = IP.split('.')
        if len(octets) == 4:
            try:
                # Notice here we take the entire number for comparison b/w 0 and 255, whereas in IPv6
                # we have to take individual chars and see if they are in range
                return all([str(int(octet)) == octet and (0 <= int(octet) <= 255) for octet in octets])
            except ValueError:
                # can be raised for 172.10.10.abc as int(abc) is invalid
                return False

    def valid_ipv6(self, IP):
        octets = IP.split(':')
        # IPv6 has 8 octets in total
        if len(octets) == 8:
	    for octet in octets:
                # Each octet in IPv6 has exactly 4 hex digits
		if 1 <= len(octet) <= 4:
                    # Compare each digit contrary to entire number we used to in IPv4
		    for c in octet:
			if c not in string.hexdigits:
			    return False
		else:
		    return False
            return True	
            # return True if all([1 <= len(octet) <= 4 and octet in string.hexdigits for octet in octets]) else False

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        Idea: https://discuss.leetcode.com/topic/103614/python-easy-understand-solution
        """
        if self.valid_ipv4(IP):
            return "IPv4"

        if self.valid_ipv6(IP):
            return "IPv6"

        return "Neither"

if __name__ == '__main__':
    ip_str = '172.16.254.1'
    ip_str = '2001:0db8:85a3:0:0:8A2E:0370:7334'
    ip_str = '256.256.256.256'
    ip_str = '0.0.0.a'
    print Solution().validIPAddress(ip_str)
