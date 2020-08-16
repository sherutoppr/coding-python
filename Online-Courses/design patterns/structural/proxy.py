'''
used when - we want to postpone the object creation unless absolutely necessary

scenario:
    producer: a fix number of producer object can be created
    artist: check frequently that producer is free or not for guest
    guest: who ask for objects

solution:
    clients: interacting with a proxy
    proxy: responsible for creating the resource intensive objects

'''

import time


class Producer:
    """define the resource-intensive objects to instantiate """
    def produce(self):
        print("producer is working hard")

    def meet(self):
        print("producer has time to meet you")


class Proxy:
    """" Define the 'less intentive-resource' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """check if producer is available or not"""
        print("artist checking if producer is available .....")

        if self.occupied == 'No':
            # if available , then create produver object
            self.producer = Producer()
            time.sleep(2)
            self.producer.meet()
        else:
            time.sleep(2)
            print("Producer is busy")


# instantiate the proxy
P = Proxy()
P.produce()

# change the state of occupied
P.occupied = "Yes"
P.produce()