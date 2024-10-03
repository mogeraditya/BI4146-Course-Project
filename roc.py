import numpy as np
import matplotlib.pyplot as plt
def given_threshold_get_tpr_fpr(neg_likelihoods, pos_likelihood, threshold, testing_ids):
    prediction_array= ["a" for i in neg_likelihoods]
    for prediction_index in range(len(prediction_array)):
        if pos_likelihood[prediction_index]<threshold and neg_likelihoods[prediction_index]<threshold:
            prediction_array[prediction_index]= "NULL"
        if pos_likelihood[prediction_index]== neg_likelihoods[prediction_index]:
            prediction_array[prediction_index]= "NULL"
        if pos_likelihood[prediction_index]> neg_likelihoods[prediction_index]:
            prediction_array[prediction_index]= "pos"
        if pos_likelihood[prediction_index]< neg_likelihoods[prediction_index]:
            prediction_array[prediction_index]= "neg"   
            
    # positive_counts= prediction_array.count("pos")
    # negative_counts= prediction_array.count("neg")
    print(prediction_array)
    null_counts= prediction_array.count("NULL")
    total_pred_counts= len(neg_likelihoods)- null_counts
    tp=0; fp=0 
    for id in range(len(testing_ids)):
        if testing_ids[id] == prediction_array[id]:
            tp+=1
        if testing_ids[id] != prediction_array[id] and prediction_array[id]!= "NULL":
            fp+=1
    tpr= tp/total_pred_counts; fpr= fp/total_pred_counts 
    return tpr, fpr    
    
def plot_roc_curve(neg_likelihoods, pos_likelihood, resolution, testing_ids):
    range_of_thresholds= np.arange(0,1+resolution, resolution)
    store_tpr_fpr= []
    for threshold in range_of_thresholds:
        tpr, fpr = given_threshold_get_tpr_fpr(neg_likelihoods, pos_likelihood, threshold, testing_ids)
        store_tpr_fpr.append([tpr,fpr])
    store_tpr_fpr= np.array(store_tpr_fpr)
    print(store_tpr_fpr)
    plt.scatter(store_tpr_fpr[:,0], store_tpr_fpr[:,1])
    plt.show()
    
neg_likelihoods= [0.95, 0.65, 0.3, 0.4, 0.7, 0.8]
pos_likelihood= [0.15, 0.50, 0.3, 0.3, 0.16, 0.95]
testing_ids= ["neg", "neg", "pos", "pos", "pos", "neg"]
plot_roc_curve(neg_likelihoods, pos_likelihood, 0.1, testing_ids)