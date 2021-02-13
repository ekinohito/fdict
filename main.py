class FDict(dict):
    def __init__(self, f, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.f = f

    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)
        else:
            return self.f(item)


def fdict(f):
    return FDict(f)


@fdict
def test(x):
    return x % 2 == 0


if __name__ == '__main__':
    test[0] = False
    for i in range(10):
        print(i, ': ', test[i])
