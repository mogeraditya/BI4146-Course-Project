import numpy as np
def given_threshold_get_tpr_fpr(neg_likelihoods, pos_likelihood, resolution, threshold, testing_ids):
    prediction_array= np.zeros(shape= len(neg_likelihoods))
    for prediction_index in range(len(prediction_array)):
        if pos_likelihood[prediction_index]<threshold and neg_likelihoods[prediction_index]<threshold:
            prediction_array[prediction_index]= "NULL"
        if pos_likelihood[prediction_index]> neg_likelihoods[prediction_index]:
            prediction_array[prediction_index]= "pos"
        if pos_likelihood[prediction_index]< neg_likelihoods[prediction_index]:
            prediction_array[prediction_index]= "neg"
            
            
    positive_counts= prediction_array.count("pos")
    negative_counts= prediction_array.count("neg")
    null_counts= prediction_array.count("NULL")
    
    
def plot_roc_curve(neg_likelihoods, pos_likelihood, resolution, testing_ids):
    range_of_thresholds= np.arange(0,1+resolution, resolution)
    for threshold in range_of_thresholds:
        
    