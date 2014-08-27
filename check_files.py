#!/usr/bin/python

import os
import shutil
#import time

print('Script: check_files.py')

# Verzeichnisse, die untersucht werden sollen
a_currentDirectory = '.'
a_testDirectory = 'testing' 
a_testTree = 'Testverzeichnisstruktur'

a_sourceTrees = [ os.path.join( a_currentDirectory, a_testDirectory, a_testTree ), 'C:\\tmp' ]
#print( 'Type of a_sourceTrees: {0}' .format( type( a_sourceTrees ) ) )

# Strings, nach denen gesucht werden soll
a_searchStrings = ( 'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü' )
print( 'Searchstrings:' )
for a_eachString in a_searchStrings:
    print( a_eachString, end = ' ' )   # end = ' ' --> Zeilenumbruch unterduecken
print( '' )                            # Leere Zeile ausgeben erzeugt nur eien Zeilenumbruch

# Daten sollen in folgender Datei gespeichert werden
a_targetFile = os.path.join( a_currentDirectory, 'result.log' )
a_fobjOut = open( a_targetFile ,"w" )

#print('os.listdir:')
#print( os.listdir( a_sourceTrees[ 0 ] ) )

#print('os.walk:')
#for a_each in os.walk( a_sourceTrees[ 0 ] ):
#    print( a_each )
#    print( 'Type of a_each: {0}' .format( type( a_each ) ) )
    
for a_root, a_dirs, a_files in os.walk( a_sourceTrees[ 0 ] ):
    for a_filename in a_files:
        a_rootWithFilenames = os.path.join( a_root, a_filename) 
        for a_eachString in a_searchStrings:
            if a_eachString in a_filename:
                print( a_rootWithFilenames )
                a_fobjOut.write( a_rootWithFilenames + '\n' )
        #print( 'Type of a_rootWithFilenames: {0}' .format( type( a_rootWithFilenames ) ) )
    for a_dirname in a_dirs:
        a_rootWithDirnames = os.path.join( a_root, a_dirname)
        for a_eachString in a_searchStrings:        
            if a_eachString in a_dirname:        
                print( a_rootWithDirnames )
                a_fobjOut.write( a_rootWithDirnames + '\n' )

a_fobjOut.close()

