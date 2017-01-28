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


def justify_text(word_list, char_len):
    cur_line = []
    cur_word_len = 0
    justified_lines = []
    spaces_per_word = 1
    for word in word_list:
        # Initially we try to stuff one spaces per word
        if (cur_word_len+len(word)+len(cur_line)) <= char_len:
            cur_word_len += len(word)
            cur_line.append(word)
        else:
            spaces_per_word = (char_len-cur_word_len)/(len(cur_line)-1)
            extra_spaces = (char_len-cur_word_len) % (len(cur_line)-1)
            spaced_cur_line = []
            for cur_word in cur_line[:-1]:
                spaced_cur_line.append(cur_word)
                spaced_cur_line.append(' '*spaces_per_word)
                if extra_spaces:
                    spaced_cur_line.append(' ')
                    extra_spaces -= 1
            spaced_cur_line.append(cur_line[-1])
            justified_lines.append(spaced_cur_line)
            cur_line = [word]
            cur_word_len = len(word)
            spaces_per_word = 1
    # Add the last word
    justified_lines.append(''.join(cur_line))
    res = []
    for each in justified_lines:
        res.append(''.join(each))
    return res

if __name__ == '__main__':
    word_list = ["This", "is", "an", "example", "of", "text", "justification.", "But", "sometimes", "justification", "is", "not", "so", "good"]
    char_len = 16
    # word_list = []
    # char_len = 1
    print justify_text(word_list, char_len)
