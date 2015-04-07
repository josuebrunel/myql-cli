##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue 07 Apr 2015 01:30:34 PM CEST
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

_debug "python -m unittest tests.TestYql${suite}${method}"
python -m unittest tests.TestYql$suite$method
