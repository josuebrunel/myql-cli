##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue 07 Apr 2015 02:01:42 PM CEST
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
