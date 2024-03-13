# this one creates a network elastic-network. and runs 2 elastic search containers from image tag:2. which use an alias of search, and that network to communicate
# which allows to sort of load balancing by using the same alias, and the
# network can sometimes call to a different container if we call him by his
# alias. since both containers are on same alias
docker network create elastic-network

NAME="elasticsearch"

docker run -d --name $NAME-1 --network elastic-network --network-alias search -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:2

docker run -d --name $NAME-2 --network elastic-network --network-alias search -p 9201:9200 -p 9301:9300 -e "discovery.type=single-node" elasticsearch:2

docker run -itd --name centos --network elastic-network centos

# we test inside centos if curl can see search alias in the network
docker exec -it centos /bin/bash
# now if we run the curl search:9200 several times
# we will see the name that shows sometimes changes, because it goes to a another
# container.. we can test that name with the other port number of the second
# container.
curl search:9200
curl search:9201
