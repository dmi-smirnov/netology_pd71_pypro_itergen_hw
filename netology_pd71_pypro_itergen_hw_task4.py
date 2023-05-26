# Необязательное задание.
# Написать генератор, аналогичный генератору из задания 2,
# но обрабатывающий списки с любым уровнем вложенности.
# Шаблон и тест в коде ниже:

import types


def flat_generator(list_of_list):
  lists_iters = [list_of_list.__iter__()]
  while lists_iters:
    try:
      item = lists_iters[-1].__next__()
      if isinstance(item, list):
        lists_iters.append(item.__iter__())
      else:
        yield item
    except StopIteration:
      lists_iters.pop()
    

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