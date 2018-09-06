#!/usr/bin/env bash
for i in {860..940}; do
./a.out $i | nc ctfq.sweetduet.info 10777
echo $i
done