import subprocess
import time

print("BabySitter is sitting the baby")
restartOnExit = 1
while 0 != restartOnExit:
    print("Baby fell over, re-sitting")
    time.sleep(5)
    restartOnExit = subprocess.call("python server.py")
