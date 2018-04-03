# -*- coding: utf-8 -*-
"""
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits
and the . character.
The . character does not represent a decimal point and is used to separate
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""
import pytest

class Solution():
    def compare_subversions(self, substr_va, substr_vb):
        if len(substr_va) > len(substr_vb):
            return 1
        elif len(substr_va) < len(substr_vb):
            return -1
        for cha, chb in zip(substr_va, substr_vb):
            if cha > chb:
                return 1
            elif cha < chb:
                return -1

        return 0

    def isgreater(self, va, vb):
        '''
        https://www.geeksforgeeks.org/compare-version-numbers-large-inputs-allowed/
        Time: O(2n) => O(n)
        returns:
            1 if va > vb
           -1 if va < vb
            0 if va = vb
        '''
        i = j = 0
        while i < len(va) or j < len(vb):
            # Ignores any leading zeroes or unwanted chars
            # while i < len(va) and (va[i] == '0' or va[i] == '.'):
            while i < len(va) and (va[i] == '0'):
                i += 1
            while j < len(vb) and (vb[j] == '0'):
                j += 1
            # Find next valid version number substring
            start = i
            while i < len(va) and va[i] != '.':
                i += 1
            substr_va = va[start : i]
            i += 1

            start = j
            while j < len(vb) and vb[j] != '.':
                j += 1
            substr_vb = vb[start : j]
            j += 1

            # compare subversions
            '''
            This if-else is b'coz we're skipping all leading zeroes (as they contribute to comparison) but
            if that is all what there is to a version number we'll have an empty string, therefore we
            replace it with a valid string ('0').
            '''
            res = self.compare_subversions(substr_va if substr_va else '0', substr_vb if substr_vb else '0')
            if res:
                return res
        return 0


class TestSolution(object):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    @pytest.mark.parametrize("args, result", [
        (['1', '01'], 0),
        (['1.10', '1.20'], -1),
        (['3.10', '2.20'], 1),
        (['1.10', '2.20'], -1),
        (['3.10', '2.20'], 1),
        (['1.30', '0.40'], 1),
        (['0.30', '0.30'], 0),
        (['0.00', '0.00'], 0),
        (['1.1.1.1', '1.1.1'],1),
        (['', ''], 0),
        ])
    def test_task(self, args, result):
        sol = Solution()
        assert sol.isgreater(*args) == result

def version_is_greater_bruteforce(version1, version2):
    '''
    There're couple of cons for this approach like:
    This approach converts individual version number to int which can be a very large
    num therefore overflow int capacity(strictly speaking not in python but you get the point ...)
    Lot of iterations over versions which can be minimized.
    '''
    ver1 = [int(x) for x in version1.split('.')]
    ver2 = [int(x) for x in version2.split('.')]
    v1_len = len(ver1)
    v2_len = len(ver2)
    if not v1_len and not v2_len:
        return 0
    if not v1_len:
        return -1
    if not v2_len:
        return 1
    for i, j in zip(ver1, ver2):
        if i > j:
            return 1
        if i < j:
            return -1
    else:
        if v1_len == v2_len:
            return 0
        if v1_len > v2_len:
            if v2_len+1 == v1_len and ver1[-1] == 0:
                return 0
            return 1
        else:
            if v1_len+1 == v2_len and ver1[-1] == 0:
                return 0
            return -1

if __name__ == '__main__':
    version1 = '1.0'
    version2 = '1'
    print version_is_greater(version1, version2)
