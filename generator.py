def flat_generator_present(my_list):
    for lists in my_list:
        for item in lists:
            yield item


def flat_generator_list(my_list):
    for item in my_list:
        if isinstance(item, list):
            for element in flat_generator_list(item):
                yield element
        else:
            yield item


