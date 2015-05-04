##################################################
#
#   Author          : josuebrunel
#   Filename        : publish_package.sh
#   Description     :
#   Creation Date   : 03-05-2015
#   Last Modified   : Mon May  4 06:59:45 2015
#
##################################################

if [ ! -z $1 ]; then
    if [ "$1" == "testing" ]; then
        server=pypitest
    else
        server=pypi
    fi
else
    server=pypitest
fi

_debug "Publish on ${server}"

_info "python setup.py register -r ${server}"
python setup.py register -r $server

_info "python setup.py sdist upload -r ${server}"
python setup.py sdist upload -r $server
