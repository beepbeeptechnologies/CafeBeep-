#!/usr/bin/env python

__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Robotic Beverage Technologies Inc"
__status__ =  "Development"
__date__ =    "Late Updated: 2020-04-21"
__doc__ =     "Class to define flavors and health additivies in a CocoDrink"

# Robotic Beverage Technologies code for custom data logging and terminal debugging output
from Debug import *

# Robotic Beverage Technologies code for controlling many different types of motors, servos, and relays
from Actuator import *

# Robotic Beverage Technologies code for controlling the physical movement and power output of a LASER
#TODO from LASER import *

class CocoDrink:

    # Drink Name CONSTANTS
	NONE = 0
	NO_DRINK = 0
	IMMUNITY_BOOST = 1
	DAILY_VITAMINS = 2
	RUM_FLAVOR = 3
	PINA_COLADA = 4
	PINEAPPLE_FLAVOR = 5
	ORANGE_FLAVOR = 6
	MAX_DRINK_NAME = ORANGE_FLAVOR
    
    # Extra add-ons for v2021.0
	CBD = 7
	ENERGY_BOOST = 8
	ORGINAL_RED_BULL = 9
    
    # Add-On level CONSTANTS 
	MAX_ADD_ON_LEVEL = 5
	MIN_ADD_ON_LEVEL = 0
	
	
	def __init__(self, drinkName, addOnFlavor, addOnFlavorLevel, addOnHealthAdditive, addOnHealthAdditiveLevels, brandingArt):
		"""
		Constructor to initialize an CocoDrink object

        Key arguments:
        self -- Newly created CocoDrink object
	    drinkName -- CONSTANT product name of drink (e.g. IMMUNITY_BOOST, PINA_COLADA, etc)
        addOnFlavor -- CONSTANT product name of flavoring being added to base drink
	    addOnFlavorLevel -- The unit step amount of flavor to be added to a drink from 0 to MAX_ADD_ON_LEVEL 
							Each unit is a different but constant volume (in milliLiters) for each flavor
        addOnHealthAdditive -- CONSTANT product name of  health additive being added to base liquid   
        addOnHealthAdditiveLevel -- The unit step amount of additive to be added to a drink from 0 to MAX_ADD_ON_LEVEL
									Each discrete unit is a differnt but constant volume (in milliLiters) for each additive
		brandingArt -- PNG image to LASER brand onto the side of the coconut (max size is 200 MB or ? x ? pixels / ? x ? inches)							
    
        Return value:
        Newly created CocoDrink() object  
        """
		
		self.DebugObject = Debug(True)
		
		self.drinkName = drinkName
		self.addOnFlavor = addOnFlavor
		self.addOnFlavorLevel = addOnFlavorLevel
		self.addOnHealthAdditive = addOnHeathAdditive
		self.addOnHealthAdditiveLevel = addOnHealthAdditiveLevel
		self.brandingArt = brandingArt
        
		if(addOnFlavorLevel > MAX_ADD_ON_LEVEL or addOnHealthAdditiveLevel > MAX_ADD_ON_LEVEL):
			Debug.Dprint(DebugObject, "OBJECT CREATION ERROR: You created a CocoDrink() object with add-on level greater then " + MAX_ADD_ON_LEVEL)
			__exit__() # Destructor / memory clean up
	
		if(addOnFlavorLevel < 0 or addOnHewlthAdditiveLevel < 0):
			Debug.Dprint(self.DebugObject, "OBJECT CREATION ERROR: You created a CocoDrink() object with add-on level less then " + MIN_ADD_ON_LEVEL)
			__exit__() # Destructor / memory clean up
				
		if(NO_DRINK > drinkName or drinkName > MAX_DRINK_NAME):
			Debug.Dprint(DebugObject, "OBJECT CREATION ERROR: You created a CocoDrink() object with a frink name that doesn't exist. Why did you do that genius?")
			__exit__() # Destructor / memory clean up
				
				
	###
	#
	#
    # @self - Instance of object being called
	#
	# return object that created exception
	####

	def __enter__(self):
		"""
		The 'with' statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed. 
		Key arguments:
		self -- 
		https://docs.python.org/2.5/whatsnew/pep-343.html
		https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
		"""
		
		print("in __enter__")
		return self


	def __exit__(self, exception_type, exception_value, traceback):
		"""
		Memory cleanup
	
		Key arguments:
		self --
		exception_type -- 
		exception_value -- 
		traceback -- 
		"""
		
		Debug.Dprint(self.DebugObject, "Cleaning up CocoDrink() object in __exit__ ")

	
	def GetFlavorType(self):
		"""
		Get product name of flavoring 
	
    	Key arguments:
    	self -- Instance of object being called
      
    	Return value:
    	return Integer GLOBAL CONSTANT from CocoDrink.py
		"""
		
		return self.addOnFlavor

 
	def GetHealthAdditiveType(self):
		"""
		Get product name of additive fluid 
	
    	Key arguments:
    	self -- Instance of object being called
      
    	Return value:
    	return Integer GLOBAL CONSTANT from CocoDrink.py
		"""
		
		return self.addOnHealthAdditive


	def GetLaserArtType(self):
		"""
		Get filename of logo LASER branding into coconut 
	
    	Key arguments:
    	self -- Instance of object being called
      
    	Return value:
    	return String GLOBAL CONSTANT from CocoDrink.py 
		"""
		
		return self.brandingArt


	def GetFlavorLevel(self):
		"""
		Get amount / level of flavor fluid in a coco drink in User Interface units 
	
    	Key arguments:
    	self -- Instance of object being called
      
    	Return value:
    	return Integer value between 0 and  MAX_ADD_ON_LEVEL inclusively 
		"""
		
		return self.addOnFlavorLevel

	def ConvertLevelToVolume(self, addOnUnits):
		"""
		Since each fluid has a different flavor or health effect strength per mL this function defined what the User Interface units of mean
	
		Key arguments:
		addOnUnits -- Integer between and 0 and MAX_ADD_ON_LEVEL (inclusive)
	
		Reture value:
		volume - In units of mL for pumps to dispense 
		"""
		
		if(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilliLiterFactor = 15
		elif(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilliLiterFactor = 13.3
		elif(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilloiiterFactor = 12
		elif(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilliLiterFactor = 19
		elif(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilliLiterFactor = 3
		elif(self.drinkName == IMMUNITY_BOOST):
			oneUnitToMilliLiterFactor = 9
		else:
			Debug.Dprint(self.DebugObject, "ERROR CODE (0x" + GLOBAL_CONSTANT_USAGE_ERROR + ") Verfiy that this Tapomatic unit has " + self.drinkName + " stocked.")
		
		volume = addOnUnits * oneUnitToMilliLeterFactor
		return volume
		
		
	def ConvertVolumeToPumpRunTime(volume, pumpPartNumber):
		"""
		Since each pump has a different flow rate(mL/Sec) this function defined how long each pump type should stay on to dispense an exact (~2 ml variance) of fluid. fudgeFactor variable enable "THICK BOI" (Search Google) fluids to be dispenses currently  
	
		Key Paramters:
		volume -- The requested volume that pump should dispense in units of milliLiters
		pumpPartNumber -- CocoTaps 8 character part number (e.g. 202-000N) as defines in Actuator.py
	
		Return value:
		seconds -- The amount of time a pump should operate to dispense the correct amount of fluid
		"""
		thiccBoiFactor = 1 # Set to default value
		
		if(pumpPartNumber == "202-0006-A"):
			oneMilloLiterToSecondFactor = 2.2
		else:
			Debug.Dprint(self.DebugObject, "ERROR CODE (0x" + PUMP_CONFIGURATION_ERROR + ") Verify that you are using the correct pump part nuumber, as defined in Actuator.py and CocoDrink.py")
			
		if(self.drinkName == PINA_COLADA):
			thiccBoiFactor = 1.75			# This flavoring is extra thick, pump longer to get correct volume
		
		seconds = volume * oneMilloLiterToSecondFactor * thiccBoiFactor
		return seconds 
		
       
	def GetHealthAdditiveLevel(self):
		"""
		Get amount / level of health additive fluid in a coco drink in User Interface units

    	Key arguments:
    	self -- Instance of object being called
      
	    Return value:
	    return Integer value between 0 and  MAX_ADD_ON_LEVEL (inclusive) 
		"""
	
		return self.addOnHealthAdditiveLevel
				
				
				