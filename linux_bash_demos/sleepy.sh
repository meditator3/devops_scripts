#! /bin/bash
echo "starting sleep...."
sleep 15 &
PID=$!
echo "PID of script is ${PID}"

pidof sleep
echo $!
wait $PID
echo "it i...end sleep!"
