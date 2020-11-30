import os
import subprocess

from nmigen.build import *
from nmigen.vendor.xilinx_spartan_3_6 import *
from nmigen_boards.resources import *


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
        Resource("cpu_rst", 0, PinsN("E9", dir="i"), Attrs(IOSTANDARD="LVCMOS33")),

        *LEDResources(
            pins="H18 L18 G15",
            attrs=Attrs(IOSTANDARD="LVCMOS25")
        ),

        *SwitchResources(
            pins = "U25  AG27 AF25 AF26 AE27 AE26 AC25 AC24",
            attrs=Attrs(IOSTANDARD="LVCMOS18"),
        ),
    ]
    connectors  = [
       
    ]

    # This board doesn't have an integrated programmer.

if __name__ == "__main__":
    from nmigen_boards.test.blinky import *
    ML505Platform().build(Blinky(), do_build=False, do_program=False).execute_local(run_script=False)