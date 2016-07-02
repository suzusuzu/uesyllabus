# -*- coding: utf-8 -*-

import json

class Lecture:

    def __init__(
            self,
            semester=None,
            start_semester=None,
            week_period=None,
            code=None,
            subject=None,
            lecturer=None,
            ):

        self.semester = semester
        self.start_semester = start_semester
        self.codo = code
        self.subject = subject
        self.lecturer = lecturer

        self.week_periods = self.__parse_week_period(week_period)

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __parse_week_period(self, week_period):
        if week_period is None:
            return []

        return map(lambda x: x.strip(), week_period.split(','))
