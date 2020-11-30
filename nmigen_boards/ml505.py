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
    default_clk = "clk50"
    resources   = [
        Resource("clk100", 0, Pins("AH15", dir="i"),
            Clock(100e6), Attrs(IOSTANDARD="LVTTL33")
        ),

        *LEDResources(
            pins="H18 L18 G15 AD26 G16 AD25 AD24 AE24",
            attrs=Attrs(IOSTANDARD="LVTTL33")
        )
    ]
    connectors  = [
       
    ]

    # This board doesn't have an integrated programmer.
