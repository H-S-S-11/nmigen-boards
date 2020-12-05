import os
import subprocess

from nmigen.build import *
from nmigen.vendor.xilinx_spartan_3_6 import *
from .resources import *


__all__ = ["ML505Platform"]


class ML505Platform(XilinxVirtex5Platform):
    device      = "xc5vlx50T"
    package     = "ffg1136"
    speed       = "1"
    default_clk = "clk100"
    default_rst = "cpu_rst"
    resources   = [
        Resource("clk100", 0, Pins("AH15", dir="i"),
            Clock(100e6), Attrs(IOSTANDARD="LVCMOS33")
        ),
        Resource("audio_bit_clk", 0, Pins("AF18", dir="i"),
            Clock(12288e3), Attrs(IOSTANDARD="LVCMOS33")),
        Resource("cpu_rst", 0, PinsN("E9", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),

        *LEDResources(
            pins="H18 L18 G15",
            attrs=Attrs(IOSTANDARD="LVCMOS25")
        ),
        #pins=["H18 L18 G15", "AD26", "G16", "AD25 AD24 AE24"],
        #attrs=["LVCMOS25", "LVCMOS18", "LVCMOS25", "LVCMOS18"]
        
        *SwitchResources(
            pins = "U25  AG27 AF25 AF26 AE27 AE26 AC25 AC24",
            attrs=Attrs(IOSTANDARD="LVCMOS18"),
        ),

        Resource("audio_codec", 0,  #AD1981 chip using AC97 codec, primary mode with 24.576MHz crystal
            Subsignal("sdata_in", Pins("AE18", dir="i")),
            Subsignal("sdata_out", Pins("AG16", dir="o")),
            Subsignal("audio_sync", Pins("AF19", dir ="o")),
            Subsignal("flash_audio_reset_b", PinsN("AG17", dir="o")), #this reset pin is shared with the config flash chips, beware if those are added as resources
            Attrs(IOSTANDARD="LVCMOS33")
        ),
        
    ]
    connectors  = [
        #J6: 2.54mm header on right of board, even pins only (odd pins are GND)
        #VccIO (bank 11/13) set with J20: 1-3, 2-4 for 3V3 or 3-5, 4-6 for 2V5
        Connector("gpio", 0,
            "- H33  - F34  - H34  - G33  - G32  - H32  - J32  - J34 "
            "- L33  - M32  - P34  - N34  - AA34 - AD32 - Y34  - Y32 "
            "- W32  - AH34 - AE32 - AG32 - AH32 - AK34 - AK33 - AJ32"
            "- AK32 - AL34 - AL33 - AM33 - AJ34 - AM32 - AN34 - AN33"
        )       
    ]

    # This board doesn't have an integrated programmer, just a JTAG header

if __name__ == "__main__":
    from .test.blinky import *
    ML505Platform().build(Blinky(), do_build=False, do_program=False).execute_local(run_script=False)