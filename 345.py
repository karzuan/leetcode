def reverseVowels(self, s: str) -> str:
        #'a', 'e', 'i', 'o', and 'u'
        vvls = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        my_vvls = []
        word_splitted = []
        n = len(s)
        for i in range(n):
            word_splitted.append(s[i])
            if s[i] in vvls:
                my_vvls.append(s[i])
        for i in range(n):
            if s[i] in vvls:
                word_splitted[i] = my_vvls.pop()
        #print(word_splitted)
        word_splitted = ''.join(word_splitted)
        print(word_splitted)


reverseVowels(None, 'OmgifEna')