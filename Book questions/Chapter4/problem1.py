import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.(com|org|edu)$'
    return bool(re.match(pattern, email))

emails = ["user@example.com", "bad-email", "test@domain.org"]
for email in emails:
    print(f"{email}: {validate_email(email)}")