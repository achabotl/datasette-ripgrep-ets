#!/bin/sh
set -eux

PACKAGES="chaco enable envisage mayavi pyface traits traits-futures traitsui qt_binder apptools codetools scimath graphcanvas"

for PACKAGE in $PACKAGES
do
	if [ -d "all/$PACKAGE" ]; then
		rm -rf "all/$PACKAGE"
	fi
	git clone --depth 1 "https://github.com/enthought/$PACKAGE.git" "all/$PACKAGE"
done
