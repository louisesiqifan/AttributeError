import configparser

config = configparser.ConfigParser()
config.read('../wrapper/constants.ini')
DATABASE_FILENAME = config['DEFAULT']['DATABASE_FILENAME']
UI = {'categories': list, 'level': str, 'title': str,
      'time': tuple, 'term': str}



def input_verification(ui_input):
    '''
    From ui_input, verify ui_input is correct
    '''
    for key, typ in UI.items():
        val = ui_input.get(key, None)
        if val is not None:
            if type(val) != typ:
                raise ValueError(f"input type for {key} should be {typ}")
            if key == 'categories':
                args = [x.title() for x in val]
                ui_input['categories'] = args
            if key == 'level':
                val = val.capitalize()
                levels = ['Easy', 'Intermediate', 'Advanced']
                assert val in levels, 'incorrect level'
                ind = levels.index(val)
                val_list = [int(i<=ind) for i,_ in enumerate(levels)]
                ui_input['level'] = val_list
            if key == 'time':
                upper_bound, mode = val
                assert mode in ['total', 'active'], 'incorrect mode'
                assert upper_bound > 0, 'incorret time constraint'
                ui_input['time'] = (str(upper_bound), mode)
            if key == 'title':
                args = val.title().split(',')
                ui_input['title'] = args
            if key == 'term':
                r = re.findall(r'[a-zA-Z]{2,}', val)
                args = list(set([x.lower() for x in r if x.lower() not in INDEX_IGNORE]))
                ui_input['term'] = args
    return ui_input