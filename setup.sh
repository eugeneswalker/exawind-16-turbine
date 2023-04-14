#!/bin/bash
git clone https://github.com/spack/spack
(cd spack && git checkout b8d15e816bf7388774e65ca59daf3831b4fa4180)
git clone https://github.com/psakievich/spack-manager.git
cp -r repos/exawind spack/var/spack/repos/.
spack config --scope site add repos:['$spack'/var/spack/repos/exawind]
# edit hipcc to add `-std=c++17 --gcc-toolchain=GCC11.2.0-PREFIX`
# vim $(which hipcc)
# -- 
# line 46:   @ARGVPLUS = (@ARGV, "--gcc-toolchain=/bootstrap/runner/install/linux-ubuntu20.04-x86_64/gcc-9.4.0/gcc-11.2.0-ixjtravimpbimwx4a5c7bdmbg6yap5tv", "-std=c++17");
# line 47:   system($^X, $HIPCC_PERL, @ARGVPLUS);
# --
#

# spack -e . env depfile -o Makefile
