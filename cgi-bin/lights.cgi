#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "</head><body>"

# command to set pin value
SETPIN="pigs p "

# define pins
RED=17 ; GREEN=22 ; BLUE=24

# set some ramdon values
RVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])
GVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])
BVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])

# kill any running sequence
rm -f /tmp/*.lights.lock

case ${QUERY_STRING} in;
  blue)
      $SETPIN $RED 0
      $SETPIN $GREEN 0
      lockfile=$(mktemp).lights.lock
      touch $lockfile
      while [ -f $lockfile ]; do
        for STEP in 1 5 10 20 10 5 1; do
          for VALUE in $(seq 1 $STEP 255); do
            $SETPIN $BLUE $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            $SETPIN $BLUE $VALUE ;
          done
        done
      done &
  ;;
  green)
      $SETPIN $RED 0
      $SETPIN $BLUE 0
      lockfile=$(mktemp).lights.lock
      touch $lockfile
      while [ -f $lockfile ]; do
        for STEP in 1 5 10 20 10 5 1; do
          for VALUE in $(seq 1 $STEP 255); do
            $SETPIN $GREEN $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            $SETPIN $GREEN $VALUE ;
          done
        done
      done &
  ;;
  red)
      $SETPIN $BLUE 0
      $SETPIN $GREEN 0
      lockfile=$(mktemp).lights.lock
      touch $lockfile
      while [ -f $lockfile ]; do
        for STEP in 1 5 10 20 10 5 1; do
          for VALUE in $(seq 1 $STEP 255); do
            $SETPIN $RED $VALUE ;
          done;
          for VALUE in $(seq 255 -$STEP 1); do
            $SETPIN $RED $VALUE ;
          done
        done
      done &
  ;;
  party)
      lockfile=$(mktemp).lights.lock
      touch $lockfile
      while [ -f $lockfile ]; do
        RNewVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$RNew VALUE " -ge "$RED VALUE " ]; then
          for VALUE in $(seq $RNewVALUE  -2 $RED VALUE ); do $SETPIN $RED $VALUE ; done
        else
          for VALUE in $(seq $RNewVALUE  2 $RED VALUE ); do $SETPIN $RED $VALUE ; done
        fi
        RVALUE =$RNewVALUE
        BNewVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$BNew VALUE " -ge "$BLUE VALUE " ]; then
          for VALUE in $(seq $BNewVALUE  -2 $BLUE VALUE ); do $SETPIN $BLUE $VALUE ; done
        else
          for VALUE in $(seq $BNewVALUE  2 $BLUE VALUE ); do $SETPIN $BLUE $VALUE ; done
        fi
        BVALUE =$BNew VALUE
        GNewVALUE =$(echo $[ 1 + $[ RANDOM % 255 ]])
        if [ "$GNew VALUE " -ge "$GREEN VALUE " ]; then
          for VALUE in $(seq $GNewVALUE  -2 $GREEN VALUE ); do $SETPIN $GREEN $VALUE ; done
        else
          for VALUE in $(seq $GNewVALUE  2 $GREEN VALUE ); do $SETPIN $GREEN $VALUE ; done
        fi
        G VALUE =$GNewVALUE
      done &
  ;;
  random)
      $SETPIN $RED $RVALUE
      $SETPIN $GREEN $GVALUE
      $SETPIN $BLUE $BVALUE
  ;;
  off)
      sleep 3 # allows running patterns to finish first
      $SETPIN $RED 0
      $SETPIN $BLUE 0
      $SETPIN $GREEN 0
  ;;
esac  
