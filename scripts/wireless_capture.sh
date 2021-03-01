###########################################
# Capture of wireless frames using tcpdump
###########################################
LOG_FILE="/var/log/wireless_cap.log"

CHANNEL=$1
# values: HT20, HT40-, HT40+, 80MHz
WIDTH=$2
WLAN_IF=$3
DURATION=$4
DUMP_FILE=/tmp/wlandump.pcap

echo "Starting wireless capture" >  $LOG_FILE 

# kill old instances of tcpdump
echo "Killing old instances of tcpdump..." >>  $LOG_FILE 
#if [ `pidof tcpdump` ]; then
#    sudo kill -9 `pidof tcpdump`
#fi;

# kill old instances of tshark
echo "Killing old instances of tshark..." >>  $LOG_FILE 
if [ `pidof tshark` ]; then
    sudo kill -9 `pidof tskark`
fi;

# take the wlan interface down
echo "Taking down interface $WLAN_IF..." >>  $LOG_FILE
sudo ifconfig $WLAN_IF down >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue taking wlan interface down" | tee -a $LOG_FILE 
    exit 1
fi

# set monitor mode
echo "Setting monitor mode for $WLAN_IF..." >>  $LOG_FILE
sudo iw dev $WLAN_IF set type monitor >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue setting wlan interface to monitor" | tee -a $LOG_FILE 
    exit 1
fi
echo ""
iwconfig >>  $LOG_FILE 2>&1
echo ""

# bring wlan interface back up
echo "Bringing up interface $WLAN_IF..." >>  $LOG_FILE
sudo ifconfig $WLAN_IF up >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue bringing wlan interface up" | tee -a $LOG_FILE 
    exit 1
fi

# set channel and width
echo "Setting channel & width for $WLAN_IF: $CHANNEL $WIDTH..." >>  $LOG_FILE
sudo iw $WLAN_IF set channel $CHANNEL $WIDTH >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue setting wlan channel/width" | tee -a $LOG_FILE 
    exit 1
fi

# Have a short sleep, adapters sometimes still scanning 
sleep 5

# run the tcpdump
echo "Running tshark against interface $WLAN_IF..." >>  $LOG_FILE
sudo tshark -i $WLAN_IF -w $DUMP_FILE -a duration:$DURATION >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue running tshark" | tee -a $LOG_FILE 
    exit 1
fi

exit 0