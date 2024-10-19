import psutil
from collections import defaultdict


class TaskManager():
    process_dict = defaultdict(lambda : {'PIDLIST':[],'RAM':0,'CPU':0})
    processes = []
    def __init__(self):
        self.get_all_processes()

    def get_all_processes(self):
        self.process_dict.clear()
        self.processes.clear()
        for p in psutil.process_iter(['pid','name','memory_info','cpu_percent']):
            try:
                self.process_dict[p.info['name']]['PIDLIST'].append(p.info['pid'])
                self.process_dict[p.info['name']]['RAM'] += p.info['memory_info'].rss / (1024*1024)
                self.process_dict[p.info['name']]['CPU'] += p.cpu_percent(interval=0)
            except (psutil.NoSuchProcess,psutil.AccessDenied):
                continue
        self.processes = sorted(self.process_dict.items(), key=lambda x: x[1]['RAM'], reverse=True)
        return self.processes
        
    def get_cpu_usage(self,appname):
        cpu_count = psutil.cpu_count(logical=True)
        sum_cpu_usage = 0
        pids = self.process_dict[appname]['PIDLIST']
        for pid in pids:
            p = psutil.Process(pid)
            sum_cpu_usage+=p.cpu_percent(interval=1)
        return sum_cpu_usage / cpu_count

    def kill_process(self,appname):
        pids = self.process_dict[appname]['PIDLIST']
        for pid in pids:
            try:
                p = psutil.Process(pid)
                p.terminate()
                p.wait()
            except psutil.NoSuchProcess:
                continue
            except psutil.AccessDenied:
                continue
        self.get_all_processes()

    def print_process_names_and_ram_usage(self):
        for pname,pinfo in self.processes:
            print(f"name : {pname} ram_usage={pinfo['RAM']}")
    def print_process_names(self):
        for pname,pinfo in self.processes:
            print(pname)
    def get_process_names_as_list(self):
        pnameList = []
        for pname,pinfo in self.processes:
            pnameList.append(pname)
        return pnameList
    def is_process_exists(self,appname):
        if len(self.process_dict[appname]["PIDLIST"]) > 0:
            print("var")
        else:
            print("yok")
        


