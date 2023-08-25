from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import colors

mod = "mod4"
terminal = "kitty"

colors = colors.MyColor

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Custom key binding
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Run rofi drun mode"),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='volume mute'),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master mute"), desc='volume mute'),

    Key([mod], "s", lazy.spawn('flameshot gui'), desc='Open flameshot gui'),
    Key([mod], "x", lazy.spawn('betterlockscreen -l'), desc='Lock screen'),
]

# groups = [Group(f"{i+1}", label="󰏃") for i in range(8)]
groups = [
    Group('1', label='', layout='monadtall'),
    Group('2', label='', matches=[Match(wm_class='firefox')]),
    Group('3', label='', matches=[Match(wm_class='Google-chrome')]),
    Group('4', label='', layout='monadtall', matches=[Match(wm_class='jetbrains-idea')]),
    Group('5', label='󰎙', layout='monadtall', matches=[Match(wm_class='jetbrains-webstorm')]),
    Group('6', label='', layout='monadtall', matches=[Match(wm_class='jetbrains-pycharm')]),
    Group('7', label='', layout='monadtall'),
    Group('8', label='', layout='monadtall', matches=[Match(wm_class='GitKraken')]),
    Group('9', label='', layout='monadtall',
          matches=[Match(wm_class='Slack'), Match(wm_class='Skype'), Match(wm_class='TelegramDesktop')]),
    Group('0', label='󰨇', matches=[Match(wm_class='Virt-manager')]),
    Group('a', label='󰨇', matches=[Match(wm_class='parsecd')])
]
for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #    [mod, "shift"],
            #    i.name,
            #    lazy.window.togroup(i.name, switch_group=True),
            #    desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Tile(margin=5),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.TreeTab(
        font="Ubuntu Bold",
        fontsize=11,
        border_width=0,
        bg_color=colors[0],
        active_bg=colors[6],
        active_fg=colors[1],
        inactive_bg=colors[1],
        inactive_fg=colors[2],
        padding_left=8,
        padding_x=8,
        padding_y=6,
        sections=["ONE", "TWO", "THREE"],
        section_fontsize=10,
        section_fg=colors[6],
        section_top=15,
        section_bottom=15,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
]

widget_defaults = dict(
    font="san",
    fontsize=15,
    padding=0,
)
extension_defaults = widget_defaults.copy()


###CUSTOM SCRIPT MOUSE CLICK CALL
@lazy.function
def power(qtile):
    qtile.cmd_spawn("sh -c /home/baoanh/.config/rofi/scripts/power")


@lazy.function
def calendar(qtile):
    qtile.cmd_spawn("sh -c /home/baoanh/personal/scripts/calendar2")


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/Assets/launch_Icon.png',
                    margin=2,
                    mouse_callbacks={"Button1": power},
                ),
                widget.GroupBox(
                    fontsize=15,
                    margin_y=3,
                    margin_x=4,
                    padding_y=2,
                    padding_x=1,
                    borderwidth=8,
                    active=colors[4],
                    inactive=colors[1],
                    rounded=False,
                    highlight_method="block",
                    urgent_alert_method="block",
                    urgent_border=colors[3],
                    urgent_text=colors[3],
                    disable_drag=True,
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[6],

                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    foreground=colors[1],
                    padding=2,
                    fontsize=14
                ),
                widget.CurrentLayoutIcon(
                    # custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[1],
                    padding=0,
                    scale=0.7
                ),
                widget.CurrentLayout(
                    foreground=colors[1],
                    font="JetBrains Mono Bold",
                    padding=5
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    foreground=colors[1],
                    padding=2,
                    fontsize=14
                ),
                widget.WindowName(
                    format="{name}",
                    font='JetBrains Mono Bold',
                    foreground=colors[6],
                    empty_group_string='Desktop',
                    fontsize=13,
                ),
                widget.Systray(
                    fontsize=2,
                    padding=7,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    foreground=colors[1],
                    padding=2,
                    fontsize=14
                ),
                widget.Memory(
                    fmt='🖥  Mem: {} used',
                    format='{MemUsed: .0f}{mm}',
                    foreground=colors[1],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    foreground=colors[1],
                    padding=2,
                    fontsize=14
                ),
                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    fmt='🕫  Vol: {}',
                    theme_path='~/.config/qtile/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                ),
                widget.Spacer(
                    length=-5,
                ),
                widget.Volume(
                    font='JetBrains Mono Bold',
                    foreground=colors[1],
                    fontsize=13,
                ),
                widget.TextBox(
                    text='|',
                    font="Ubuntu Mono",
                    foreground=colors[1],
                    padding=2,
                    fontsize=14
                ),
                widget.Clock(
                    format='⏱  %I:%M %p',
                    foreground=colors[1],
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    mouse_callbacks={'Button1': calendar},
                ),
            ],
            size=32,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

from libqtile import hook
# some other imports
import os
import subprocess


# stuff
@hook.subscribe.startup_once
def autostart_once():
    subprocess.run('/home/baoanh/.config/qtile/autostart_once.sh')  # path to my script, under my user directory
    subprocess.call([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
