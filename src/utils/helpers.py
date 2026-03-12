def format_confession_message(user, confession):
    return f"**Confession from {user}:**\n{confession}"

def validate_confession_input(confession):
    if len(confession) > 2000:
        return False, "Confession is too long. Please keep it under 2000 characters."
    if not confession.strip():
        return False, "Confession cannot be empty."
    return True, ""