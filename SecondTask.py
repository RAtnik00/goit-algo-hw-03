import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []
    
    result = set()
    while len(result) < quantity:
        num = random.randint(min, max)
        result.add(num)

    return sorted(result)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)