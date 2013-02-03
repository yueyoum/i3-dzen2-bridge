# Icons Bridge for i3status and dzen2

i3status can output lines for dzen2,
But, no icons.

this script simple bridged the i3status and dzen2.

#### original

    i3status | dzen2

#### now

    i3status | ./i3-dzen-bridge.py | dzen2


## install

1.  `git clone https://github.com/yueyoum/i3-dzen2-bridge.git`
2.  make a symbol link for i3dzen2.sh in SYSTEM PATH

    eg. `cd /usr/local/bin; sudo ln -s <PATH>/i3dzen2.sh i3dzen2`



![i3-dzen-bridge-1](http://i1297.photobucket.com/albums/ag23/yueyoum/dzen2-s_zps6c50c408.png)

![i3-dzen-bridge-2](http://i1297.photobucket.com/albums/ag23/yueyoum/dzen2-fullscreen_zps251e2f02.png)

