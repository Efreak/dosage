#!/bin/sh
set -e
set -u

d=$(dirname $0)
if [ $# -ge 1 ]; then
  list="$*"
else
  list="arcamax comicfury comicgenesis creators gocomics keenspot smackjeeves webcomicfactory tapastic"
fi
for script in $list; do
  echo "Executing ${script}.py"
  "${d}/${script}.py"
done
