class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.index = 0
        self.sub_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.sub_index < len(self.list_of_lists[self.index]):
                item = self.list_of_lists[self.index][self.sub_index]
                self.sub_index += 1
                return item
            else:
                self.sub_index = 0
                self.index += 1
                if self.index < len(self.list_of_lists):
                    return self.__next__()
                else:
                    raise StopIteration
        except IndexError:
            raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print(list(FlatIterator(list_of_lists_1)))

if __name__ == '__main__':
    test_1()