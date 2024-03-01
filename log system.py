import datetime


def log_system():
    def log_msg(msg=''):
        # print(msg)
        return msg

    def log_msg_timestamp(msg=''):
        ct = datetime.datetime.now()
        return f"{ct.hour}:{ct.minute}:{ct.second} : {msg}"

    def log_msg_timestamp_level(msg='', level=''):
        ct = datetime.datetime.now()

        return f"{ct.hour}:{ct.minute}:{ct.second}  :{level} - {msg}"

    def log_events_date(events=''):
        return f'{events} - {datetime.date.today()}'

    return log_msg, log_msg_timestamp, log_msg_timestamp_level, log_events_date


def log_processing(log_list, filter_type=None, start_time=None, end_time=None, max_length=None):
    def log_filter():
        filtered_logs = []
        for log in log_list:
            if filter_type is not None:
                if 'no' in filter_type:
                    if filter_type.split()[1] not in log:
                        filtered_logs.append(log)
                else:
                    if filter_type in log:
                        filtered_logs.append(log)
            elif start_time is not None and end_time is not None:
                if 'timestamp' in log:
                    time_ = log.split()[0]
                    hour = int(time_.split(':')[0])
                    minutes = int(time_.split(':')[1])
                    if end_time > (hour,minutes) > start_time:
                        filtered_logs.append(log)
            elif max_length is not None:
                if len(log) < max_length:
                    filtered_logs.append(log)
        return filtered_logs

    return log_filter()


log, log_time, log_time_level, log_events = log_system()
log_list = [log('log message '),
            log_time('log message with timestamp')
    , log_time_level('log print with level and timestamp', 'info'),
            log_events('successfully printed events with date')]

print("filter out no timestamp logs")
print(log_processing(log_list, filter_type='no timestamp'),'\n')
print("filter out no date logs")
print(log_processing(log_list, filter_type='no date'),'\n')
print("show only logs with msg that shorter than 50")
print(log_processing(log_list, max_length=50),'\n')
print("show only logs in timestamp range 20:00:00 and 21:00:00")
print(log_processing(log_list, start_time=(20, 0), end_time=(21, 55)))
