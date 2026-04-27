is_logged_in = True

def login_required(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("❌ Please login first!")
    return wrapper

@login_required
def view_profile():
    print("👤 Welcome to your profile!")

@login_required
def view_settings():
    print("⚙️ Here are your settings!")

view_profile()
view_settings()
