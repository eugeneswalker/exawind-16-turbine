# Copyright (c) 2022, National Technology & Engineering Solutions of Sandia,
# LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S.
# Government retains certain rights in this software.
#
# This software is released under the BSD 3-clause license. See LICENSE file
# for more details.

from spack import *
from spack.pkg.exawind.amr_wind import AmrWind as bAmrWind
import spack.config
import os
from shutil import copyfile
import inspect
import re
from spack.util.executable import ProcessError

def variant_peeler(var_str):
    """strip out everything but + variants and build types"""
    output = ""
    # extract all the + variants
    for match in re.finditer(r"(?<=\+)([a-z0-9]*)", var_str):
        output+="+{v}".format(v=var_str[match.start(): match.end()])
    # extract build type
    for match in re.finditer("r(?<=build_type=)(a-zA-Z)", var_str):
        output = var_str[match.start():match.end()] + " " + output
    return output

class AmrWindNightly(bAmrWind):
    """Extension of amr-wind for nightly build and test"""

    variant("host_name", default="default")
    variant("extra_name", default="default")
    variant("latest_amrex", default=False)
