#!/bin/bash

BUILD_DATE=$(printf '%(%Y-%m-%d)T' -1)
BUILD_TAG=${BUILD_TAG:-${BUILD_DATE}}

REGISTRY=${REGISTRY:-esw123}
OUTPUT_IMAGE="${REGISTRY}/exawind-rocm:${BUILD_TAG}"

docker build -t "${OUTPUT_IMAGE}" .