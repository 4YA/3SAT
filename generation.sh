#!/bin/fish
mkdir "data n=300,c=1250"
for i in (seq 1000)
	python3 generation.py -v 300 -c 1250 &
    sleep 1
    #fg (jobs -l | awk '{print $1}')
   
    
    ./minisat instance.in >> instance.out;
    #fg
    mkdir "instance $i";
    mv "instance.out" "instance $i";
    mv "instance.in" "instance $i";
    cp -r "instance $i" "data n=300,c=1250"
    rm -r "instance $i"
    echo "Iteration : $i, generation complete.";
    
end


mkdir "data n=200,c=850"
for i in (seq 1000)
	python3 generation.py -v 200 -c 850 &
    sleep 1
    #fg (jobs -l | awk '{print $1}')
   
    
    ./minisat instance.in >> instance.out;
    #fg
    mkdir "instance $i";
    mv "instance.out" "instance $i";
    mv "instance.in" "instance $i";
    cp -r "instance $i" "data n=200,c=850"
    rm -r "instance $i"
    echo "Iteration : $i, generation complete.";
    
end