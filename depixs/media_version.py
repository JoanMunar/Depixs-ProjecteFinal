#-*- coding: utf-8 -*-

import subprocess
import datetime


def run_process(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    data = []
    while(True):
      retcode = p.poll()
      line = p.stdout.readline()
      data.append(line)
      if(retcode is not None):
        break

    return ''.join(data).replace('\n','')


def get_hg_version():
    try:
        return run_process(['hg', 'identify', '--num', '--config',  'ui.report_untrusted=False'])
    except:
        return run_process(['/usr/local/bin/hg', 'identify', '--num', '--config',  'ui.report_untrusted=False'])
        pass
