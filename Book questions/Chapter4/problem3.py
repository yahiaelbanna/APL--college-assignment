import re

def validate_phone(phone):
    pattern = r'^\+?\d{1,3}[-]?\d{3}[-]?\d{4}$'
    return bool(re.match(pattern, phone))

phones = ["+1-555-1234", "5551234", "123-456-7890"]
for phone in phones:
    print(f"{phone}: {validate_phone(phone)}")