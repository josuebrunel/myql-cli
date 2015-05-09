##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Sat 09 May 2015 06:36:53 PM CEST
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

python -m unittest tests.TestYql$suite$method

if [ -f credentials.json ]; then
    python -m unittest tests.TestYqlOAuth
fi
