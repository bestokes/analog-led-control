#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "</head><body>"

# command to set pin value
SETPIN="/usr/local/bin/pigs p "

# define pins
RED=17 ; GREEN=22 ; BLUE=24

# set some ramdon values
RVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])
GVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])
BVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])

# kill any running sequence
rm -f /lockfiles/*

if [ "$QUERY_STRING" = "blue" ]; then
      lockfile=$(mktemp --tmpdir=/lockfiles/)
      touch $lockfile
      /usr/local/bin/pigs p $RED 0
      /usr/local/bin/pigs p $GREEN 0
      while [ -f $lockfile ]; do
        for STEP in 5 10 20 10 5; do
          for VALUE in $(seq 1 $STEP 255); do
            /usr/local/bin/pigs p $BLUE $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            /usr/local/bin/pigs p $BLUE $VALUE ;
          done
        done
      done &
elif [ "$QUERY_STRING" = "green" ]; then
      /usr/local/bin/pigs p $RED 0
      /usr/local/bin/pigs p $BLUE 0
      lockfile=$(mktemp --tmpdir=/lockfiles/)
      touch $lockfile
      while [ -f $lockfile ]; do
        for STEP in 5 10 20 10 5; do
          for VALUE in $(seq 1 $STEP 255); do
            /usr/local/bin/pigs p $GREEN $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            /usr/local/bin/pigs p $GREEN $VALUE ;
          done
        done
      done &
elif [ "$QUERY_STRING" = "red" ]; then
      /usr/local/bin/pigs p $BLUE 0
      /usr/local/bin/pigs p $GREEN 0
      lockfile=$(mktemp --tmpdir=/lockfiles/)
      touch $lockfile
      while [ -f $lockfile ]; do
        for STEP in 5 10 20 10 5; do
          for VALUE in $(seq 1 $STEP 255); do
            /usr/local/bin/pigs p $RED $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            /usr/local/bin/pigs p $RED $VALUE ;
          done
        done
      done &
elif [ "$QUERY_STRING" = "party" ]; then
      lockfile=$(mktemp --tmpdir=/lockfiles/)
      touch $lockfile
      while [ -f $lockfile ]; do
        RNewVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$RNew VALUE " -ge "$RVALUE " ]; then
          for VALUE in $(seq $RNewVALUE  -2 $RVALUE ); do /usr/local/bin/pigs p $RED $VALUE ; done
        else
          for VALUE in $(seq $RNewVALUE  2 $RVALUE ); do /usr/local/bin/pigs p $RED $VALUE ; done
        fi
        RVALUE=$RNewVALUE
        BNewVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$BNew VALUE " -ge "$BLUE VALUE " ]; then
          for VALUE in $(seq $BNewVALUE  -2 $BVALUE ); do /usr/local/bin/pigs p $BLUE $VALUE ; done
        else
          for VALUE in $(seq $BNewVALUE  2 $BVALUE ); do /usr/local/bin/pigs p $BLUE $VALUE ; done
        fi
        BVALUE=$BNew VALUE
        GNewVALUE=$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$GNew VALUE " -ge "$GREEN VALUE " ]; then
          for VALUE in $(seq $GNewVALUE  -2 $GVALUE ); do /usr/local/bin/pigs p $GREEN $VALUE ; done
        else
          for VALUE in $(seq $GNewVALUE  2 $GVALUE ); do /usr/local/bin/pigs p $GREEN $VALUE ; done
        fi
        GVALUE=$GNewVALUE
      done &
elif [ "$QUERY_STRING" = "random" ]; then
      /usr/local/bin/pigs p $RED $RVALUE
      /usr/local/bin/pigs p $GREEN $GVALUE
      /usr/local/bin/pigs p $BLUE $BVALUE
elif [ "$QUERY_STRING" = "off" ]; then
      /usr/local/bin/pigs p $RED 0
      /usr/local/bin/pigs p $BLUE 0
      /usr/local/bin/pigs p $GREEN 0
fi
