class Process:
    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def run(self, quantum):
        if self.remaining_time <= quantum:
            execution_time = self.remaining_time
            self.remaining_time = 0
        else:
            execution_time = quantum
            self.remaining_time -= quantum
        return execution_time

class RoundRobin:
    def __init__(self, quantum):
        self.quantum = quantum
        self.queue = []
        self.time = 0
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def run(self):
        self.processes.sort(key=lambda x: x.arrival_time)
        
        while self.processes or self.queue:
            # اضافه کردن پروسس‌های جدید به صف با توجه به زمان ورودشان
            while self.processes and self.processes[0].arrival_time <= self.time:
                self.queue.append(self.processes.pop(0))
            
            if self.queue:
                current_process = self.queue.pop(0)
                execution_time = current_process.run(self.quantum)
                self.time += execution_time
                print(f"Time {self.time}: Process {current_process.id} executed for {execution_time} units.")
                
                if current_process.remaining_time > 0:
                    self.queue.append(current_process)
            else:
                # اگر صف خالی است اما هنوز پروسس‌هایی وجود دارند که وارد نشده‌اند
                self.time = self.processes[0].arrival_time
                print(f"Time {self.time}: Idle (waiting for next process)")

        print("All processes completed.")

# استفاده از الگوریتم

p = int (input("number of processes:"))
q = int (input("quantum:"))

rr = RoundRobin(quantum=q)

for i in range (p):
    id = int (input("ID p:"))
    ET = int (input("ET p:"))
    AT = int (input("AT p:"))
    rr.add_process(Process(id, ET, AT))

rr.run()