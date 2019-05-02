#!/usr/bin/env bash
conda create -y --prefix env -c conda-forge \
  anaconda \
  ConfigArgParse \
  grpcio \
  grpcio-tools \
  ipywidgets \
  opencv \
  pillow \
  pyarrow \
  pyspark=2.4.1 \
  python=3.6 \
  tensorflow
