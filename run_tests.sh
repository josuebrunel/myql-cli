##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Sat Jun  6 04:00:31 2015
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


