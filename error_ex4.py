class AgeError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise AgeError("Age negative aagilla!")
    elif age > 150:
        raise AgeError("Age bahala jaasti!")
    else:
        print(f"✅ Valid age: {age}")

try:
    validate_age(25)
    validate_age(-5)

except AgeError as e:
    print(f"❌ Error: {e}") 
