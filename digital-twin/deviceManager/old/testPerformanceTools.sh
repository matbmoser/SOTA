### calcTestPerformance.sh <inputlog> <outputlog>
# Calculates the parameters to measure the performance
# by: Mathias Brunkow Moser
# © CGI - ALL RIGHTS RESERVED
###


### We use a regular expression to search for variable in file 

## If we want to use a function to get the variable
function getVariable()
{
  grep -oP "(?<=$1=\[).*?(?=\])" $2 --text
}

function getMemoryVariable()
{
  awk -F\| '$3 ~ /^[0-9]*[.][0-9]*$/ {if($3 != ""){print $3}}' $1
}


## If we want to use a function
function getTotalTime()
{
  # Gets every line from stdin passes to seconds and adds it
  awk -F: '
  { 
    n=0; 
    for(i=NF; i>=1; --i) 
      time += $i * 60 ^ n++;
  } END { print time }'
}

## If we want to use a function
function getTotal()
{
  # Gets every line from stdin passes to seconds and adds it
  awk '
  { 
    total+=$1
  } END { print total }'
}

function getNumLines()
{
  # Gets the number of lines
  awk -F: '
    { 
      count++
    } 
    END { print count }'
}




function calcAverage()
{
  # We calculate the average if the second element is not 0, if $2 is 0 a exception is raised by awk
  awk "
  BEGIN{
      print $1/$2
    }
  "
}

function getMinMax(){
  awk '{if(min==""){min=max=$1}; if($1>max) {max=$1}; if($1<min) {min=$1}; total+=$1; count+=1} END {print min,max}'
}


function calcTestCameraPerformance()
{

MEMORY=$(getMemoryVariable $1)
NMESSAGES=$(getVariable nmessages $1)
NMESSAGESSENT=$(getVariable messagesSent $1)
TMPTOTALTIME=$(getVariable totalTime $1)
TMPTOTALCLIENTS=$(getVariable ncameras $1)
TMPTOTALCREATEDCLIENTS=$(getVariable created $1)

TOTALMESSAGESSENT=$(echo "$NMESSAGESSENT" | getTotalTime)
TOTALTIME=$(echo "$TMPTOTALTIME" | getTotalTime)
TMPRECIEVEDTIME=$(getVariable duration $1)
RECIEVEDTIME=$(echo "$TMPRECIEVEDTIME" | getTotalTime)
TOTALNMESSAGES=$(echo "$NMESSAGES" | getTotal)
TOTALCLIENTS=$(echo "$TMPTOTALCLIENTS" | getTotal)
TOTALCREATEDCLIENTS=$(echo "$TMPTOTALCREATEDCLIENTS" | getTotal)
TOTALMEM=$(echo "$MEMORY" | getTotal)

MEMARR=( $(echo "$MEMORY" | getMinMax) )
MINMEM="${MEMARR[0]}"
MAXMEM="${MEMARR[1]}"

# Try to get Min Max variables if they exist
MINSEND=$(getVariable minSendDuration $1)
MAXSEND=$(getVariable maxSendDuration $1)
AVGSEND=$(getVariable avgSendDuration $1)

# Try to get Min Max variables if they exist
MINRECIEVE=$(getVariable mintime $1)
MAXRECIEVE=$(getVariable maxtime $1)
AVGRECIEVE=$(getVariable avgtime $1)

# Get min and max time
TIMEARR=( $(echo "$TMPTOTALTIME" | getMinMax) )
# If they not exist calculate MIN and MAX
if [ -z "$MINSEND"]
then
MINSENDTIME="${TIMEARR[0]}"
else
MINSENDTIME=$MINSEND
fi

if [ -z "$MAXSEND"]
then
MAXSENDTIME="${TIMEARR[1]}"
else
MAXSENDTIME=$MAXSEND
fi

if [ -z "$AVGSEND"]
then
AVGTOTALSENT=$(calcAverage $TOTALTIME $TOTALCREATEDCLIENTS)
else
AVGTOTALSENT=$AVGSEND
fi


if [ -z "$MINRECIEVE"]
then
MINRECIEVETIME="${TIMEARR[0]}"
else
MINRECIEVETIME=$MINRECIEVE
fi

if [ -z "$MAXRECIEVE"]
then
MAXRECIEVETIME="${TIMEARR[1]}"
else
MAXRECIEVETIME=$MAXRECIEVE
fi

if [ -z "$AVGRECIEVE"]
then
AVGTOTALRECIEVE=$(calcAverage $TOTALNMESSAGES $TOTALTIME)
else
AVGTOTALRECIEVE=$AVGRECIEVE
fi

NUMMEMORYLINES=$(echo "$MEMORY" | getNumLines)

## Calculate the average time
AVERAGEMEM=$(calcAverage $TOTALMEM $NUMMEMORYLINES)
Camera=$(echo "$1" | cut -f1 -d"." | cut -c13-)
## Get timestamp
TIMESTAMP=$(date +%s)
## Store the results in the second log
echo '{"timestamp": "'$TIMESTAMP'", "Camera": "'$Camera'", "cameras": "'$TOTALCREATEDCLIENTS'", "camerassent": "'$TOTALCLIENTS'", "messagespersec": "'$AVERAGETIME'", "mintime": "'$MINRECIEVETIME'","avgtime": "'$AVGTOTALRECIEVE'","maxtime": "'$MAXRECIEVETIME'", "totalrecievetime": "'$RECIEVEDTIME'", "minsendtime": "'$MINSENDTIME'","avgsendtime": "'$AVGTOTALSENT'","maxsendtime": "'$MAXSENDTIME'", "totalsendtime": "'$TOTALTIME'", "nmessagesarrived": "'$TOTALNMESSAGES'", "messagessent": "'$TOTALMESSAGESSENT'", "minmemory": "'$MINMEM'", "avgmemory": "'$AVERAGEMEM'", "maxmemory": "'$MAXMEM'", "totalmemory": "'$TOTALMEM'"}'\
>> $2
}


function calcTestServerPerformance()
{
##
MEMORY=$(getMemoryVariable $1)
## Get the total in seconds from the duration
NMESSAGES=$(getVariable nmessages $1)
## Get the total in seconds from the duration
LINES=$(getVariable duration $1)
## Calculate the total duration
TOTALDURATION=$(echo "$LINES" | getTotalTime)
TOTALNMESSAGES=$(echo "$NMESSAGES" | getTotal)
TOTALMEM=$(echo "$MEMORY" | getTotal)

# Try to get Min Max variables if they exist
MIN=$(getVariable mintime $1)
MAX=$(getVariable maxtime $1)
AVG=$(getVariable avgtime $1)
# Get min and max time
TIMEARR=( $(echo "$LINES" | getMinMax) )
# If they not exist calculate MIN and MAX
if [ -z "$MIN"]
then
MINTIME="${TIMEARR[0]}"
else
MINTIME=$MIN
fi

if [ -z "$MAX"]
then
MAXTIME="${TIMEARR[1]}"
else
MAXTIME=$MAX
fi


if [ -z "$AVG"]
then
AVERAGETIME=$(calcAverage $TOTALDURATION $TOTALNMESSAGES)
else
AVERAGETIME=$AVG
fi


MEMARR=( $(echo "$MEMORY" | getMinMax) )
MINMEM="${MEMARR[0]}"
MAXMEM="${MEMARR[1]}"

## Calculate the number of lines
NUMDURATIONLINES=$(echo "$LINES" | getNumLines)
NUMMEMORYLINES=$(echo "$MEMORY" | getNumLines)


AVERAGEMEM=$(calcAverage $TOTALMEM $NUMMEMORYLINES)



## Get timestamp
TIMESTAMP=$(date +%s)

## Store the results in the second log
echo '{"timestamp": "'$TIMESTAMP'", "mintime": "'$MINTIME'", "avgtime": "'$AVERAGETIME'", "maxtime": "'$MAXTIME'", "totaltime": "'$TOTALDURATION'", "messagesprocessed": "'$TOTALNMESSAGES'", "minmemory": "'$MINMEM'", "avgmemory": "'$AVERAGEMEM'", "maxmemory": "'$MAXMEM'", "totalmemory": "'$TOTALMEM'"}'\
>> $2
}



