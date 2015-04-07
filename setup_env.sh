##################################################
#
#   Author          : josuebrunel
#   Filename        : setup_env.sh
#   Description     :
#   Creation Date   : 06-04-2015
#   Last Modified   : Tue 07 Apr 2015 01:24:34 PM CEST
#
##################################################

env=env
lib=lib
repository=git@github.com:josuebrunel/myql.git

_debug "Cleaning the cat house"
rm -rf $env
rm -rf $lib

_debug "Creating Env"
mkdir -p $env
virtualenv $env

_debug "Activating Virtual Env"
source $env/bin/activate

_debug "Cloning libs"
git clone $repository $lib

_debug "Installing libs"
cd $lib
python setup.py install --record files.txt

_info "Cleaning the cat house"
rm -rf $lib

_info "source ${env}/bin/activate"
