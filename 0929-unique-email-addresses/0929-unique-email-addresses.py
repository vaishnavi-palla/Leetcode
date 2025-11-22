class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dum = []
        for s in emails:
            start = s.find('+')
            end = s.find('@')
            if start != -1 and end != -1 and start < end:
                dum.append(s[:start] + s[end:])
            else:
                dum.append(s)
        res = set()
        for mail in dum:
            em = ''
            for i in range (len(mail)):
                if mail[i] == '@':
                    em += mail[i:]
                    break
                if mail[i] == '.':
                    pass
                else:
                    em += mail[i]
            res.add(em)
        return len(res)