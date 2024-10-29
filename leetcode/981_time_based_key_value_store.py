class TimeMap(object):
    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key in self.time_map:
            self.time_map[key].append([timestamp, value])
        else:
            self.time_map[key] = [[timestamp, value]]
        
    def get(self, key, timestamp):
        res = ""
        if key in self.time_map:
            time_stamps = self.time_map[key]
            l = 0
            r = len(time_stamps) - 1
            while l <= r:
                mid = (l + r) // 2
                time = time_stamps[mid][0]
                value = time_stamps[mid][1]
                if time <= timestamp:
                    res = value
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return res