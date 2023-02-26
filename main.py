import types
# Задача №1
class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = [i[:] for i in list_of_list]


    def __iter__(self):
        self.list = self.l_of_l
        return self

    def __next__(self):
        if len(self.list) == 0:
            raise StopIteration
        down_list = self.list[0]
        down_el = down_list.pop(0)
        if len(down_list) == 0:
            self.list.pop(0)

        return down_el
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


if __name__ == '__main__':
    test_1()

# Задача №2
def flat_generator(list_of_lists):
    while len(list_of_lists) != 0:

        list_of_lists = [i[:] for i in list_of_lists]
        down_list = list_of_lists[0]
        el = down_list.pop(0)
        if len(down_list) == 0:
            list_of_lists.pop(0)
        yield el

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

# Задача №4
def flat_generator(list_of_list):
    for el in list_of_list:
        if isinstance(el,list):
            yield from flat_generator(el)
        else:
            yield el


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()