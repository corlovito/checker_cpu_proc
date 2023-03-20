import os
import time

while True:
    time.sleep(30)
    #os.system("ps -eLf | grep [p]arse.php | awk '{print $2}' > proc.txt")
    os.system("./cpu_check.sh > cpu.txt")
    status=os.system("systemctl status checker | awk '/Active/ {print $2}'")
    print(status)

    def kill_proc():
        with open("proc.txt") as file:
            array = [row.strip() for row in file]

        proc_array=[float(x) for x in array]
        for i in proc_array:
            os.kill(int(i), 9)

    def start_proc():
        os.system("systemctl start checker")

    #if status=="active":
    #    print("Script running")
    #else:
    #    #start_proc()
    #    os.system("systemctl start checker")


    with open("cpu.txt") as file:
        array = [row.strip() for row in file]

    cpu_array=[float(x) for x in array]

    for i in cpu_array:
        if i > 10:
            #kill_proc()
            os.system("systemctl restart checker")
        else:
            print('%s Normal' % i)