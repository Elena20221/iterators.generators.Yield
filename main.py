from iterator import  FlatIteratorList, FlatIteratorPresent
from generator  import flat_generator_present, flat_generator_list


if __name__ == '__main__':
    nested_list1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    nested_list2 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in FlatIteratorPresent(nested_list1):
     print(item)
    flat_list = [item for item in FlatIteratorPresent(nested_list1)]
    print(flat_list)
    for item in FlatIteratorList(nested_list2):
     print(item)
    flat_list2 = [item for item in FlatIteratorList(nested_list2)]
    print(flat_list2)
    for item in flat_generator_present(nested_list1):
     print(item)
    for item in flat_generator_list(nested_list2):
     print(item)














