nohup python main.py > logs/twitterBot.out 2>&1 &
echo $! > logs/save_pid.txt
