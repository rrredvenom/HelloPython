


transformation = lambda list_item: list_item
values = [1, 4, 5, 'asf', 2.323, True]
result = list(map(transformation, values))

if result == values:
    print('ok')
else:
    print('not ok')