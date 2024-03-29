import os
from pathlib import Path

print( __file__ )
script_location = __file__
examplesDir = Path( os.path.join(script_location, "..") )
print( examplesDir )

examplesDir = examplesDir.resolve()
print( examplesDir )

