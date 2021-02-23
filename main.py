class FDict:
    def __init__(self, f):
        self.contexts = [{}]
        self.f = f

    def __setitem__(self, key, value):
        self.contexts[-1][key] = value

    def __getitem__(self, item):
        for context in reversed(self.contexts):
            if item in context:
                return context[item]
        return self.f(item)

    def __enter__(self):
        self.contexts.append({})

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.contexts.pop()


@FDict
def test(x):
    return x % 2 == 0


if __name__ == '__main__':
    test[0] = False
    for i in range(5):
        print(i, ': ', test[i])

    with test:
        test[3] = True
        for i in range(5):
            print(i, ': ', test[i])

    for i in range(5):
        print(i, ': ', test[i])
