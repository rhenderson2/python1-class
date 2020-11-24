# homework assignment section 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('rick', 'henderson',
                            personality_trait01='thinker',
                            personality_trait02='fun - loving',
                            personality_trait03='steady')
print(user_profile)