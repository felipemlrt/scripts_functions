#! /bin/bash

#use awk to print only certain columns from one file to another
#usando awk para passar apenas algumas colunas de um arquivo para outro

awk '{print $2 $4}' in.txt out.txt

#turning rows in columns
#

awk '{printf("%s ", $0)}'
