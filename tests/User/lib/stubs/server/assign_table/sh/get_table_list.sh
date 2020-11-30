#!/usr/bin/env bash

sh ./t1.sh > table_list.html

tidy table_list.html |grep -i "<div" | sed 's/<div/\n/g' |sed 's/style/\n/g'|grep -i 'lid=' |grep -v line |sed 's/ //g'

# grep -i lid= table_list.html
# sort table_list.html