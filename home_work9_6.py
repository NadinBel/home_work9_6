import itertools
def all_variants(text):
    for item in range(1, len(text) + 1):
        for i in itertools.combinations(text, item):
            s = ''.join(i)
            yield s




# Testing with driver code
a = all_variants("abc")
for i in a:
    print(i)