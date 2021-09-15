# -*- coding: utf-8 -*-
# @Author: GXR
# @CreateTime: 2021-09-15
# @UpdateTime: 2021-09-15

import os

from apscheduler.schedulers.blocking import BlockingScheduler


def start_sekiro():
    os.popen("cd /srv/sekiro && sh /srv/sekiro/sekiro_run.sh")


scheduler_options = {
    "job_defaults": {"coalesce": True, "max_instances": 1, "misfire_grace_time": 30}
}
scheduler = BlockingScheduler(**scheduler_options)

scheduler.add_job(start_sekiro, "interval", minutes=0.1, id="sekiro")

if __name__ == "__main__":
    scheduler.start()
