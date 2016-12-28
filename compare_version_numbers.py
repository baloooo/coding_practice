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


def version_is_greater(version1, version2):
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
