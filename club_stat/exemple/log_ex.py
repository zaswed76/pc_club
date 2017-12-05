# -*- coding: utf-8 -*-

# import logging
#
# logging.basicConfig(
#     format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
#     level=logging.INFO,
#     filename=u'mylog.log')
#
#
# logging.info(u'This is an info message')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")
log2 = logging.getLogger(__name__)



def f(x):
    try:
        r = 5/x
    except:
        r = 0
        log.exception("Error!")

    log2.warning("warn")
    return r

f(0)
f(1)
f("w")
f(1)
f([])