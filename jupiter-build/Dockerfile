FROM ecpe4s/ubuntu20.04-runner-x86_64-gcc11:2023-04-10

RUN rm -f /usr/include/asm \
 && rm -f /usr/include/bits \
 && rm -f /usr/include/gnu \
 && rm -f /usr/include/sys \
 && wget https://repo.radeon.com/amdgpu-install/5.4/ubuntu/focal/amdgpu-install_5.4.50400-1_all.deb \
 && apt install -y ./amdgpu-install_5.4.50400-1_all.deb \
 && rm -f ./amdgpu-install_5.4.50400-1_all.deb \
 && echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/amdgpu/5.4/ubuntu focal main' | tee /etc/apt/sources.list.d/rocm.list \
 && echo 'deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/rocm-keyring.gpg] https://repo.radeon.com/rocm/apt/5.4 focal main' | tee /etc/apt/sources.list.d/rocm.list \
 && apt update -y \
 && amdgpu-install -y --usecase=rocm,hip,hiplibsdk,mllib,mlsdk --rocmrelease=5.4.0 --no-dkms \
 && apt clean -y \
 && echo /opt/rocm/lib > /etc/ld.so.conf.d/rocm.conf \
 && ldconfig -v

RUN echo export PATH=/opt/rocm/bin:'${PATH}' >> /etc/bash.bashrc

ENV PATH=/opt/rocm/bin:$PATH
