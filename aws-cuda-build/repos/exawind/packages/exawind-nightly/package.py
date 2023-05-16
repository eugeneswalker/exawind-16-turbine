# Copyright (c) 2022, National Technology & Engineering Solutions of Sandia,
# LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S.
# Government retains certain rights in this software.
#
# This software is released under the BSD 3-clause license. See LICENSE file
# for more details.

from spack import *
from spack.pkg.exawind.exawind import Exawind as bExawind
import spack.config
import os
from shutil import copyfile
import inspect
import re
from spack.util.executable import ProcessError

class ExawindNightly(bExawind):
    """Extension of exawind for nightly build and test"""

    variant("host_name", default="default")

    phases = ["install"]
