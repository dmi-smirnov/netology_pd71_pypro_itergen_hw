# Необязательное задание.
# Написать итератор, аналогичный итератору из задания 1,
# но обрабатывающий списки с любым уровнем вложенности.
# Шаблон и тест в коде ниже:

class FlatIterator:

  def __init__(self, list_of_lists):
    self.list_of_lists = list_of_lists

  def __iter__(self):
    self.lists_iters = [self.list_of_lists.__iter__()]
    return self
  
  def __next__(self):
    item = FlatIterator.__get_next_item(self.lists_iters)
    return item
  
  def __get_next_item(lists_iters):
    while lists_iters:
      try:
        item = lists_iters[-1].__next__()
        if isinstance(item, list):
          lists_iters.append(item.__iter__())
        else:
          return item
      except StopIteration:
        lists_iters.pop()
    raise StopIteration
    
    # Вариант с рекурсией:
    # try:
    #   item = lists_iters[-1].__next__()
    # except StopIteration:
    #   lists_iters.pop()
    #   if not lists_iters:
    #     raise StopIteration
    #   item = FlatIterator.__get_next_item(lists_iters)
        
    # if isinstance(item, list):
    #     lists_iters.append(item.__iter__())
    #     item = FlatIterator.__get_next_item(lists_iters)

    # return item

def test_3():

  list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
  ]

  for flat_iterator_item, check_item in zip(
      FlatIterator(list_of_lists_2),
      ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
  ):

    assert flat_iterator_item == check_item

  assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
  test_3()