#!/usr/bin/env python3

from os import system

###################### CLASS DESCRIPTION #########################

class Water:
    
    def __init__ ( self, volume = 1, temp = 18 ):
        self.set_volume( volume )
        self.set_temp( temp )

    def __str__ ( self ):
        return f"WATER <{self.__volume}> L | <{self.__temp}> C | <{self.__state}> "

## setter & getter for temp ###########
    
    def set_temp( self, temp ):
        if temp > 2000 or temp < -273:
            print( "ERROR!" )
        else:
            self.__temp = temp
            if( temp > 100 ):
                self.__state   = "vapor"
            elif( temp <= 0 ):
                self.__state = "solid"
            else:
                self.__state = "liquid"

    
    def get_temp( self ):
        return self.__temp
## #################################

## setter & getter for volume ###########
    
    def set_volume( self, volume ):
        if self.isNumber( volume ):
            if ( volume <= 0 ):
                print( "ERROR!!" )
            else:
                self.__volume  = volume

        elif ( type( volume ) == str ) and volume in [ "large", "medium", "small" ]:
                if( volume == "large" ):
                    self.__volume = 1000
            
                elif( volume == "medium" ):
                    self.__volume = 100
            
                elif( volume == "small" ):
                    self.__volume = 10
        
    
    def get_volume( self ):
        return self.__volume
## #################################

    def isNumber( self, value ):
        return ( type( value ) == int or type( value ) == float )
###################### CLASS DESCRIPTION #########################


def heet( water, value, deltaTemp = 0 ):
    water.set_volume( value )
    water.set_temp( water.get_temp() + deltaTemp ) 
    print( f"{water.get_temp()} C" )
    print( f"{water.get_volume()} L" )


w = Water()
system( "clear" )
heet( w, 234, 30 )


