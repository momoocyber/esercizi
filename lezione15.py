def anagram(s: str, t: str) -> bool:
    
    s=s.lower()
    t=t.lower()
    if len(s)== len(t):
        for i in t:
            if i in s:
                return True
            else:
                return False
    else:
        return False