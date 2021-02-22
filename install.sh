#!/bin/bash

BASEDIR=/opt/wlanpi-chat-bot
CONFIG_FILE=/opt/wlanpi-chat-bot/etc/config.json

if [ "$1" == '-r' ]; then
    echo "Removing WLAN Pi Chat bot..."
    sudo systemctl disable wlanpi-chat-bot.service
    sudo rm /lib/systemd/system/wlanpi-chat-bot.service
    sudo systemctl reset-failed
    sudo rm -rf $BASEDIR
    echo "Removed."
else
    echo "Installing WLAN Pi Chat bot..."
    sudo mkdir -p $BASEDIR
    sudo cp wlanpi-chat-bot $BASEDIR

    sudo cp -R ./transports $BASEDIR
    sudo cp -R ./utils $BASEDIR
    sudo cp -R ./etc $BASEDIR
    sudo cp -R ./wlanpi_commands $BASEDIR

    sudo chmod +x $BASEDIR/wlanpi-chat-bot

    # prompt user for app key
    read -p 'Please enter your bot token: ' TOKEN
    sed -i "s/\"bot_token\"\: \"\",/\"bot_token\"\: \"$TOKEN\",/" $CONFIG_FILE


    cd ./scripts
    sudo install -p -m 644 wlanpi-chat-bot.service /lib/systemd/system/wlanpi-chat-bot.service
    sudo systemctl enable wlanpi-chat-bot.service
    sudo systemctl start wlanpi-chat-bot.service
    echo "Bot service status:"
    echo ""
    echo "=============================================================="
    sudo systemctl status wlanpi-chat-bot.service
    echo "=============================================================="
fi

# sudo systemctl disable wlanpi-chat-bot.service
# sudo rm /lib/systemd/system/wlanpi-chat-bot.service
# sudo systemctl reset-failed
# sudo systemctl status wlanpi-chat-bot.service
