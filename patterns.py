def generate_v1(patterns):
    options = {
        'date': {
            'max_len': 10,
            'position': (368.7, 731),
            'align': 'centred',
            'fontsize': 9
        },

        'time': {
            'max_len': 10,
            'position': (450.4, 731),
            'align': 'centred',
            'fontsize': 9
        },

        'name': {
            'max_len': 10,
            'position': (67, 717.5),
            'align': 'left',
            'fontsize': 11
        },

        'doctor': {
            'max_len': 10,
            'position': (67, 36),
            'align': 'left',
            'fontsize': 10
        },

        'phone_number': {
            'max_len': 10,
            'position': (87, 704.1),
            'align': 'left',
            'fontsize': 11
        },

        'wanted_result': {
            'max_len': 10,
            'position': (297, 652),
            'align': 'centred',
            'fontsize': 14
        },

        'for_better_effect': {
            'max_len': 45,
            'position': (319.7, 384),
            'align': 'left',
            'fontsize': 8,
            'leading': 15.45,
            'mode': 'text'
        }
    }

    items = {
        'title': {'max_len': 10, 'position': (0, 0), 'align': 'left'},
        'amount': {'max_len': 10, 'position': (158.1, 0), 'align': 'centred'},
        'period': {'max_len': 10, 'position': (198, 0), 'align': 'centred'},
    }

    steps = [(52.2, 548.6), (319.7, 548.6), (52.2, 370)]

    for i, (x, y) in enumerate(steps):
        step = create_str_table(
            position=(x, y),
            items=items,
            n_rows=5,
            row_height=15.45,
            row_name='procedure',
            table_prefix=f'step_{i + 1}_'
        )

        step.update({
            f'step{i + 1}_comment': {'max_len': 10,
                                     'position': (x, y - 92.7),
                                     'align': 'left'}
        })

        options.update(step)

    patterns['v1'] = {}
    patterns['v1']['options'] = options
    patterns['v1']['bg'] = 'blank_v1.pdf'


def create_str_row(position, items):
    options = {}
    options.update({k:v.copy() for k, v in items.items()})
    for item in items:
        new_pos_x = round(options[item]['position'][0] + position[0], 2)
        new_pos_y = round(options[item]['position'][1] + position[1], 2)
        options[item]['position'] = (new_pos_x, new_pos_y)
    return options


def create_str_table(position, items, n_rows, row_height, row_name='row', table_prefix=''):
    options = {}
    for i in range(0, n_rows):
        row_position = position
        row_y = round(row_position[1] - row_height*i, 2)
        row_position = (row_position[0], row_y)
        row = create_str_row(row_position, items)
        renamed_row = {f'{table_prefix}{row_name}_{k}_{i+1}':v for k,v in row.items()}
        options.update(renamed_row)
    return options


PATTERNS = {}
generate_v1(PATTERNS)