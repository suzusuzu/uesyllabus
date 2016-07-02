# -*- coding: utf-8 -*-

import argparse
import datetime
import json
import os
from piline import ask


def parse():
    config = {}

    with open(os.path.abspath(os.path.dirname(__file__)) + '/resource/config.json', 'r') as f:
        config = json.loads(f.read(), "utf-8")

    this_year = str(datetime.date.today().year)

    parser = argparse.ArgumentParser(description='uesyllabus')

    parser.add_argument('--version', action='version', version='uesyllabus 0.1')

    parser.add_argument('-i', '--interactive-mode', action='store_true')

    parser.add_argument('-y', '--year', default=this_year, help='年度')
    parser.add_argument('-b', '--belong', default="31", choices=config['belong'].keys(), help='開講所属')
    parser.add_argument('-s', '--semester', default="", choices=config['semester'].keys(), help='学期')
    parser.add_argument('-l', '--lecturer', default="", help='教員名')
    parser.add_argument('-sj', '--subject', default="", help='科目名')
    parser.add_argument('-k', '--keyword', default="", help='キーワード')
    parser.add_argument('-sy','--school-year', default="", choices=config['school_year'].keys(), help='学年')
    parser.add_argument('-w', '--week', default="", choices=config['week'].keys(), help='曜日')
    parser.add_argument('-p', '--period', default="", choices=config['period'].keys(), help='時限')

    args = parser.parse_args()

    return generate_options(args, config)

def generate_options(args, config):

    options = {}

    if args.interactive_mode:
        options['nendo'] = ask('年度を入力してください', default='2016')
        options['jikanwariShozokuCode'] = ask('開講所属を入力してください 指定しない場合はそのままEnterを押してください', type='select', selects=config['belong'], default='31')
        options['gakkiKubunCode'] = ask('学期を入力してください 指定しない場合はそのままEnterを押してください', type='select', selects=config['semester'], default='')
        options['kyokanNm'] = ask('教員名を入力してください ※中間一致')
        options['kamokuNm'] = ask('科目名を入力してください ※中間一致')
        options['keyword'] = ask('キーワードを入力してください ※中間一致')
        options['nenji'] = ask('学年を入力してください 指定しない場合はそのままEnterを押してください', type='select', selects=config['school_year'], default='')
        options['yobi'] = ask('曜日を入力してください 指定しない場合はそのままEnterを押してください', type='select', selects=config['week'], default='')
        options['jigen'] = ask('時限を入力してください 指定しない場合はそのままEnterを押してください', type='select', selects=config['period'], default='')
    else:
        options['nendo'] = args.year
        options['jikanwariShozokuCode'] = args.belong
        options['gakkiKubunCode'] = args.semester
        options['kyokanNm'] = args.lecturer
        options['kamokuNm'] = args.subject
        options['keyword'] = args.keyword
        options['nenji'] = args.school_year
        options['yobi'] = args.week
        options['jigen'] = args.period

    return options
