##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue 19 May 2015 01:56:03 PM CEST
#
##################################################

if [ ! -z $1 ]; then
    suite="$1"
else
    suite='Query'
fi

if [ ! -z $2 ]; then
    method=".$2"
else
    method=''
fi

if [ -f credentials.json ]; then
    python -m unittest tests.TestYqlOAuth
fi

python -m unittest tests.TestYql$suite$method


