import objc, Quartz
from AppKit import NSBitmapImageRep
from Quartz.CoreGraphics import CGMainDisplayID

# Big big thanks to https://bitbucket.org/ronaldoussoren/pyobjc/ for updated .bridgesupport files
# And also this particular message that showed how to use them:
# http://www.mail-archive.com/pythonmac-sig@python.org/msg09749.html

# Import the definition for CGDisplayCreateImageForRect
objc.parseBridgeSupport( """<?xml version='1.0'?>
<!DOCTYPE signatures SYSTEM "file://localhost/System/Library/DTDs/BridgeSupport.dtd">
<signatures version='1.0'>
  <depends_on path='/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation' />
  <depends_on path='/System/Library/Frameworks/IOKit.framework/IOKit' />
  <depends_on path='/System/Library/Frameworks/CoreServices.framework/CoreServices' />
  <function name='CGDisplayCreateImageForRect'>
    <retval already_cfretained='true' type='^{CGImage=}' />
    <arg type='I' />
    <arg type='{CGRect={CGPoint=ff}{CGSize=ff}}' type64='{CGRect={CGPoint=dd}{CGSize=dd}}' />
  </function>
</signatures>
""", globals(), '/System/Library/Frameworks/ApplicationServices.framework/Frameworks/CoreGraphics.framework')

mainID = CGMainDisplayID()
# Grab a chunk of the screen from 0,0 to 100,100 from top left
image = CGDisplayCreateImageForRect(mainID, ((0,0), (100,100)))
bitmap = NSBitmapImageRep.alloc()
bitmap.initWithCGImage_(image)
# Get the RGB color (float values from 0 to 1 per color, plus alpha) at a particular point
bitmap.colorAtX_y_(93.484375, 60.4921875)

