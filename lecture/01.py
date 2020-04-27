# Objects
shakes = open('shakespeare.txt')
text = shakes.read().split()
print(len(text))
print(text[:25])
print(text.count('the'))
print(text.count('thou'))
print(text.count('you'))
print(text.count('forsooth'))
print(text.count(','))

# Sets
print('sets')
words = set(text)
print(len(words))
print(max(words))
print(max(words, key=len))

# Reversals
print('Reversals')
print('draw'[::-1])
print({w for w in words if w==w[::-1] and len(w)>4})
print({w for w in words if w[::-1] in words and len(w) == 4})
print({w for w in words if w[::-1] in words and len(w) > 6})

