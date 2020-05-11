#!/bin/bash

#cd linuxopg
sudo git add *
sudo git config --global user.email "torben400@hotmail.com"
sudo git config --global user.name "torbenboll"
echo Navn til commiten?
read commit
sudo git commit -m $commit
sudo git push
