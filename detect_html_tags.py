"""
https://www.hackerrank.com/challenges/detect-html-tags
"""
import re

regex = r"<\s*[a-zA-Z]{1,3}\s*>*"
n = int(raw_input().strip())
tags = set()
final_tags = []
for i in xrange(n):
    inp = raw_input().strip()
    tag_matches = re.finditer(regex, inp)
    for match in tag_matches:
        tags.add(re.sub(r'[<|>|\\\s]', '', match.group()))
for tag in tags:
    final_tags.append(tag)
print ';'.join(sorted(final_tags))
