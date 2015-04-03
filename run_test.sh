##################################################
#
#   Author          : josuebrunel
#   Filename        : run_test.sh
#   Description     :
#   Creation Date   : 03-04-2015
#   Last Modified   : Fri 03 Apr 2015 03:30:32 PM UTC
#
##################################################
if [ ! -z $1 ]; then
    method=".$1"
else
    method=''
fi

python -m unittest tests.TestYqlShell$method
