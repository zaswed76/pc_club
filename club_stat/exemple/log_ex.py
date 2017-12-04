# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO,
    filename=u'mylog.log')


logging.info(u'This is an info message')

