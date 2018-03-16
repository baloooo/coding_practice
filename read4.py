'''
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, res_buf, n):
        """
        https://leetcode.com/problems/read-n-characters-given-read4/discuss/49512/9-line-61ms-AC-python-solution-with-comments

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)

        read4 method reads 4 slots off of NIC(for example) and places it in passed in temp_buf.
        It also returns the number of bytes placed which you can otherwise get from temp_buf.
        I'm using temp_buf just to enhance my understanding.
        """
        idx = 0
        while True:
            buf4 = [""] * 4
            cur_read_len = min(read4(buf4), n - idx)
            for i in xrange(cur_read_len):
                res_buf[idx] = buf4[i]
                idx += 1
            # cur read character less than 4 means end of file reached. OR desired length of chars are read.
            if cur_read_len != 4 or n == idx:
                return idx

    '''
    difference is:
    Call once: Assume you are always going to read from the start of the file/bufer.
    Call multiple times: Start reading from where you left off. This means that you have to
    store the last place (ptr) where you stopped and store the read but uncopied bytes to the buffer.

    I think code wise it should be same for both the cases except that the pointer from where
    to start reading the internal read4 buffer, the internal read4 buffer itself and the number
    of bytes to be read from that buffer, need to be stored in the 2nd case.
    '''
    def read_multiple_times(self, res_buf, n):
        pass
