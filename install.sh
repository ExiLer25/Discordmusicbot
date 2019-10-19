#!/bin/sh

curl -sS http://files.minecraftforge.net/maven/net/minecraftforge/forge/$forgv/forge-$forgv-installer.jar -o installer.jar

java -jar forge-*-installer.jar -installServer
