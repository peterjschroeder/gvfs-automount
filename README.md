gvfs_automount
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

    gvfs_automount >/dev/null &

If you use i3, you can add something like this to your `.i3/config` instead:

    exec --no-startup-id gvfs_automount >/dev/null

