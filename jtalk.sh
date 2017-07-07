#!/bin/sh

#VOICE='/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice'
VOICE='/usr/share/hts-voice/mei/mei_normal.htsvoice'
TMPFILE='/tmp/jtalk.wav'
DIC='/var/lib/mecab/dic/open-jtalk/naist-jdic'

echo "$1" | open_jtalk -m $VOICE -x $DIC -ow $TMPFILE
aplay -q $TMPFILE
rm $TMPFILE
