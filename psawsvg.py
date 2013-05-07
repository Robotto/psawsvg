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
        self.OptionParser.add_option('-p', '--passes', action = 'store', type = 'string', dest = 'passes', default = '2', help = 'Enter number of passes')
        self.OptionParser.add_option('-s', '--speed', action = 'store', type = 'string', dest = 'speed', default = '20', help = 'Enter speed in mm/sec')
        self.OptionParser.add_option('-P', '--power', action = 'store', type = 'string', dest = 'power', default = '80', help = 'Enter power in watts from 0 to 80')
        self.OptionParser.add_option('-a', '--assistair', action = 'store', type = 'inkbool', dest = 'assistair', default = True, help = 'Assistair on/off')
        self.OptionParser.add_option('-e', '--isEngravingLayer', action = 'store', type = 'inkbool', dest = 'isEngravingLayer', default = False, help ='Is the current layer intended for engraving?')
        self.OptionParser.add_option('-l', '--linepitch', action = 'store', type = 'string', dest = 'linepitch', default = '0.1', help = 'Enter raster linepitch in mm/pixel')
        
        


    def effect(self):

        # Get the option values.
        passes = self.options.passes
        speed = self.options.speed
        power = self.options.power
        assistair = self.options.assistair

        isEngravingLayer = self.options.isEngravingLayer
        linepitch = self.options.linepitch


        #Get old style:
        currentstyle = parseStyle(self.current_layer.get('style'))
        
        #inkex.debug(currentstyle)

        psawstyle = {'photonsaw-speed' : speed, 'photonsaw-power': power, 'photonsaw-assistair' : assistair, 'photonsaw-passes' : passes}

        if isEngravingLayer:
          psawstyle.update({'photonsaw-passes' : '1', 'photonsaw-linepitch' : linepitch})
          


        currentstyle.update(psawstyle)

        self.current_layer.set('style', formatStyle(currentstyle))
        
        
# Create effect instance and apply it.
effect = PSAWsvg()
effect.affect()
