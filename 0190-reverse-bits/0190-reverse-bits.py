class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res=0
        for i in range(32):
            lsb= n & 1
            reverseLsb= lsb << (31-i)
            res=res | reverseLsb
            n=n>>1
        return res
            