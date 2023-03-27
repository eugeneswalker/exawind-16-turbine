#!/bin/bash
git clone https://github.com/spack/spack
(cd spack && git checkout b8d15e816bf7388774e65ca59daf3831b4fa4180)
git clone https://github.com/psakievich/spack-manager.git
cp -r repos/exawind spack/var/spack/repos/.
