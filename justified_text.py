# -*- coding: utf-8 -*-
"""
Justified Text
Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as
you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is
inserted between words.

Your program should return a list of strings, where each string represents a
single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""
def justify_text2(words, max_width):
    """
    shorter and more precise version.
    https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    res, num_of_letters, cur = [], 0, []
    for w in words:
        # add len(cur) as this would ensure we can have atleast spaces equal to words within max_width
        if num_of_letters + len(w) + len(cur) > max_width:
            # Assign spaces in round robin fashion
            for i in range(max_width - num_of_letters):
                # The "or 1" part is for dealing with the edge case len(cur) == 1.
                # len(cur)-1 makes sure last char is never given a space since lines are not supposed to end with spaces.
                # appends a space after every string in cur array
                cur[i % (len(cur) -1 or 1)] += ' '
            res.append(''.join(cur))
            num_of_letters = 0
            cur = []
        cur += [w]
        num_of_letters += len(w)
    # puts one space after every word in current and then puts all remaining spaces at last, ljust fills in spaces for remaining places
    return res + [' '.join(cur).ljust(max_width)]


def justify_text(word_list, line_width):
    # optimize this
    if len(word_list) == 0:
        return []
    cur_line = []
    cur_word_len = 0
    justified_lines = []
    spaces_per_word = 1
    extra_spaces = 0
    for word in word_list:
        # Initially we try to stuff one spaces per word
        if (cur_word_len+len(word)+len(cur_line)) <= line_width:
            cur_word_len += len(word)
            cur_line.append(word)
        else:
            if len(cur_line)>1:
                spaces_per_word = (line_width-cur_word_len)/(len(cur_line)-1)
                extra_spaces = (line_width-cur_word_len) % (len(cur_line)-1)
            spaced_cur_line = []
            for cur_word in cur_line[:-1]:
                spaced_cur_line.append(cur_word)
                spaced_cur_line.append(' '*spaces_per_word)
                if extra_spaces:
                    spaced_cur_line.append(' ')
                    extra_spaces -= 1
            if len(cur_line)==1:
                spaced_cur_line.append(cur_line[-1]+' '*(line_width-len(cur_line[-1])))
            else:
                spaced_cur_line.append(cur_line[-1])
            justified_lines.append(spaced_cur_line)
            cur_line = [word]
            cur_word_len = len(word)
            spaces_per_word = 1
    if not justified_lines and not cur_line:
        return []
    # Add the last word
    justified_lines.append(' '.join(cur_line))
    justified_lines[-1]+=(' '*(line_width-len(justified_lines[-1])))
    res = []
    for each in justified_lines:
        res.append(''.join(each))
    return res

if __name__ == '__main__':
    # word_list = ["This", "is", "an", "example", "of", "text", "justification.", "But", "sometimes", "justification", "is", "not", "so", "good"]
    # line_width = 16
    # word_list = ["This", "is", "an", "example", "of", "text", "justification."]
    # line_width = 16
    # word_list = [ "" ]
    # line_width=10
    word_list =  [ "am", "fasgoprn", "lvqsrjylg", "rzuslwan", "xlaui", "tnzegzuzn", "kuiwdc", "fofjkkkm", "ssqjig", "tcmejefj", "uixgzm", "lyuxeaxsg", "iqiyip", "msv", "uurcazjc", "earsrvrq", "qlq", "lxrtzkjpg", "jkxymjus", "mvornwza", "zty", "q", "nsecqphjy" ]
    line_width = 14
    print justify_text(word_list, line_width)
