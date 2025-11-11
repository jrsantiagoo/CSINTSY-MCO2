# Creates features for a given word
# Returns an array of numbers corresponding to each feature
def label_to_int(label):
    if label == 'FIL':
        return 0
    if label == 'ENG':
        return 1
    return 2    #OTH

def int_to_label(label_int):
    if label_int == 0:
        return 'FIL'
    if label_int == 1:
        return 'ENG'
    return 'OTH'

