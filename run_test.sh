##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Tue 07 Apr 2015 11:26:31 AM CEST
#
##################################################


if [ ! -z $1 ]; then
    method=".$1"
else
    method=''
fi

python -m unittest tests.TestYqlQuery$method
