# coding=utf8

class HallMgr(object):
    # free hall number
    free_number = 0
    # number of halls in used
    busy_number = 0

    def allocate(self):
        if self.free_number:
            self.free_number -= 1
            self.busy_number += 1
        else:
            # there is no enough hall, so create more
            self.busy_number += 1

    def free(self):
        if self.busy_number:
            self.busy_number -= 1
            self.free_number += 1
        else:
            raise Exception('error')

    def process_activities(self, activities):
        '''activities is list, [start_time, stop_time]'''
        start_times = [a[0] for a in activities]
        stop_times = [a[1] for a in activities]
        # sort in increasing order
        start_times.sort()
        stop_times.sort()
        # boolean list, True is allocate, False is free
        action_list = []
        while len(start_times) and len(stop_times):
            if start_times[0] < stop_times[0]:
                start_times.pop(0)
                action_list.append(True)
            elif start_times[0] > stop_times[0]:
                stop_times.pop(0)
                action_list.append(False)
            else:
                start_times.pop(0)
                stop_times.pop(0)
                action_list.append(False)
                action_list.append(True)
        action_list.extend([True for i in start_times])
        action_list.extend([False for i in stop_times])
        for i in action_list:
            self.allocate() if i else self.free()

        return self.free_number

if __name__ == '__main__':
    a_1 = [[0,10], [5,7], [9,12], [11,13]]
    a_2 = [[0,5], [2,7], [4,12], [11,13]]
    hall_mgr = HallMgr()
    print hall_mgr.process_activities(a_1) == 2
    print hall_mgr.process_activities(a_2) == 3

