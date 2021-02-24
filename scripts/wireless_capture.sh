###########################################
# Capture of wireless frames using tcpdump
###########################################
LOG_FILE="/var/log/wireless_cap.log"
WLAN_IF=wlan0
CHANNEL=36
# values: HT20, HT40-, HT40+, 80MHz
WIDTH=HT20
DUMP_FILE=/tmp/wlandump.pcap

echo "Starting wireless capture" >  $LOG_FILE 

# kill old instances of tcpdump
if [ `pidof tcpdump` ]; then
    sudo kill -9 `pidof tcpdump`
fi;

# take the wlan interface down
sudo ifconfig $WLAN_IF down >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue taking wlan interface down" | tee -a $LOG_FILE 
    exit 1
fi

# set monitor mode
sudo iw $WLAN_IF set monitor none >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue setting wlan interface to monitor" | tee -a $LOG_FILE 
    exit 1
fi

# bring wlan interface back up
sudo ifconfig $WLAN_IF up >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue bringing wlan interface up" | tee -a $LOG_FILE 
    exit 1
fi

# set channel and width
sudo iw $WLAN_IF set channel $CHANNEL $WIDTH >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue setting wlan channel/width" | tee -a $LOG_FILE 
    exit 1
fi

# run the tcpdump
sudo tcpdump -i $WLAN_IF -c 100 -w $DUMP_FILE >> $LOG_FILE 2>&1
if [ "$?" != '0' ]; then
    echo "Issue running tcpdump" | tee -a $LOG_FILE 
    exit 1
fi

exit 0