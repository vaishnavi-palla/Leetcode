class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        for word in sentence.split():
            if word.isalpha():
                res+=1
            
            else:
                req = False
                h,c,f,e=0,0,0,0
                for i in range(len(word)):
                    if word[i] == '-':
                        if i == len(word)-1:
                            req = False
                            break
                        else:
                            h += 1
                            if word[i-1].isalpha() and word[i+1].isalpha() and h<=1 and i != (len(word))-1:
                                req = True
                            else:
                                req = False
                                break
                    if word[i] == ',':
                        c += 1
                        if i == len(word)-1 and c <= 1:
                            req = True
                        else:
                            req = False
                            break
                    if word[i] == '.' :
                        f += 1
                        if i == len(word)-1 and f <= 1:
                            req = True
                        else:
                            req = False
                            break
                    if word[i] == '!' :
                        e += 1
                        if i == len(word)-1 and e <= 1:
                            req = True
                        else:
                            req = False
                            break
                    if word[i] in '0987654321':
                        req = False
                        break
                if req == True:
                    res+=1
        return res