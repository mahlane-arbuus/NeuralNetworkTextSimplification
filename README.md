# NeuralNetworkTextSimplification
Instructions for training a neural network. It is the building block in regards to developing text simplification for Estonian. The majority of this work is provided by a previous research seen at https://github.com/senisioi/NeuralTextSimplification

## Preprocessing data
1) Gather your data and tokenize it if not already tokenized.
2) Separate the data into training and validation, in total you should have 4 files: train source, train target, validation source and validation target.
3) Pull the repository from a Linux subsystem or an Unix based operating system and navigate to OpenNMT directory.
4) Make sure that you have Torch installed and run the preprocess.lua script with the following command: 
```th preprocess.lua -train_src /PATH -train_tgt /PATH -valid_src /PATH -valid_tgt /PATH -save_data /SAVE_DIRECTORY```
Use paths of your own desire.
5) After this, a .t7 file appears in the save directory. This is the model that will be used for training.
For more information about OpenNMT, visit https://opennmt.net/OpenNMT-py/quickstart.html

## Training model
1) Navigate to the src/scripts/ folder
