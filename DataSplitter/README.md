## What is this?
This command-line script splits a data set into trainig, development, and test sets.
It accepts 4 file paths as mandatory arguments: `source file`, `training file`, `development file`, and `test file`.  The cript should be exectuable. Make sure that the script and helper methods are in the same directory.


## Why do we need it?
Machine learning specialists almost always evaluate systems on a held-out "test
set" which is disjoint from the data used to train the system. Commonly, they
also reserve a portion of the data for tuning *hyperparameters*, parameters of
the model which cannot be directly learned from the data. For this they often
use a "validation" or "development" set which is also disjoint from the
training and test sets. 
