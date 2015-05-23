if [ -e pid.txt ]; then
  kill -15 $(cat pid.txt) | true
  rm pid.txt
fi

pip install -r requirements.txt

export BUILD_ID=dontKillMe
nohup python main.py &
echo $! > pid.txt
