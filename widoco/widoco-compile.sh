#!/usr/bin/env bash

set -o allexport
source widoco-compile-config
set +o allexport

echo ":: Creating tmp folder"
mkdir tmp
cd tmp

echo ":: Cloning WIDOCO git repo"
git clone https://github.com/dgarijo/Widoco.git && cd Widoco

WIDOCO_VERSION=$(mvn -q -Dexec.executable="echo" -Dexec.args='${project.version}' --non-recursive exec:exec)

echo ":: Setting WIDOCO lang variables"
sed -i -e "s#Add your references here. It is recommended to have them as a list.#$WIDOCO_REFERENCES_CONTENT#g" src/main/resources/widoco/en.properties

echo ":: Building WIDOCO"
mvn package 

echo ":: Moving and renaming WIDOCO jar"
cp jar/widoco-${WIDOCO_VERSION}-jar-with-dependencies.jar ../../widoco-custom.jar 
cd ..

echo ":: Cleaning up tmp folder contents"
rm -rf Widoco
cd ..
rmdir tmp

echo "> Done. You'll probably want to commit the new WIDOCO jar"