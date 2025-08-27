from manager import Manager
import time

manager = Manager()

while True:
    manager.publish_messages()
    time.sleep(60)

