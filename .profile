eval "$(/usr/bin/gnome-keyring-daemon --components=ssh)"
export SSH_AUTH_SOCK


ibus-daemon &


# Added by Toolbox App
export PATH="$PATH:/home/baoanh/.local/share/JetBrains/Toolbox/scripts"
export PATH="$PATH:/home/baoanh/.local/bin"
# Added for clipmenu
export CM_LAUNCHER="rofi"
export CM_MAX_CLIPS=20
export CM_SELECTIONS="clipboard"
export BROWSER="firefox"
