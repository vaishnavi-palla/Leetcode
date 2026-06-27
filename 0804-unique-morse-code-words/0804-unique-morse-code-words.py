class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = []
        for word in words:
            res = ""
            for i in word:
                if i == "a":
                    res += ".-"
                elif i == "b":
                    res += "-..."
                elif i == "c":
                    res += "-.-."
                elif i == "d":
                    res += "-.."
                elif i == "e":
                    res += "."
                elif i == "f":
                    res += "..-."
                elif i == "g":
                    res += "--."
                elif i == "h":
                    res += "...."
                elif i == "i":
                    res += ".."
                elif i == "j":
                    res += ".---"
                elif i == "k":
                    res += "-.-"
                elif i == "l":
                    res += ".-.."
                elif i == "m":
                    res += "--"
                elif i == "n":
                    res += "-."
                elif i == "o":
                    res += "---"
                elif i == "p":
                    res += ".--."
                elif i == "q":
                    res += "--.-"
                elif i == "r":
                    res += ".-."
                elif i == "s":
                    res += "..."
                elif i == "t":
                    res += "-"
                elif i == "u":
                    res += "..-"
                elif i == "v":
                    res += "...-"
                elif i == "w":
                    res += ".--"
                elif i == "x":
                    res += "-..-"
                elif i == "y":
                    res += "-.--"
                else:
                    res += "--.."
            trans.append(res)
        return len(set(trans))