# Basic of CNN for Beginners
A CNN is a class of deep, feed-forward (not recurrent) artificial neural networks that are applied to analyzing visual imagery.

# Things to note before reading
1. Images are just matrices of pixel values.
2. Channel is a conventional term used to refer to a certain component of an image. An image from a standard digital camera will have three channels — red, green, and blue (RGB). While a grayscale image has only one channel. The value of each pixel in the matrix will range from 0 to 255.

# Convolutional Layer
Filter is an **X** detector, which acts like a sliding window and perform element-wise multiplication to search the **X** pattern in the image.  If a certain part in the image looks like **X**, the value of the convolved feature (feature maps/activation map, these terms are used interchangeably) for that part in the next layer will be high.

If to detect more patterns, more types of filters will be needed. Here is the part where the depth of the next layer comes in. Let’s say you use 3 filters, which is **X**, **O** and **I** detector to slide through the images, then the next layer of the network will be **depth=3**.

The filter can also be the filter for detecting color contrast, texture, etc. of the images, depending on the prediction task that you want the CNN to learn

## Examples of filters performing operations on image
![ALT TXT](https://miro.medium.com/max/866/1*4bkq6f6ZU3PkPzEHXfJrLQ.png)


# Hyperparameters that control the behavior of each convolved layer:
## Stride of 1
![ALT TXT](https://miro.medium.com/max/1188/0*xgDU2SubxqbuhOE_.png)
## Stride of 2
![alt txt](https://miro.medium.com/max/1254/0*lLObfXD688RRzQsy.png)

# Example of Padding = 2 on a 32x32x3 image
![alt txt](https://miro.medium.com/max/530/1*x5eQUEasvbOfzgIyf884og.png)
## The formula for convolution. Output and input indicate the size for height or width.
![alt txt](https://miro.medium.com/max/810/1*8Gd2MAokcWLzGV1jQrfZHQ.png)
# Number of filters (depth of the next layer)
6x6x3 image with 4 3x3 filters. After convolving, will get 4x4xn, n depends on the number of filters you use, in other words, it is the number of features detector you use. In this case, n will be 4.

# Size of the Filter
The size of the filter is a usually odd number so that the filter has the central pixel/central vision so to know the position of the filter. As if the size of the filter is even, then you need some asymmetric padding.

The weights/parameters of the convolutional layer are the values of the filters in the convolutional layer. Those are the learnable values within a CNN.

After convolution is performed, an activation function will be applied to introduce non-linearity to the feature maps.
The reason that we apply non-linearity is that convolution is a linear operation — element-wise matrix multiplication and addition, so we account for non-linearity by introducing a non-linear function like ReLU, prevent the model from computing the linear function, which will be a bad model (because the model will not be able to handle complex non-linear problems).

# Pooling Layer
Spatial Pooling (also called subsampling or downsampling) reduces the dimensionality of each feature map and retains the most important information of an image. Spatial Pooling can be of different types: Max, Average, Sum, etc. In practice, Max Pooling has been shown to work better.

Max pooling being the most popular. This basically takes a filter (example: size 2x2) and a stride of the same length(which is 2). It then applies it to the input volume and outputs the maximum number in every sub-region that the filter convolves around. The output size formula for the max-pooling is the same as the convolution one.
The pooling layer doesn’t have any learnable parameters, hence adding more pooling layers in the CNN doesn’t add complexity to the model directly.

1. Makes the input representations (feature dimension) smaller and more manageable.
2. Reduces the number of parameters and computations in the network, therefore, controlling overfitting.
3. Makes the network invariant to small transformations, distortions, and translations in the input image (a small distortion in the input will not change the output of Pooling — since we take the maximum/average value in a local neighborhood).

![alt txt](https://miro.medium.com/max/1204/0*KxpARsMRPiIfVhPb.png)

# Dropout Layer
The idea of dropout is simplistic in nature. This layer **drops out** a random set of activation maps in that layer by setting them to zero during training. Simple as that. It makes sure that the network isn’t getting too “fitted” to the training data and thus helps to alleviate the overfitting problem.

**An important note is that this layer is only used during training, and not during test time.**

# Network in Network Layer (1x1 convolution)
Not in the traditional architecture of CNN but very useful, because it helps in generating more features, and making network deeper in a computationally inexpensive way.

A network-in- network layer refers to a convolutional layer with a 1 x 1 size filter. -1x1 convolutions span a certain depth, so we can think of it as a 1 x 1 x N convolution where N is the number of filters applied in the layer. Effectively, this layer is performing an N-D element-wise multiplication where N is the depth of the input volume into the layer.

If the previous layer has 128 feature maps then “1x1 convolutions” are convolutions across all these feature maps with filters each of size 1x1x128. Say one chooses to have 64 of these 1x1x128 dim filters, then the result will be 64 features maps, each the same size as before. View each output feature map as “per-pixel” projections (dot-product) onto a lower-dimensional space using a single learned filter (weights tied) across all feature maps. Basically, they just crush 128 feature maps (representational responses to 128 learned filters) into 64 feature maps ignoring the spatial dimension.
Remember that larger filters like a 3x3x128 filter would also learn to summarize feature responses across all feature maps so in this way all size filters do the same thing. The only difference is that 1x1 (learned) filters ONLY do this across feature-maps where 3x3 filters also consider local spatial correlations.
So, it is used for two reasons:
1. Dimensionality reduction:
When performing larger size convolutions (spatial 3x3 or 5x5…) over a large number of feature maps, bringing down the dimensions in-depth (# feature maps) reduces computations dramatically. This is done in GoogLeNet Inception modules to get the network in to deeper without overfitting.
2. Since activation functions will be applied again, it is then applying non-linearity to the model, thus making the model more complex and robust to complex problems.

# Classification
Normally, the pipeline for classification is a fully connected layer, which starts with a flattening step, then a fully connected layer (which is a layer full of connections to do classification, also called the dense layer) and attached with softmax function.

## Flattening
The output of the convolutional part of the CNN is converted into a 1D feature vector, to be used by the Fully connected layer. This operation is called flattening. It gets the output of the convolutional layers, flattens all its structure to create a single long feature vector to be used by the fully connected layer for the final classification.

## Fully Connected Layer (FC)
In this layer, where the weight and bias are the same as the normal neural network, use cost to compute the loss function, gradient descent to optimize parameters, and reduce cost function.

## Activation Function
 The output from the Fully Connected Layer is then passed through the activation function. It can be softmax or any other function depedning on the problem.

 # Putting Everything Together

![ALT TXT](https://miro.medium.com/max/1400/0*bYlcS6GpW0T2ZoQL.png)

# Read More
1. [Youtube video to have a clear picture of CNN by Brandon Rohrer](https://www.youtube.com/watch?v=FmpDIaiMIeA&t=870s)
2. [Intro to CNN by Adit Deshpande](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/)
3. [Deeper understanding on CNN by Ujjwal Karn](https://www.kdnuggets.com/2016/11/intuitive-explanation-convolutional-neural-networks.html)