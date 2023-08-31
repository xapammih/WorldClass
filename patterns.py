def generate_v1(patterns):
    options = {
        'current_date': {
            'max_len': 10,
            'position': (368.7, 731),
            'align': 'centred',
            'fontsize': 9
        },

        'current_time': {
            'max_len': 10,
            'position': (450.4, 731),
            'align': 'centred',
            'fontsize': 9
        },

        'fio': {
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

        'phone': {
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

        'step_4_commentary': {
            'font': 'RobotoMono',
            'max_len': 44,
            'position': (319.7, 384),
            'align': 'left',
            'fontsize': 8,
            'leading': 15.45,
            'mode': 'text'
        }
    }

    items = {
        'procedure': {'max_len': 10, 'position': (0, 0), 'align': 'left'},
        'count_procedures': {'max_len': 10, 'position': (158.1, 0), 'align': 'centred'},
        'procedure_period': {'max_len': 10, 'position': (198, 0), 'align': 'centred'},
    }

    steps = [(52.2, 548.6), (319.7, 548.6), (52.2, 370)]

    for i, (x, y) in enumerate(steps):
        step = create_str_table(
            position=(x, y),
            items=items,
            n_rows=5,
            row_height=15.45,
            row_name='',
            table_prefix=f'step_{i + 1}'
        )

        step.update({
            f'step_{i + 1}_commentary': {'max_len': 10,
                                         'position': (x, y - 92.7),
                                         'align': 'left'}
            })

        options.update(step)

    # print(step.keys())

    patterns['v1'] = {}
    patterns['v1']['options'] = options
    patterns['v1']['bg'] = 'blank_v1.pdf'


def generate_v2(patterns):
    options = {
        'current_date': {
            'max_len': 10,
            'position': (368.7, 742),
            'align': 'centred',
            'fontsize': 8
        },

        'current_time': {
            'max_len': 10,
            'position': (450.4, 742),
            'align': 'centred',
            'fontsize': 8
        },

        'fio': {
            'max_len': 10,
            'position': (67, 728),
            'align': 'left',
            'fontsize': 10
        },

        'doctor': {
            'max_len': 10,
            'position': (422, 75),
            'align': 'left',
            'fontsize': 8
        },

        'phone': {
            'max_len': 10,
            'position': (87, 714.6),
            'align': 'left',
            'fontsize': 10
        },

        'wanted_result': {
            'max_len': 10,
            'position': (297, 683.7),
            'align': 'centred',
            'fontsize': 10
        },

        'step_4_commentary': {
            'font': 'RobotoMono',
            'max_len': 44,
            'position': (324.2, 378.4),
            'align': 'left',
            'fontsize': 8,
            'leading': 15.45,
            'mode': 'text',
            'max_text_rows': 12
        }
    }

    items = {
        'procedure': {'max_len': 10, 'position': (0, 0), 'align': 'left'},
        'count_procedures': {'max_len': 10, 'position': (156.1, 0), 'align': 'centred'},
        'procedure_period': {'max_len': 10, 'position': (199, 0), 'align': 'centred'},
    }

    steps = [(54.2, 593.6), (324.2, 593.6), (54.2, 363.4)]

    for i, (x, y) in enumerate(steps):
        step = create_str_table(
            position=(x, y),
            items=items,
            n_rows=9,
            row_height=15.45,
            row_name='',
            table_prefix=f'step_{i + 1}'
        )

        step.update({
            f'step_{i + 1}_commentary': {'mode': 'text',
                                         'font': 'RobotoMono',
                                         'fontsize': 8,
                                         'max_len': 44,
                                         'position': (x, y - 138.7),
                                         'leading': 15.45,
                                         'align': 'left',
                                         'max_text_rows': 2}
            })

        options.update(step)

    # print(step.keys())

    patterns['v2'] = {}
    patterns['v2']['options'] = options
    patterns['v2']['bg'] = 'blank_v2.pdf'


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
generate_v2(PATTERNS)
