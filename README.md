# Restoring_the_Sister
This is the repository for my 2021 paper "Restoring The Sister: Reconstructing a Lexicon from Sister Languages using Neural Machine Translation". The actual paper can be found [here](https://www.aclweb.org/anthology/2021.americasnlp-1.13/).

# Instructions
The repository contains the initial data file and all data-processing scripts needed to replicate the experiment. If you are just interested in the data file, please refer to "romance-ortography.txt".

This experiment requires python 3 and the following python dependencies: 
- opennmt-py 2.0.1 (other versions should work, but no guarantees can be made)
- jellyfish 0.8.2 (other versions should work)

If you do not have these packages installed, call "pip install --user opennmt-py==2.0.1" followed by "pip install --user jellyfish==0.8.2".


If you wish to replicate the experiment, clone the repository and run the following scripts *in this order* (please note, these scripts were written tailored to this data, so they will not work for your custom data):
- mungenormalizev2.py (seperates the file into multiple files for each language, extracts vocabulary)
- restructure.py (removes all cognate pairs that do not have an equivalent in Italian, which is our target)
- concatenate.py (concatenates the training data in the manner described in the paper)
- reduce.py (artifically reduces a set of training data for comparison)

After running these scripts, you can call "python execute_all.py --dir here". This will train models for *all* .yaml files in the directory (warning: this may take up to 12 hours or more). If you want to train individual models, simply call "onmt_train --config *config-file*".

The trained models will save in the folder /models/. In order to evaluate a model, you need to call "onmt_translate -model *model directory and name* -src *test file for that model* -output *where you want to save the output*". All data, including the test-files is stored in /data/. If you are unsure what the right test-file is for a model, then enter its .yaml file. The test-file will have the same name as the validation *target* file, except the  "\_val" will be changed to "\_test". 

In order to evaluate a model, you can use the "evaluation_command.py" script. It takes two arguments, your translated file (--src) and the target test file (--tgt). Your target file will always be "data/italian_test_res.txt". This script will save a text file which will be named after your translated file + "edit_eval.txt". It will contain edit distances of 0-5 in absolute numbers, the custom score (see paper), and the edit distances in percentages.
