# NeuralNetworkTextSimplification
Instructions for training a neural network. It is the building block in regards to developing text simplification for Estonian. The majority of this work is provided by a previous research seen at https://github.com/senisioi/NeuralTextSimplification

## Preprocessing data and training a model
1) Gather your data and tokenize it if not already tokenized.
2) Make data into two batches for training and testing. For testing separate the data for source and target. Separate the remaining data into training and validation, in total you should have 6 files: train source, train target, validation source and validation target and the two files for testing.
3) Pull the repository from a Linux subsystem or an Unix based operating system and navigate to OpenNMT directory.
4) Make sure that you have Torch installed and run the preprocess.lua script with the following command:<br>
```th preprocess.lua -train_src /PATH -train_tgt /PATH -valid_src /PATH -valid_tgt /PATH -save_data /SAVE_DIRECTORY```<br>
Use paths of your own desire.
6) After this, a .t7 file appears in the save directory. This is the trained model that will be used for evaluating.
For more information about OpenNMT, visit https://opennmt.net/OpenNMT-py/quickstart.html <br>
You can also download a pretrained model for seeing only the results.

## Testing the model
1) Navigate to the src/scripts/ folder
2) Edit the translate.sh file and add the corresponding missing information, like paths for testing etc.
3) Wait for the process to finish. This doesn't take long.
4) After the evaluation, the results appears in the results_NTS folder.

## Results
1) Simply open the text file in the results_NTS folder to see the results.
