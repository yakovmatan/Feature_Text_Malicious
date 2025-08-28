from pub_100_mes_at_min.src.manager import Manager
import time

manager = Manager()

while True:
    manager.publish_messages()
    time.sleep(60)

