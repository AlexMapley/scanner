#!/bin/sh
echo 'This is Interactive Perl shell'
rlwrap -A -pgreen -S"perl> " perl -wnE'say eval()//$@'