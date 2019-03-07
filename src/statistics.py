import math
import linecache
import os
import tracemalloc


class Statistics:
    def __init__(self):
        self.trace = tracemalloc
        self.trace.start()

    def display_top(self, snapshot, key_type='lineno', limit=10):
        snapshot = snapshot.filter_traces((
            self.trace.Filter(False, "<frozen importlib._bootstrap>"),
            self.trace.Filter(False, "<unknown>"),
        ))
        top_stats = snapshot.statistics(key_type)

        print("Top %s lines" % limit)
        for index, stat in enumerate(top_stats[:limit], 1):
            frame = stat.traceback[0]
            # replace "/path/to/module/file.py" with "module/file.py"
            filename = os.sep.join(frame.filename.split(os.sep)[-2:])
            print("#%s: %s:%s: %s KiB"
                  % (index, filename, frame.lineno, self.convert_size(stat.size)))
            line = linecache.getline(frame.filename, frame.lineno).strip()
            if line:
                print('%s' % line)

        other = top_stats[limit:]
        if other:
            size = sum(stat.size for stat in other)
            print("%s other: %s KiB" % (len(other), self.convert_size(size)))
        total = sum(stat.size for stat in top_stats)
        print("Total allocated size: %s " % self.convert_size(total))

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])
