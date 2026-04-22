import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("❌ Min 8 characters irali!")
    if not re.search(r'[A-Z]', password):
        errors.append("❌ Ondu uppercase letter irali!")
    if not re.search(r'[0-9]', password):
        errors.append("❌ Ondu number irali!")
    if not re.search(r'[@#$!]', password):
        errors.append("❌ Ondu special character irali (@#$!)!")

    if not errors:
        print(f"✅ '{password}' — Strong password!")
    else:
        print(f"❌ '{password}' — Weak password!")
        for error in errors:
            print(f"   {error}")

validate_password("Divya@123")
validate_password("divya123")
validate_password("Div@1")
