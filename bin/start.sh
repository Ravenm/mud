BASEDIR=$(dirname $0/..)

if [ -e $BASEDIR/pid.txt ]; then
  kill -15 $(cat $BASEDIR/pid.txt) | true
  rm $BASEDIR/pid.txt
fi

pip install -r $BASEDIR/requirements.txt

export BUILD_ID=dontKillMe
nohup python $BASEDIR/main.py &
echo $! > $BASEDIR/pid.txt
