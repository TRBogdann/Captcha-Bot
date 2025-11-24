
#TODO - Make an actual reader
 
def loadVocabulary(filepath):
    with open(filepath,'r') as f:
        vocab =  f.read()
        return list(vocab)