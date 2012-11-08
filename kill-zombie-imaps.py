#!/usr/bin/python
#
# We keep getting these zombie imap processes that look like this:
#
# root     16170  4776  0 Dec01 ?        00:00:00 imapd
#
# Here the process is owned by root, has a PID of 16170, and is called imapd
#
# What we need to do is grab all of the ones owned by root, determine
# the process ids, and then kill them.  Easy enough, right?
#
# Written by Lou Ruppert <lou@ucf.org>
#
import subprocess
import re
import os

pl = subprocess.Popen(['/bin/ps', '-U', '0'],
                       stdout=subprocess.PIPE).communicate()[0]

for line in pl.splitlines():
    m = re.search('(\d+)\s+\?\s+[\d+:]+\s+imapd', line)
    if (m != None):
        pid = int(m.group(1))
        if (pid != 0):
            os.kill(pid, 9)
