#!/bin/bash

# Apply wallpaper using wal
#wal -R &
nitrogen --restore
# Start picom
picom --config ~/.config/picom/picom.conf &
#start flameshot
flameshot &
#start nm-applet
nm-applet &
#start fcitx5
#fcitx5 &
copyq &
