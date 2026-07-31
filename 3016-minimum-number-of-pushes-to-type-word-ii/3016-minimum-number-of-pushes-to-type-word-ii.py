class Solution:
    def minimumPushes(self, word: str) -> int:
        d = Counter(word)

        d_s = {k:v for k,v in sorted(d.items(), key=lambda item:item[1],reverse=True)}
        # print(d_s)

        counter = res =  0
        level = 1
        for k,v in d_s.items():
            if counter >= 8:
                counter = 0
                level += 1

            counter += 1
            res += (level * d_s[k])
            # print(k,level)
        return res