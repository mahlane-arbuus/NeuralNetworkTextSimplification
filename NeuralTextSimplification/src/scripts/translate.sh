#!/bin/bash
source ./base_conf.sh

RES_DIR=`readlink -f ../../results_${CUR_EXP}`
mkdir -p $RES_DIR
# Rename YOUR_MODEL with the appropriate path of your model created with OpenNMT
MODEL_PATH=`readlink -f ../../models/YOUR_MODEL.t7`
MODEL=${MODEL_PATH##*/}

BEAM_SIZE=5
#GPUS=1,2 in case you want to use a GPU, otherwise leave as 0
GPUS=0
OUTPUT=${RES_DIR}/result_${MODEL}_${BEAM_SIZE}
LOG_OUT=${RES_DIR}/result_${MODEL}_${BEAM_SIZE}.log

# add your path to source, in this case your regular sentences, this time there is no need for validation
SRC=/PATH_TO_SOURCE
# add your path to target, in this case your simplified sentences, this time there is no need for validation
TGT=/PATH_TO_TARGET
cd $OPENNMT_PATH
# sometimes this command fails, in this case instead of 'th' add the full path in the torch install folder,
# for example /home/user/torch/install/bin/th
th translate.lua -replace_unk -beam_size ${BEAM_SIZE} -gpuid ${GPUS} -n_best 4 -model ${MODEL_PATH} -src ${SRC} -tgt ${TGT} -output ${OUTPUT} -log_file ${LOG_OUT}
cd $CWD
echo "Check results in "${OUTPUT}
