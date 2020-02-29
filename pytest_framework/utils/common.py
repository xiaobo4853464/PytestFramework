import operator


def pytest_collection_modifyitems(session, config, items):
    cases_count = len(items)
    grouped_items = {}

    for item in items:
        mark = item.get_closest_marker('run')
        if mark:
            order = mark.kwargs.get('priority')
        else:
            order = None
        grouped_items.setdefault(order, []).append(item)

    priority_case_count = {"priority_%s" % k: len(v) for k, v in grouped_items.items()}
    print(priority_case_count)
    sorted_items = []
    unordered_items = [grouped_items.pop(None, [])]

    start_list = sorted((i for i in grouped_items.items() if i[0] >= 0),
                        key=operator.itemgetter(0))
    end_list = sorted((i for i in grouped_items.items() if i[0] < 0),
                      key=operator.itemgetter(0))

    sorted_items.extend([i[1] for i in start_list])
    sorted_items.extend(unordered_items)
    sorted_items.extend([i[1] for i in end_list])

    items[:] = [item for sublist in sorted_items for item in sublist]
