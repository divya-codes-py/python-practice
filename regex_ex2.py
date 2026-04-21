import re

def validate_phone(number):
    pattern = r'^[6-9][0-9]{9}$'
    if re.match(pattern, number):
        print(f"✅ '{number}' — Valid phone number!")
    else:
        print(f"❌ '{number}' — Invalid phone number!")

validate_phone("9876543210")
validate_phone("1234567890")
validate_phone("8123456789")
