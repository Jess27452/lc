class Solution:
    def encode(self, strs):
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, string):
        res = []
        i = 0

        while i < len(string):
            j = i

            while string[j] != "#":
                j += 1

            length = int(string[i:j])

            res.append(string[j + 1 : j + 1 + length])

            i = j + 1 + length

        return res