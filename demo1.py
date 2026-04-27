import threading
from time import sleep


def run(name):
    sleep(1)
    dir_values = {"one": "1", "two": "2"}
    print(f'one={dir_values[name]}')


thread = threading.Thread(target=run, args=("one",))
thread.start()
thread.join()
print("done")


