
import datetime

import _main_multi as m

if __name__ == "__main__":

    time_limit = datetime.datetime.now() + datetime.timedelta(minutes=1)
    name = 'test'

    m.random_part(time_limit, name)

    pass