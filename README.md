![sani_tracker_rgbd](https://github.com/user-attachments/assets/caddaf96-3da6-499f-a017-bcc46a4103ca)

<h2>Haar Cascade Trainer</h2>

This software implements training and usage of OpenCV's Haar Cascade Classifier tools in python. It includes a training utility and two applications cases- one which applies the classifier to a stream from a camera, and one that does in-group and out-group testing.

It was developed as part of a project for tracking handlebars and pushbars on doors, and thus searching for multiple target types. To deal with this, the paradigm is to make a distinct classifier for each target type and execute them in parallel. Towards that end, we made utilities which make setting up to train multiple classifiers easily, and implementes unit testing on the multiple parallel classifiers.

<h3>Includes:</h3>
- A utility to make positive and negative training data from sample target images and a stock of background images
- Utilities to prepare the necessary BG and positives vector files for training
- Scripts for executing training from the sample directories
- A pair of example implementations using the generated cascade classifiers- one showing usage on a video stream with a stock classifier for faces, the other doing unit testing on in and out group images with multiple cascades in parallel








