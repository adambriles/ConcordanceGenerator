# Concordance Generator
Concordance Generator is a Python Script to generate a concordance for user provided text files, written in English. The generated concordance
can either be written to a file or to stdout. 

## Requirements
- Python v.3.8+ installed
- Pip v.20.0.2+ installed
- The spaCy natural nanguage processing Python library v.3.3.1+
  - The English Pipeline for spaCy

#### Setting up spaCy
1. On the command line execute: pip3 install spacy
2. On the command line execute: python3 -m spacy download en_core_web_sm 

## Running the concordance generator
From the top level directory of this repository: 
  1. Getting help: 
     - ./generate_concordance/generateConcordance.py --help
  2. Writing the generated concordance to a specified text file 
     - ./generate_concordance/generateConcordance.py --inputFile <your input file> --outputFile <your output file>
  3. Writing the generated concordance to a specified text file 
     - ./generate_concordance/generateConcordance.py --inputFile <your input file> --stdout 
     
  Note: Demo files have been provided under the /test_files directory
     
## Running the Unit Tests
From the top level directory of this repository: 
  1. python3 -m unittest discover test  
  
## Libraries Used: 
1. spaCy:
   - Used its natural language processing cababilities to track what words appeared in what sentences


## Directory Structure and Important Files: 
  /generate_concordance - Where all files required to run the Concordance Generator are stored
  
  /generate_concordance/generateConcordance.py - Contains main()
  
  /generate_concordance/__init__.py - Ensures /concordance_generator is treated as if it contains a package
  
  /generate_concordance/concordance_empty.py - Contains Exception raised by the ConcordanceGenerator class 
  
  /generate_concordance/concordance_generator.py - Containers the ConcordanceGenerator class
  
  /generate_concordance/ConcordanceUtils.py - Static functions used across the code 
  
  /generate_concordance/word_info.py - Class used to store metrics needed to generate a concordance for each word
  
  /test - Where all Unit Test files are stored
  
  /test_files - Test files used in Unit Tests and for a user's convenience
