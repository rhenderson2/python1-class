# homework assignment section 8-10
# List texts and empty list of sent texts.
texts = ['This is the first text',
         'this is text 2',
         'and this is text three']
sent_texts = []

# Simulate sending each text until all are sent.
# Move each text from texts to sent_texts after texting.
def send_messages(texts, sent_texts):
    while texts:
        current_text = texts.pop()
        print(f"\nTexting: {current_text}")
        sent_texts.append(current_text)

# Display texts then show list of texts and sent_texts.

send_messages(texts, sent_texts)
print('\n')
print(texts)
print(sent_texts)
