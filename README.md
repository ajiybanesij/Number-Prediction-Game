# Number-Prediction-Game

This game runs on two containers that predict numbers using Python, RabbitMQ and Docker.

## Game
![System](https://github.com/ajiybanesij/Number-Prediction-Game/blob/master/SystemPicture.PNG)

Container_A generates a number between 0 and 9 and adds it to the A_to_B queue. It also expects data from the B_to_A queue. If data comes from the queue, it makes 5 number predictions and if one of the predictions is correct, it gets 1 point.

Container_B generates a number between 0 and 9 and adds it to the B_to_A queue. It also expects data from the A_to_B queue. If data comes from the queue, it makes 5 number predictions and if one of the predictions is correct, it gets 1 point. 



## RabbitMQ for Docker

[RabbitMQ for Docker ](https://www.rabbitmq.com/download.html)

```bash
docker run -d --hostname my-rabbit --name myrabbit -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=123456 -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

## Container build

```bash
cd Container A
docker build -t container_a

cd Container B
docker build -t container_b
```
 ## Start Game
```bash
docker run -it container_a

docker run -it container_b
```
## Screens
### Container A
![Container A](https://github.com/ajiybanesij/Number-Prediction-Game/blob/master/ContainerA_Image.PNG)

### Container B
![Container B](https://github.com/ajiybanesij/Number-Prediction-Game/blob/master/ContainerB_Image.PNG)
