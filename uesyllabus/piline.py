# -*- coding: utf-8 -*-


def ask(description='' ,type='text', selects=None, default=None):

    print ''
    print description

    if type == 'text':
        if default is not None:
            print 'default ' + default

        input_text = raw_input()
        if default is not None and input_text == '':
            return default
        else:
            return input_text

    elif type == 'select':

        if default is not None and default != '':
            print 'default ' + default + ':' + selects[default]

        while True:

            print 'Please input number  number:value'
            for key in selects:
                print key + ':' + selects[key]

            input_text = raw_input()
            if input_text in selects.keys():
                return input_text
            else:
                if default is None:
                    print 'sorry input number again'
                elif input_text == '':
                    return default
