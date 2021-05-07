#!/usr/bin/env python3

from os import system

class Water:
    
    def __init__ ( self, volume = 0 ):

        if self.isNumber( volume ):
            self.volume  = volume

        elif ( type( volume ) == str ) and volume in [ "large", "medium", "small" ]:
            
            if( volume == "large" ):
                self.volume = 1000
            
            elif( volume == "medium" ):
                self.volume = 100
            
            elif( volume == "small" ):
                self.volume = 10
        
        else:
            print( "ERROR! Wrong volume value!" )



    def __str__ ( self ):
        return f"WATER <{self.volume} L>"

    def __len__( self ):
        return self.volume

## comparation func ##################

    def __gt__ ( self, other ):
        if self.isNumber( other ):
            return self.volume > other
        else:
            return self.volume > other.volume
    
    def __eq__ ( self, other ):
        if self.isNumber( other ):
            return self.volume == other
        else:
            return self.volume == other.volume
    
    def __ne__ ( self, other ):
        if self.isNumber( other ):
            return self.volume != other
        else:
            return self.volume != other.volume
    
## ########################################    
    
    def __add__ ( self, other ):
        return Water( self.volume + other.volume )

    def isNumber( self, value ):
        return ( type( value ) == int or type( value ) == float )


emptyWater = Water()
largeWater = Water( "large" )
largeWater2 = Water( 1000 )
smallWater = Water( 10 )
resultWater = largeWater + smallWater


system( "clear" )
#print( emptyWater ) 
#print( largeWater )
#print( smallWater )
#print( resultWater )

print("COMPARISON RESULTS:")
print( f"Is Large Water < Small Water? >>> {largeWater < smallWater}" )
print( f"Is Large Water 2 == Large Water? >>> {largeWater2 == largeWater}" )
print( f"Is Large Water 2 != Large Water? >>> {largeWater2 != largeWater}" )


