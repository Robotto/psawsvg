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
        self.OptionParser.add_option('-p', '--PSAWpasses', action = 'store',
          type = 'string', dest = 'PSAWpasses', default = '2',
          help = 'Enter number of passes')
        self.OptionParser.add_option('-s', '--PSAWspeed', action = 'store',
          type = 'string', dest = 'PSAWspeed', default = '20',
          help = 'Enter speed in mm/sec')
        self.OptionParser.add_option('-P', '--PSAWpower', action = 'store',
          type = 'string', dest = 'PSAWpower', default = '80',
          help = 'Enter power in watts from 0 to 80')
        self.OptionParser.add_option('-l', '--PSAWlinepitch', action = 'store',
          type = 'string', dest = 'PSAWlinepitch', default = '0.1',
          help = 'Enter raster linepitch in mm/pixel')
        self.OptionParser.add_option('-a', '--PSAWassistair', action = 'store',
          type = 'inkbool', dest = 'PSAWassistair', default = True,
          help = 'Assistair on/off')
        


    def effect(self):

        # Get the option values.
        passes = self.options.PSAWpasses
        speed = self.options.PSAWspeed
        power = self.options.PSAWpower
        linepitch = self.options.PSAWlinepitch
        assistair = self.options.PSAWassistair

        #TODO: GET OLD STYLE AND COMBINE WITH NEW

        style = {'photonsaw-speed' : speed, 'photonsaw-power': power, 'photonsaw-assistair' : assistair, 'photonsaw-passes' : passes}

        self.current_layer.set('style', formatStyle(style))
        
# Create effect instance and apply it.
effect = PSAWsvg()
effect.affect()