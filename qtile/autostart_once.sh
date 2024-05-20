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

#run "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"
 #run "picom" -b
 #redshift -P -O 5000
 #run "greenclip" daemon
 ## run "xsettingsd"