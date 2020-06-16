
import pika

import random
import time

set_queue = "B_to_A"
get_queue = "A_to_B"
win_queue = "Point_B"

point = "1"

credentials = pika.PlainCredentials('admin', '123456')
parameters = pika.ConnectionParameters('172.17.0.2', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()


def setPoint():
    try:
        channel.queue_declare(queue=win_queue)
        channel.basic_publish(exchange='', routing_key=win_queue, body=point)
    except:
        return -1


def sendNumber(number):
    try:
        channel.queue_declare(queue=set_queue)
        channel.basic_publish(exchange='', routing_key=set_queue, body=str(number))
    except:
        return -1


def receiveNumber():
    try:
        channel.queue_declare(queue=get_queue)
        method_frame, header_frame, body = channel.basic_get(queue=get_queue)
        if method_frame.NAME == 'Basic.GetEmpty':
            return-1
        else:
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            return int(body)
    except:
        return(-1)


def randomArray():
    random_array = []
    for i in range(0, 5):
        randomNumber = (random.randint(0, 20))
        random_array.append(randomNumber)
    return random_array


control = True

print("--------Started Game For B ---------")
while(control):
    time.sleep(1)
    randomNumber = (random.randint(0, 20))
    sendNumber(randomNumber)
    receivedData = receiveNumber()
    if receivedData != -1:
        random_array = randomArray()
        print("Incoming number : "+str(receivedData) +"  Predictions Array  : "+str(random_array))
        cntl = receivedData in random_array
        if cntl:
            print("B Gained "+str(point)+" point")
            print("-----------------")
            setPoint()
        else:
            print("B predictions are wrong.")
            print("-----------------")
