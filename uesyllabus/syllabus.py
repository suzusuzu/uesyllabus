# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from lecture import Lecture

class Syllabus:
    URL = 'http://kyoumu.office.uec.ac.jp/campusweb/'
    SUBMIT_URL = 'http://kyoumu.office.uec.ac.jp/campusweb/campussquare.do'

    def __init__(self):
        pass

    def get_lectures(self, options=None):
        lectures = {}
        text = self.__get_page(options)
        soup = BeautifulSoup(text, "lxml")
        tables = soup.find_all('table')
        if len(tables) > 1:
            trs = tables[1].find_all('tr')
            for tr_index, tr in enumerate(trs):
                if tr_index != 0:
                    try:
                        tds = tr.find_all('td')

                        semester = tds[1].text.strip()
                        start_semester = tds[2].text.strip()
                        week_period = tds[3].text.strip()
                        code = tds[4].text.strip()
                        subject = tds[5].text.strip()
                        lecturer = tds[6].text.strip()

                        lectures[code] = Lecture(semester, start_semester, week_period, code, subject, lecturer)
                    except:
                        pass

        return lectures

    def __get_page(self, options=None):
        payload = self.__get_default_payload()
        if options is not None:
            for key in options:
                payload[key] = options[key]
        return self.s.post(Syllabus.SUBMIT_URL, data=payload).text


    def __get_default_payload(self):
        self.s = requests.Session()
        request = self.s.get(Syllabus.URL)
        soup = BeautifulSoup(request.text, "lxml")
        payload = {}

        inputs = soup.find_all('input')
        for input in inputs:
            if str(input).find("name") > -1:
                payload[input['name']] = input['value']

        selects = soup.find_all('select')
        for select in selects:
            if str(select).find('name') > -1:
                payload[select['name']] = ''

        return payload

