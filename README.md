# A Picture is Worth a Thousand Steps: Using Image Processing Techniques to Predict Freezing of Gait (FoG) in Parkinson’s Disease Patients​

Parkinson’s Disease (PD) is a neurodegenerative disease that affects the substantia nigra,
a region in the brain. It causes many hindrances to activities of daily living (ADL). A debilitating
symptom of PD is Freezing of Gait (FoG), where patients are unable to move forward despite
intention of walking. The forward momentum of the torso can often lead to patients falling, causing
serious medical consequences. Prior work has explored the use of gait tests, medical questionnaires
and inertial measurement units to predict FoG. In this research, work has been done to perform a
comprehensive review of various input formats, signal processing algorithms and machine learning
algorithms to predict such FoG events. A novel method for image representation via autoscaling
and RGB pixelation has been introduced, in addition to raw signal data and the Moore-Bachlin
algorithm for Freeze Indices. We find that a 2-dimensional convolutional neural network (CNN)
performs the best on scaled images, attaining state-of-the-art accuracy of 99.50% and sensitivity
of 99.65%. We integrate this model into an Android application which can be used by patients and
doctors to predict and track freeze events over a period of time. This can help doctors diagnose
patients and gauge the severity of the disease, so as to prescribe medication.

<p align="center">
<img width="623" height="401" alt="image" src="https://github.com/user-attachments/assets/148d1fa8-d74d-4661-b056-8526530e3888" />
</p>

## General Results

In this work, experimented with three major feature vectors:
- raw signal data input of shape `(768,)`
- extraction of the Moore-Bachlin Freeze Indices of shape `(3,)`
- image representation of shape `(16, 16, 3)` (see above)

### Raw Signal Data Input

We observe that the SVM architecture performs the best, at an accuracy of 91.21%, but it has a poor recall rate as compared to the 1D-CNN. We also tried to run the data through Google Cloud's AutoML pipeline as well, and observed a model with a higher accuracy, as seen below.

| Model Used | Accuracy (%) | Recall (%) | Precision (%) |
|------------|--------------|------------|---------------|
| Google Cloud AutoML Model | **93.70** | 49.89 | 80.79 |
| Support Vector Machine (SVM) | **91.21** | 29.29 | 82.14 |
| 1D Convolution Neural Network (CNN) | 90.88 | **78.03** | 52.97 |
| Neural Network with 3 Hidden Layers | 90.36 | 38.67 | 52.39 |
| Random Forest (RF) | 90.06 | 14.56 | **89.42** |
| Big Single-Hidden-Layer Perceptron | 90.03 | 61.59 | 50.09 |
| Neural Network with 4 Hidden Layers | 90.00 | 0.01 | 20.00 |
| Small Single-Hidden-Layer Perceptron | 89.91 | 50.47 | 49.54 |
| k-Nearest Neighbours (kNN) | 88.67 | 8.51 | 51.99 |
| Logistic Regression | 87.98 | 0.04 | 0.79 |
| Neural Network with 2 Hidden Layers | 84.20 | 75.34 | 36.08 |

## Moore-Bachlin Freeze Indices

<p align="center">
<img width="520" height="210" alt="image" src="https://github.com/user-attachments/assets/14a2931d-5abc-4c7b-b1eb-f99085450ab1" />
</p>

In prior literature, a parameter known as the Freeze Index (FI) has been established to minimize
the feature set of a dataset while maintaining a large part of the temporal features. This algorithm
has been further elaborated on via the Moore-Bachlin Algorithm, which computes a corresponding Energy 
Index (EI), which can be used to isolate low-power conditions (e.g. walking). The FI and EI can be
isolated via the following algorithm:

$$F(a, b) = \int_a^b \left|A(f)\right|^2 df = \sum_{n=\left\lceil \frac{N}{f_{sr}}\times a \right\rceil}^{\left\lfloor \frac{N}{f_{sr}}\times b \right\rfloor} \left| A[n] \right|^2$$
$$FI = \frac{F(3,8)}{F(0.5,3)}, \quad EI = F(0.5, 8)$$

Here, the function $A(f)$ represents the Fourier Transform of the signal, while $A[n]$ represents the corresponding Discrete Fast Fourier Transform (DFFT) computed over N frequencies and $f_{sr}$ is the sampling rate frequency. Prior work has utilized this algorithm by establishing a threshold of 1.5 for the freeze index, i.e. if $FI > 1.5$, it is classified as a freeze event.

| Model Used | Accuracy (%) | Recall (%) | Precision (%) |
|------------|--------------|------------|---------------|
| **kNN** | **90.28** | **52.61** | **77.79** |
| Random Forest | 88.43 | 38.65 | 74.98 |
| Neural Network (Swish, Adam, $\alpha = 0.02$) | 86.17 | 25.12 | 63.96 |
| SVM (Gaussian Kernel) | 86.08 | 18.46 | 70.20 |
| LogReg | 84.77 | 9.12 | 59.80 |
| SVM (Linear Kernel) | 84.45 | 0.44 | 64.63 |

## Image Representation

We design a deep convolutional neural network (CNN) to be trained over the generated images (see the figure above for more details regarding the architecture). This CNN performed well, achieving a 99.50% accuracy and hence, state-of-the-art. This model achieves a recall rate of 99.65% and a precision of 95.63% over 20 epochs.


# References
- _Aich S, Pradhan PM, Park J, Sethi N, Vathsa VSS, Kim HC (2018) A validation study of freezing of gait (fog) detection and machine-learning-based fog prediction using estimated gait characteristics with a wearable accelerometer. Sensors 18(10), DOI 10.3390/s18103287, URL https://www.mdpi.com/1424-8220/18/10/3287_
- _Moore ST, MacDougall HG, Ondo WG (2008) Ambulatory monitoring of freezing of gait in parkinson’s disease. Journal of Neuroscience Methods 167(2):340–348, DOI 10.1016/j.jneumeth.2007.08.023, URL https://www.sciencedirect.com/science/article/pii/S0165027007004281_
- _Bachlin M, Plotnik M, Roggen D, Maidan I, Hausdorff JM, Giladi N, Troster G (2010) Wearable assistant for parkinson’s disease patients with the freezing of gait symptom. IEEE Transactions on Information Technology in Biomedicine 14(2):436–446, DOI 10.1109/TITB.2009.2036165_
