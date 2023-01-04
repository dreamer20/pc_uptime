from datetime import timedelta


def totaluptimeformat(uptime: int) -> str:
    if uptime < 60:
        return 'less then minute'
    tdelta = timedelta(seconds=uptime)
    hours, minutes = 0, 0
    totaluptime_string = ''

    if tdelta.seconds >= 3600:
        hours = tdelta.seconds // 3600
        minutes = (tdelta.seconds % 3600) // 60
    else:
        minutes = tdelta.seconds // 60

    if (tdelta.days > 0):
        totaluptime_string = f'{tdelta.days} d. '

    if (hours > 0):
        totaluptime_string += f'{hours} h. '

    if (minutes > 0):
        if len(str(minutes)) == 1:
            totaluptime_string += f'0{minutes} min.'
        else:
            totaluptime_string += f'{minutes} min.'

    return totaluptime_string
