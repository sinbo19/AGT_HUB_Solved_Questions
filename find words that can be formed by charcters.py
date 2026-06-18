lass Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0

        for word in words:
            ok = True

            for ch in word:
                if word.count(ch) > chars.count(ch):
                    ok = False
                    break

            if ok:
                total += len(word)

        return total  
