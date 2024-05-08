
"""
def blackjack_hand_total(cards: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    mano=0
    numero_assi=0
    for i in cards:
        if i<=10:
            mano= mano+i
        elif i==11:
            numero_assi+=1
    
    if numero_assi >=1:  
        if mano>10:
              mano=mano+numero_assi
        else:
            mano= mano+11+numero_assi-1
            
        
    return mano        





def construct_rectangle(area: float) -> list[float]:
    # elimina il pass e inserisci il codice
    
    
    
    W = int(area**0.5)
        
    while W> 0:
        if area % W == 0:  
            L = area // W  
            return [L, W]   
        W=W-1    
    



def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    # eliminare il pass ed inserire il codice
    
    text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    frequencies = {}
    for word in text.split():
        if word not in stopwords:
            frequencies[word] = frequencies.get(word, 0) + 1
    
    return frequencies



def find_disappeared_numbers(nums: list[int]) -> list[int]:
    # elimina il pass e inserisci il codice
    n = len(nums)
    all_numbers = set(range(1, n+1))  
    nums_set = set(nums)  
    missing_numbers = list(all_numbers - nums_set)  
    return missing_numbers





def is_subsequence(s: str, t: str) -> bool:
    # elimina pass e inserisci il tuo codice
    it = iter(t)   
    return all(char in it for char in s)  




def even_odd_pattern(nums: list[int]) -> list[int]:
   
    pari_nums = []
    disp_nums = []
    
    for n in nums:
        if n % 2 == 0:
            pari_nums.append(n)  
        else:
            disp_nums.append(n)  
    
    return pari_nums + disp_nums


"""


def prime_factors(n: int) -> list[int]:
    
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)
    
    return factors


print(prime_factors(99999999999))