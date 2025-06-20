import re

def normalize_phone(phone_number):
    symbol = re.sub(r'[^\d+]', '', phone_number)
    add_plus = re.sub(r'\b380(\d{9})\b', r'+380\1', symbol)
    add_num = re.sub(r'(?<!\d)(?<!380)(?<!\+)(\d{9})(?!\d)', r'+380\1', add_plus)
    deleted_plus = re.sub(r'\++', '+', add_num)
    add_num2 = re.sub(r'\b0(\d{9})\b', r'+38' + r'0\1', deleted_plus)
    return add_num2


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)