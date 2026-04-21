import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f"✅ '{email}' — Valid email!")
    else:
        print(f"❌ '{email}' — Invalid email!")

validate_email("divya@gmail.com")
validate_email("divya@.com")
validate_email("divya123@yahoo.in")
