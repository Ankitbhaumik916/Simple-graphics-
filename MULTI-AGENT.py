import threading
import queue
import time

# Queues for message passing
agent1_queue = queue.Queue()
agent2_queue = queue.Queue()

def agent1():
    messages = ["Hello!", "How are you?", "That's great!", "Bye!"]
    for msg in messages:
        print("Agent 1 sends:", msg)
        agent2_queue.put(msg)
        time.sleep(1)
        reply = agent1_queue.get()
        print("Agent 1 receives:", reply)

def agent2():
    responses = ["Hi!", "I'm good, you?", "Thanks!", "See you!"]
    for reply in responses:
        msg = agent2_queue.get()
        print("Agent 2 receives:", msg)
        print("Agent 2 sends:", reply)
        agent1_queue.put(reply)
        time.sleep(2)

# Threads to run both agents concurrently
t1 = threading.Thread(target=agent1)
t2 = threading.Thread(target=agent2)

t1.start()
t2.start()

t1.join()
t2.join()
