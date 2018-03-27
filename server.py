import sys, traceback, Ice
import Vocal

class CollI(Vocal.Coll):

    def __init__(self):
        self.collection = []

    def add(self, track, current=None):
        print "Add track: " + track.title
        self.collection.append(track)

    def remove(self, track, current=None):
        print "Remove track"

    def search(self, track, current=None):
        print "Search track"

    def getTrack(self, track, current=None):
        print "Get track"

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("CollAdapter", "default -p 10000")
    object = CollI()
    adapter.add(object, ic.stringToIdentity("Coll"))
    adapter.activate()
    ic.waitForShutdown()
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)