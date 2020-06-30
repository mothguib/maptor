#!/bin/sh

. activate pse-env

cd ~/Reps/PytrolSimEditor/
git pull
rsync -az --exclude='.git/' $REPS/PytrolSimEditor/ ~/Run/PytrolSimEditor/
cd $RUN/PytrolSimEditor/

nexecs=(2000 1000 670 400)
variant=0.2

for m in circle corridor map_b
do
    i=0
    for n in 5 10 15 25
    do
	python main2-2.3d-idls2bin-vidls.py --variant "$variant" --map "$m" --nagts "$n" --nbexecs "${nexecs[i]}"
	i=$(($i + 1))
    done
done
	

