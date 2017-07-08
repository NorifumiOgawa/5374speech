#!/usr/bin/env python
# -*- coding:utf-8 -*-

from icalendar import Calendar, Event
from datetime import datetime
import math
import subprocess
import shlex

PATH = '/home/pi/5374speech/'
CMD_TALK = PATH + 'jtalk.sh'

def main():
    gomi_calendar = Calendar.from_ical(open(PATH + '5374.ics', 'rb').read())
    youbi = ["MO","TU","WE","TH","FR","SA","SU"]
    youbi_ja = ["月","火","水","木","金","土","日"]
    d = datetime.now()
    youbi_count = int(math.floor((d.day + 6) / 7))
    gomi_count = 0

    text = '今日は第%s%s曜日、ゴミの収集日です。' % (youbi_count, youbi_ja[d.weekday()])
    youbi_with_count = str(youbi_count) + youbi[d.weekday()]

    for gomidashi in gomi_calendar.walk():
        if gomidashi.name == 'VEVENT':
            summary = gomidashi.get('summary').encode("utf-8")
            recur = gomidashi.get("RRULE")

            if youbi[d.weekday()] in recur.get("BYDAY", []) or youbi_with_count in recur.get("BYDAY", []):
                text = text + summary + ' '
                gomi_count+=1

    if gomi_count > 0:
        text = CMD_TALK + ' \"' + text + 'を捨てましょう。\"'
        proc = subprocess.Popen(shlex.split(text))
        proc.communicate()

if __name__ == '__main__':
    main()
