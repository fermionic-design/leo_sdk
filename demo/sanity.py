import sys
import serial

sys.path.append('../include')

from ORION_8G_12G import * 
from SPI import *
    
spi = SPI()
orion = ORION_8G_12G(spi)

orion.DEVICE_ID.read()
print('device_id = '+hex(orion.DEVICE_ID.device_id))

orion.REVISION.read()
print('major_revision = '+hex(orion.REVISION.major_rev))
print('minor_revision = '+hex(orion.REVISION.minor_rev))

orion.PHASE_CODE_TX0.read()
print('phase_code_tx0 = '+hex(orion.PHASE_CODE_TX0.phase_code_tx0))

orion.PHASE_CODE_TX0.phase_code_tx0 = 0x5a
orion.PHASE_CODE_TX0.write()
orion.PHASE_CODE_TX0.read()
print('phase_code_tx0 = '+hex(orion.PHASE_CODE_TX0.phase_code_tx0))

spi.close()
 