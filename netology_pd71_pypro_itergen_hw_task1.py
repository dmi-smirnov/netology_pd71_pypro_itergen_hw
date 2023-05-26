
# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков
# и возвращает их плоское представление, т. е. последовательность,
# состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

  def __init__(self, list_of_list):
    self.ext_list = list_of_list

  def __iter__(self):
    self.ext_list_iter = self.ext_list.__iter__()
    self.int_list_iter = self.ext_list_iter.__next__().__iter__()
    return self

  def __next__(self):
    try:
      item = self.int_list_iter.__next__()
    except StopIteration:
      self.int_list_iter = self.ext_list_iter.__next__().__iter__()
      item = self.int_list_iter.__next__()

    return item


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