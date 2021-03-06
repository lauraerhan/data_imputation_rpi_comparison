# data_imputation_rpi_comparison
 Evaluation of two machine learning techniques (kNN and missForest) against two statistical techniques (mean and MICE) for the task of embedded data 
 imputation (on a RPI 4B).
 
 
 This repository includes the code and datasets behind the work presented in the following journal paper: 
 L. Erhan, M. Di Mauro, A. Anjum, O. Bagdasar, W. Song, and A. Liotta. “Embedded Data Imputation for Environmental Intelligent Sensing: A Case Study”. In:
Sensors 21.23 (2021), p. 7774. DOI: 10.3390/s21237774

Included so far:

- python script to generate the contaminated dataset, starting from the original dataset.
- python script for the experiments - the bare bone implementation which was ran on the RPI 4B for profiling and time analysis.
- original dataset used - taken from here: http://iot.ee.surrey.ac.uk:8080/datasets/pollution/ (City Pulse Smart City Dataset - pollution measurement); we used data corresponding to one of the sensors.
