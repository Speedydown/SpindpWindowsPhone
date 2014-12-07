try:
    import spidev
except:
    print "could not load SPIDEV"

import time

class GetSpiData:
        def __init__(self):
            try:
                self.spi = spidev.SpiDev()
                self.spi.open(0, 0)
            except:
                pass


        # read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
        def readadc(self, adcnum):
                if ((adcnum > 7) or (adcnum < 0)):
                        return -1
                r = self.spi.xfer2([1,(8+adcnum)<<4,0])
                adcout = ((r[1]&3) << 8) + r[2]
                return adcout

        def getSpi(self):
            try:
                spiData = '%d' %(self.readadc(0))
                return spiData
            except:
                return "could not read SPI"
