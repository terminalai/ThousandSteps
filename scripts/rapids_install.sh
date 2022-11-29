conda create --name gaitml python=3.8
conda activate gaitml
conda create -n rapids-22.10 -c rapidsai -c conda-forge -c nvidia  \
    rapids=22.10 python=3.8 cudatoolkit=11.5