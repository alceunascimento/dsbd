#!/bin/bash

arqin=$1
arqout=$2

LANG=C sed -E 's/[\d008]//g' $arqin | sed -E 's/\r/\n/g' | grep val_loss > temp.txt
cut -d ' ' -f 11,17 < temp.txt | nl -s ' ' -n rz -w 3 | sed -E 's/ /; /g' > $arqout
rm temp.txt

