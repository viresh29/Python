from datetime import datetime, timedelta, timezone
import pytz
import pendulum

dag_interval = timedelta(days=1)

hours_of_checking = {
    'hour': 0,
    'minute': 40,
    'second': 0,
    'microsecond': 0
}

timezone = 'US/Central'

execution_date = datetime(2021, 1, 23, 12, 40)


def get_poking_time_for_reports(dag_interval, timezone, execution_date, **kwargs):
    # Add the schedule interval to execution date and convert it to midnight
    midnight_of_execution_date = (
        execution_date + dag_interval).replace(**kwargs)

    # get the local time from mid night execution date and add the UTC time at the end.
    local_time = pendulum.instance(pytz.timezone(timezone).localize(
        datetime.fromtimestamp(midnight_of_execution_date.timestamp())).astimezone(pytz.utc))

    return local_time


print('Poking Time - {}'.format(get_poking_time_for_reports(
    dag_interval, timezone, execution_date, **hours_of_checking)))
