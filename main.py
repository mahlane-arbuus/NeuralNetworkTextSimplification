from subprocess import call

algorithms = ["neural", "gector"]

s = input("Enter the name of the algorithm you wish to work with. Options are (" + "/".join(algorithms) + "): ")

while True:
    if s == "exit":
        break
    elif s == "neural":
        o = input("Do you wish to train the model? (y/n)")
        if o == "y":
            train_src = input("Enter the path to the training source file: ")
            train_tgt = input("Enter the path to the training target file: ")
            valid_src = input("Enter the path to the validation source file: ")
            valid_tgt = input("Enter the path to the validation target file: ")
            call("th preprocess.lua -train_src " + train_src + " -train_tgt " + train_tgt + " -valid_src " + val_src + " -valid_tgt " + val_tgt + " -save_data " + "NeuralTextSimplification\models", shell=True)
        o = input("Do you wish to test the model? (y/n): ")
        if o == "y":
            if os.path.exists("NeuralTextSimplification\src\scripts\translate.sh"):
                os.remove("NeuralTextSimplification\src\scripts\translate.sh")
                
            model = input("Enter model path: ")
            gpus = input("Enter gpus, if you don't use then enter 0: ")
            source = input("Enter path of testing source: ")
            target = input("Enter path of testing target: ")
            
            file = open("NeuralTextSimplification\src\scripts\translate.sh", "w")
            file.write('''#!/bin/bash\n
            source ./base_conf.sh\n

            RES_DIR=`readlink -f ../../results_${CUR_EXP}`\n
            mkdir -p $RES_DIR\n
            # Rename YOUR_MODEL with the appropriate path of your model created with OpenNMT\n
            MODEL_PATH=`readlink -f ''' + model + '''`\n
            MODEL=${MODEL_PATH##*/}\n

            BEAM_SIZE=5\n
            GPUS=''' + gpus + '''\n
            OUTPUT=${RES_DIR}/result_${MODEL}_${BEAM_SIZE}\n
            LOG_OUT=${RES_DIR}/result_${MODEL}_${BEAM_SIZE}.log\n

            # add your path to source, in this case your regular sentences, this time there is no need for validation\n
            SRC=''' + source + '''\n
            # add your path to target, in this case your simplified sentences, this time there is no need for validation\n
            TGT=''' + target + '''\n
            cd $OPENNMT_PATH\n
            # sometimes this command fails, in this case instead of 'th' add the full path in the torch install folder,\n
            # for example /home/user/torch/install/bin/th\n
            th translate.lua -replace_unk -beam_size ${BEAM_SIZE} -gpuid ${GPUS} -n_best 4 -model ${MODEL_PATH} -src ${SRC} -tgt ${TGT} -output ${OUTPUT} -log_file ${LOG_OUT}\n
            cd $CWD\n
            echo "Check results in "${OUTPUT}"''')
            file.close()
            call("sudo bash NeuralTextSimplification\src\scripts\translate.sh", shell=True)
        s = input("Enter next command: ")
    elif s == "gector":
        o = input("Do you wish to install the requirements? (y/n): ")
        if o == "y":
            call("pip install -r " + "gector-master\requirements.txt")
        o = input("Do you wish to train a model? (y/n): ")
        if o == "y":
            o = input("Do you wish to preprocess the data? (y/n): ")
            if o == "y":
                source = input("Enter path of the source file: ")
                target = input("Enter path of the target file: ")
                output = input("Path of output file: ")
                call("python3 utils/preprocess_data.py -s " + source + " -t " + target + " -o " + output, shell=True)
            train = input("Enter training data path: ")
            val = input("Enter validation data path: ")
            call("python train.py --train_set " + train + " --dev_set " + val + " \--model_dir gector-master\data", shell=True)
            print("Model saved in data folder.")
        o = input("Do you wish to test a model? (y/n): ")
        if o == "y":
            model = input("Enter model path: ")
            vocab = input("Enter vocabulary file path: ")
            source = input("Enter test source file path: ")
            tgt = input("Enter test target file path: ")
            call("python predict.py --model_path " + model + " --vocab_path " + vocab + " --input_file " + source + " --output_file " + tgt, shell=True)
        s = input("Enter next command: ")
    else:
        print("Command not recognized, try again.")
        s = input()
