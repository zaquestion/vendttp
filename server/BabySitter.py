import subprocess

print("BabySitter is sitting the baby")
restartOnExit = 1
while 0 != restartOnExit:
    print("Baby fell over, re-sitting")
    restartOnExit = subprocess.call("python server.py")
