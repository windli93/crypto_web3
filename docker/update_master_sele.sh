#docker restart $(docker ps -a |  grep "sele_chrome.*"  | awk '{print $1}')
echo "update sele_chrome service"
sele="sele"
docker service update ${sele}_chrome --update-delay 10s --update-failure-action rollback --update-parallelism 1 --force
#sleep 60
#echo "Stack deploy selenium_full_grid"
#docker stack deploy -c /home/ubuntu/selenium_full_grid.yml ${sele}
#sleep 20
echo "Remove sele_chrome service container"
docker rm $(docker ps -a | grep Exited | awk '{print $1}')