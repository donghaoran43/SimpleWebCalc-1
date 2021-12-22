#!/bin/bash

container_name="calculator-main"

docker build -t ${container_name} .
docker container stop ${container_name}
docker container rm ${container_name}

sleep 1

docker run --name ${container_name} \
	-d \
	-p 5000:5000 \
	${container_name}

#sleep 10
#curl -L http://127.0.0.1:5000/calc.php



