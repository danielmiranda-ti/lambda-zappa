if [ ! -d "venv" ]
then
    python3.8 -m venv venv
    echo '================================'
fi

source venv/bin/activate

pip3 install -r requirements.txt