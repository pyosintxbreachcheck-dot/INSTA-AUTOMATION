import schedule
import time


def start_scheduler(job):

    schedule.every(24).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)
