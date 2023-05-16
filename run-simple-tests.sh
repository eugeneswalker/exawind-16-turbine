#!/bin/bash -e

spack load $(spack find --format /{hash} nalu-wind | head -1)

if [[ ! -d nalu-wind ]] ; then
  git clone https://github.com/exawind/nalu-wind
  (cd nalu-wind && git submodule update --init --recursive --jobs 0)
fi

cd nalu-wind/reg_tests/test_files

declare -A tests=( [edgeHybridFluids]=8 [ablNeutralEdgeSegregated]=8 [ablNeutralNGPHypre]=2 [ablNeutralNGPTrilinos]=2 [ablNeutralNGPHypreSegregated]=2)

for k in "${!tests[@]}"; do
  v=${tests[$k]}
  cd $k
  mpirun -np $v naluX -i $k.yaml >$k.log 2>&1
  if [[ $? -ne 0 ]] ; then
    echo "RUN FAILED: $k (see $k.log)"
  else
    python ../../check_norms.py --abs-tol 1e-8 $k{,.norm.gold}
  fi
  cd ..
done
