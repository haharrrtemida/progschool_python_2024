text = "магазин"

text_set = set(text)
text_frozenset = frozenset(text)

print(text_set.__sizeof__())
print(text_frozenset.__sizeof__())