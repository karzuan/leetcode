# Input: s = "the sky is blue"
# Output: "blue is sky the"

def reverseWords(self, s: str) -> str:
    my_list = s.split()
    #print(my_list)
    result = []
    n = len(my_list)
    for i in range(n):
        result.append(my_list[n-1])
        n = n-1
    #print(result)
    result = ' '.join(result)
    print(result)
    return result


reverseWords(None, "the  sky is blue")