def solution(numer1, denom1, numer2, denom2):
    numer_add = (denom1*numer2) + (denom2*numer1)
    denom_add = denom1 * denom2
    
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    answer = gcd(numer_add, denom_add)
    
    return [numer_add / answer, denom_add / answer]