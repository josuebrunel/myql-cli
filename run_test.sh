##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue Apr  7 09:49:07 2015
#
##################################################


if [ ! -z $1 ]; then
    method=".$1"
else
    method=''
fi

python -m unittest tests.TestYqlQuery$method
