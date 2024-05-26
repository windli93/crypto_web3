#docker restart $(docker ps -a |  grep "sele_chrome.*"  | awk '{print $1}')
echo "Remove sele_chrome service container"
docker rm $(docker ps -a | grep Exited | awk '{print $1}')