#!/bin/bash

courses=("algo-COMP3760" "pstat-MATH3042")
TOTALWEEKS=3
mkdir hw.main
for c in ${courses[@]}; do
  mkdir $c
done
for d in */; do 
  cd $d 
  mkdir lab && mkdir lecture
  cd lecture
  for ((i = 1; i<=TOTALWEEKS; i++)); do
    mkdir week-$i
    cd week-$i && touch lec.md && touch README.md && cd ..
  done
  cd ..
  cd lab
  for ((i = 1; i<=TOTALWEEKS; i++)); do
    mkdir week-$i
    cd week-$i && touch lec.md && touch README.md && cd ..
  done
  cd ..
  cd ..
done


