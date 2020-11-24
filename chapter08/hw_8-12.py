# homework assignment section 8-12
def sandwich(*items):
    print(f"\nYou have ordered a sandwich with:")
    for item in items:
        print(f"- {item}")

sandwich('ham', 'lettuce', 'mayo', 'cheese')
sandwich('turkey', 'cheese', 'pickle', 'mayo')
sandwich('ham', 'turkey', 'pickle', 'mustard', 'cheese', 'lettuce')