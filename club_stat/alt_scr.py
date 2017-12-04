
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

import logging

logging.basicConfig(
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.WARNING,
    filename=u'mylog4.log')

def job_function():
    print(str(datetime.now()))
    logging.warning(u'info')
    logging.error(u'This is an info message')

sched = BlockingScheduler()
sched.add_job(job_function, 'cron', hour='*', minute="*", second="*/5")
sched.start()


