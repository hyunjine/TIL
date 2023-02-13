def solution(numer1, denom1, numer2, denom2):
    top = (numer1 * denom2) + (numer2 * denom1)
    bot = denom1 * denom2
    for i in range(2, min(top, bot)):
        while top % i == 0 and bot % i == 0: 
            top //= i
            bot //= i
    return [top, bot]