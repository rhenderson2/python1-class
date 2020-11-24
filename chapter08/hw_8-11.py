# homework assignment section 8-11
def send_messages(texts, sent_texts):
    while texts:
        current_text = texts.pop()
        print(f"\nTexting: {current_text}")
        sent_texts.append(current_text)

texts = ['This is the first text',
         'this is text 2',
         'and this is text three']
sent_texts = []

send_messages(texts[:], sent_texts)
print('\n')
print(texts)
print(sent_texts)