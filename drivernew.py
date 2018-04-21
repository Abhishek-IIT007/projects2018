import logging
import os
import numpy as np

file = "glove.6B.50d.txt"
import numpy as np
def loadGloveModel(gloveFile):
    print ("Loading Glove Model")
    
     
    with open(gloveFile, encoding="utf8" ) as f:
       content = f.readlines()
    model = {}
    for line in content:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print ("Done.",len(model)," words loaded!")
    return model
     
     
model= loadGloveModel(file)   
 
# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):
    # Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
    # Note the writing to file has to be handled by you.
    clus=open("output/"+ name_of_file,'w')
    flag = []
    for i in range(len(list_of_terms)):
        not_found=[]
        
        if list_of_terms[i] in flag:
            #print("duplicate")
            continue
        
        clus.write(list_of_terms[i])
        flag.append(list_of_terms[i])
        for j in range (i+1,len(list_of_terms)):
            try:
                u=model[list_of_terms[i]]
                v=model[list_of_terms[j]]
                distance = 0.0 
                dot = np.dot(u, v)
                norm_u = np.sqrt(np.sum(u * u))
                norm_v = np.sqrt(np.sum(v * v))
                cosine_similarity = dot / (norm_u * norm_v)
                if (cosine_similarity >0.7):
                    clus.write(' ')
                    flag.append(list_of_terms[j])
                    clus.write(list_of_terms[j])
            except:
                    
                 not_found.append(list_of_terms[i])
                 not_found.append(list_of_terms[j])
                 not_fset=set(not_found)
                 
        clus.write('\n')
        

# Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath, each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()
   
        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)
    print("DONE")

        # End of code
