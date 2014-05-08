psawsvg
=======

NEW: Currently behind from the newst features of the psaw. Please be advised that this might fail, and that i don't have time to edit it :/

An inkscape extension written in python to help you add photonsaw attributes to SVG layers created in inkscape.

This script runs on all top-level layers unless you select the "isEngravingLayer" checkbox or when disabling the "All Layer" checkbox.

But that's not a hassle at all, because you have already made several layers which you intend to apply different psaw attributes to... right?

Files
=====

The extension consists of two files:

psawsvg.inx - A descriptor which inkscape uses to create the query box for the plugin.

psawsvg.py - The actual code, which reads the current layer's style attributes and appends the PSAW attributes to it.

If a layer already has PSAW attributes, these are overwritten, so don't worry about duplicate entries.

The 'linepitch' attribute is only written if the engraving layer box is checked. This also overrides the 'passes' attribute, because you don't want several passes in an engraving.

Installation
============
copy the two files into your inkscape extensions dir to:

Linux: ~/.config/inkscape/extensions

Windows: %appdata%\Inkscape\extensions

Mac: ~/.config/inkscape/extensions

Linux/Mac note: Please make sure to have 'psawsvg.py' set to be executable (i.e. chmod a+x psawsvg.py).

NOTE
====
Remember to save your svg file after you have run the extension on all layers. It doesn't auto-save.

~Robotto
