# Copyright (c) 2022, National Technology & Engineering Solutions of Sandia,
# LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S.
# Government retains certain rights in this software.
#
# This software is released under the BSD 3-clause license. See LICENSE file
# for more details.

from spack import *
from spack.pkg.exawind.nalu_wind import NaluWind as bNaluWind
from spack.pkg.exawind.nalu_wind import trilinos_version_filter
import spack.config
import os
from shutil import copyfile
import inspect
import re
from spack.util.executable import ProcessError


class NaluWindNightly(bNaluWind, CudaPackage):
    """Extension of Nalu-Wind for nightly build and test"""
    maintainers = ["psakievich"]

    version("master", branch="master", submodules=True)

    variant("host_name", default="default")
    variant("extra_name", default="default")

    variant("snl", default=False, description="Reports to SNL dashboard")

    phases = ["test"]

    def dashboard_build_name(self):
        variants = "-" + self.dashboard_variants() if "+snl" in self.spec else ""
        return "-{}{}^{}".format(self.dashboard_compilers(), variants, self.dashboard_trilinos())

    def dashboard_compilers(self):
        compiler = self.spec.format("{compiler}")
        cuda = "-" + self.name_and_version("cuda") if "cuda" in self.spec else ""
        return compiler + cuda

    def dashboard_trilinos(self):
        vstring = trilinos_version_filter(self.spec["trilinos"].version)
        trilinos = "trilinos@{v}".format(v=vstring)
        uvm = self.spec["trilinos"].format("{variants.uvm}") if "cuda" in self.spec else ""
        return trilinos + uvm

    def name_and_version(self, package):
        return self.spec[package].format("{name}{@version}")

    def dashboard_variants(self):
        whitelist = ["fftw", "hypre", "tioga", "openfast"]
        printable = [v for v in self.spec.variants if v in whitelist]
        enabled = [v for v in printable if self.spec.variants[v].value]

        build_type = self.spec.format("{variants.build_type}").split("=")[1]
        formatted = "".join([self.spec.format("{variants." + variant + "}") for variant in enabled])
        return build_type + formatted
