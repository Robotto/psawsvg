#!/usr/bin/env python

# These two lines are only needed if you don't put the script directly into
# the installation directory
import sys
sys.path.append('/usr/share/inkscape/extensions')

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

class PSAWsvg(inkex.Effect):
    """
    Example Inkscape effect extension.
    Creates a new layer with a "Hello World!" text centered in the middle of the document.
    """
    def __init__(self):
        """
        Constructor.
        Defines the "--what" option of a script.
        """
        # Call the base class constructor.
        inkex.Effect.__init__(self)

        # Define string option "--what" with "-w" shortcut and default value "World".
        self.OptionParser.add_option('-p', '--passes', action = 'store', type = 'string', dest = 'passes', default = '1', help = 'Enter number of passes')
        self.OptionParser.add_option('-s', '--speed', action = 'store', type = 'string', dest = 'speed', default = '15', help = 'Enter speed in mm/sec')
        self.OptionParser.add_option('-n', '--anylayer', action = 'store', type = 'inkbool', dest = 'anylayer', default = True, help = 'Change all layers at once')
        self.OptionParser.add_option('-r', '--rasterSpeed', action = 'store', type = 'string', dest = 'rasterSpeed', default = 300, help ='Speed of raster engraving, slow=precise, fast=fast')
        self.OptionParser.add_option('-l', '--linepitch', action = 'store', type = 'string', dest = 'linepitch', default = '0.1', help = 'Enter raster linepitch in mm/pixel')




    def effect(self):

        # Get the option values.
        passes = self.options.passes
        speed = self.options.speed
        rasterSpeed = self.options.rasterSpeed
        linepitch = self.options.linepitch


        psawstyle = {'photonsaw-speed' : speed, 'photonsaw-passes' : passes, 'photonsaw-raster-speed' : rasterSpeed, 'photonsaw-raster-pitch' : linepitch}
        #if self.options.isEngravingLayer:
        #    psawstyle.update({'photonsaw-passes' : '1', 'photonsaw-linepitch' : linepitch})

        #inkex.debug(psawstyle)

        if self.options.anylayer:
            gees = self.document.xpath('//svg:g', namespaces=inkex.NSS)
            for g in gees:
                currentstyle = parseStyle(g.get('style'))
                currentstyle.update(psawstyle)
                g.set('style', formatStyle(currentstyle))
        else:
                currentstyle = parseStyle(self.current_layer.get('style'))
                currentstyle.update(psawstyle)
                self.current_layer.set('style', formatStyle(currentstyle))


# Create effect instance and apply it.
effect = PSAWsvg()
effect.affect()
