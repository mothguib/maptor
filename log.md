## [20181230]:

* Generation of HPLE HPME and HPRE's on-vertex iidls, eidls and idls:

. activate pse-env; i=; mkdir -p ~/Run"$i"; cd $REPS/PytrolSimEditor/; gitl; rsync -a --delete --exclude .git/ $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd $REPS/Pytrol; gitl; rsync -a --delete --exclude .git/ $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/Pytorch-Trainer/; gitl; rsync -a --delete --exclude .git/ $REPS/Pytorch-Trainer/ ~/Run"$i"/Pytorch-Trainer/; cd ~/Run"$i"/PytrolSimEditor; for s in hple hpme hpre; do for m in islands map_a grid; do for n in 1 5 10 15 25; do for e in $(seq 0 29); do python main2-4.3d-idls2vidls-eidls.py --map "$m" --nagts "$n" --strategy "$s" --variant "0.2" --nbexecs 30 --duration 3000 --exec-id "$e"; done; done; done; done

## [20181231]:

* Computation of HPLE HPME and HPRE's simulation MSE:

i=2; mkdir -p ~/Run"$i"; cd $REPS/PytrolSimEditor/; gitl; rsync -a --delete $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd $REPS/Pytrol; gitl; rsync -a $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/Pytorch-Trainer/; gitl; rsync -a --delete $REPS/Pytorch-Trainer/ ~/Run"$i"/Pytorch-Trainer/; cd ~/Run"$i"/PytrolSimEditor; for s in hple hpme hpre; do for m in islands map_a grid; do for n in 1 5 10 15 25; do python main7.mse-eidls-ridls.py --map "$m" --strategy "$s" --nagts "$n" --variant "0.2" --inf-exec-id 0 --sup-exec-id 29 --duration 3000 --data-src "$s"_0.2; done; done; done

## [20190121]:

*

. activate pse-env; i=; mkdir -p ~/Run"$i"; cd $REPS/PytrolSimEditor/; gitl; rsync -a --delete --exclude=.git $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd $REPS/Pytrol; git pull; rsync -a $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/Pytorch-Trainer/; gitl; rsync -a --delete $REPS/Pytorch-Trainer/ ~/Run"$i"/Pytorch-Trainer/; cd ~/Run"$i"/PytrolSimEditor; for m in islands map_a grid circle corridor map_b; do k=0; nagts="5 10 15 25"; nagts=($nagts); nbexecs="2000 1000 667 400"; nbexecs=($nbexecs); while [ "$k" -lt 4 ]; do python main2-2.3d-idls2bin-vidls.py --map "$m"  --nagts "${nagts[$k]}" --nbexecs "${nbexecs[$k]}" --data-src hpcc_0.5; k=$(($k+1)); done; done

## [20190131]:

*

. activate pse-env; cd $REPS/PytrolSimEditor/; git pull; rsync -az --exclude=.git --delete $REPS/PytrolSimEditor/ $RUN/PytrolSimEditor/; cd $RUN/PytrolSimEditor/; python main4.stats.py

## [20190523]:

*

. activate pse-env; cd $REPS/PytrolSimEditor/; git pull; rsync -az --exclude=.git --delete $REPS/PytrolSimEditor/ $RUN/PytrolSimEditor/; cd $RUN/PytrolSimEditor/; python main4.stats.py

## [20190526]:

* Generation of the on-vertex binary positions, on-vertex individual and on-vertex global idlenesses of HPCC 0.5:

. activate pse-env; i=2; cd $REPS/Pytrol/; git pull; rsync -az --exclude=.git --delete $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/PytrolSimEditor/; git pull; rsync -az --exclude=.git --delete $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd ~/Run"$i"/PytrolSimEditor/; k=0; execs=(2000 1000 667 400); for n in 5 10 15 25; do for m in islands map_a grid corridor circle map_b; do python main2-2.3d-idls2bin-vidls.py --nagts "$n" --map "$m" --nbexecs ${execs[k]} --dirpath-logs-vidls ~/Run"$i"/PytrolSimEditor/logs//logs-vidls/ --dirpath-logs-viidls ~/Run"$i"/PytrolSimEditor/logs//logs-viidls/ --dirpath-logs-bin ~/Run"$i"/PytrolSimEditor/logs/logs-bin/ --data-src hpcc_0.5 &>> ~/Run"$i"/PytrolSimEditor/tmp."$m"."$n".log; done; k=$(($k + 1)); done

## [20190526]:

*

. activate pse-env; i=; cd $REPS/Pytrol; git pull ; rsync -az --delete --exclude=.git $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/MAPTrainer/; git pull; rsync -az --delete --exclude=.git $REPS/MAPTrainer/ ~/Run"$i"/MAPTrainer/; cd $REPS/PytrolSimEditor/; git pull; rsync -a --delete --exclude=.git $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd ~/Run"$i"/PytrolSimEditor/; python main4.stats.py

## [20190526]:

* Computing of the topologies' features

. activate pse-env; i=3; mkdir -p ~/Run"$i"/; cd $REPS/Pytrol; git pull ; rsync
 -az --delete --exclude=.git $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/MAPTrainer/; git pull; rsync -az --delete --exclude=.git $REPS/MAPTrainer/ ~/Run"$i"/MAPTrainer/; cd $REPS/PytrolSimEditor/; git pull; rsync -a --delete --exclude=.git $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd ~/Run"$i"/PytrolSimEditor/; python main3.map2binEdges.py

## [20190625]:

* Generations of data for the scenario {A, 15}:

 . activate pse-env; i=; cd $REPS/Pytrol/; git pull; rsync -az --exclude=.git --delete $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/PytrolSimEditor/; git pull; rsync -az --exclude=.git --delete $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd ~/Run"$i"/PytrolSimEditor/; python main2-2.3d-idls2bin-vidls.py --nagts 15 --map map_a --nbexecs 667 --dirpath-logs-vidls logs//logs-vidls/ --dirpath-logs-viidls logs//logs-viidls/ --dirpath-logs-bin logs/logs-bin/ --data-src hpcc_0.5

 ## [20190625]:

* Generations of data for all scenarios

. activate pse-env; i=; cd $REPS/Pytrol/; git pull; rsync -az --exclude=.git --delete $REPS/Pytrol/ ~/Run"$i"/Pytrol/; cd $REPS/PytrolSimEditor/; git pull; rsync -az --exclude=.git --delete $REPS/PytrolSimEditor/ ~/Run"$i"/PytrolSimEditor/; cd ~/Run"$i"/PytrolSimEditor/; k=0; execs=(2000 1000 667 400); for n in 5 10 15 25; do for m in islands map_a grid corridor circle map_b; do python main2-2.3d-idls2bin-vidls.py --nagts "$n" --map "$m" --nbexecs ${execs[k]} --dirpath-logs-vidls logs//logs-vidls/ --dirpath-logs-viidls logs//logs-viidls/ --dirpath-logs-bin logs/logs-bin/ --data-src hpcc_0.5 &>> ~/Run"$i"/PytrolSimEditor/tmp."$m"."$n".log; done; k=$(($k + 1)); done

