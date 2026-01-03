gvfs_automount.py
=========

Overview
--
 
Automatically mounts removable media (eg: CD-ROMS, USB-drives, etc.) upon
insertion/connection. Also generates a desktop notification when it mounts
something.


Usage
--

It's a good idea to pipe stdout to a file or to `/dev/null`, as Python tends to
freak out if stdout gets closed. From something like an .xsession file you'd
want to do something like:

    ~/bin/gvfs_automount.py >/dev/null &

If you use i3, like I do, you can add something like this to your `.i3/config`
instead:

    exec --no-startup-id ~/bin/gvfs_automount.py >/dev/null

(These both assume you've put the script in ~/bin -- adjust the path
accordingly.)
