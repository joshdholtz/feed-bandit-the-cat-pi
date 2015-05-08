from iron_mq import *

import os
import time

import stepper

project_id = os.environ['IRON_MQ_PROJECT_ID']
token = os.environ['IRON_MQ_TOKEN']
queue_name = os.environ['IRON_MQ_QUEUE_NAME']

ironmq = IronMQ(project_id=project_id,token=token)
queue = ironmq.queue(queue_name)

def check_message():
  print("Checking for message")

  resp = queue.get(max=1, timeout=None)
  messages = resp['messages']
  if (len(messages) > 0):
    message = messages[0]

    message_id = message['id']
    message_body = message['body']

    queue.clear()

    print("Rotating feeder")
    stepper.rotate(1024,5,2)
    time.sleep(2)
    stepper.rotate(1024,5,2)

if __name__ == "__main__":
  while True:
    check_message()
    time.sleep(10)
