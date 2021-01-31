#!/bin/sh
set -eux

PACKAGES="chaco enable envisage mayavi pyface traits traits-futures traitsui qt_binder traits-futures apptools codetools scimath graphcanvas"

for PACKAGE in $PACKAGES
do
	if [ -d "all/$PACKAGE" ]; then
		rm -rf "all/$PACKAGE"
	fi
	git clone --depth 1 "https://github.com/enthought/$PACKAGE.git" "all/$PACKAGE"
done

# Remove all/**/.git to reduce upload size and speed up ripgrep
find all -name ".git" -exec rm -fr "{}" \;
