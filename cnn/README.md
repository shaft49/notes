# Basic of CNN for Beginners
A CNN is a class of deep, feed-forward (not recurrent) artificial neural networks that are applied to analyzing visual imagery.

# Things to note before reading
1. Images are just matrices of pixel values.
2. Channel is a conventional term used to refer to a certain component of an image. An image from a standard digital camera will have three channels — red, green, and blue (RGB). While a grayscale image has only one channel. The value of each pixel in the matrix will range from 0 to 255.

# Convolutional Layer
Filter is an **X** detector, which acts like a sliding window and perform element-wise multiplication to search the **X** pattern in the image.  If a certain part in the image looks like **X**, the value of the convolved feature (feature maps/activation map, these terms are used interchangeably) for that part in the next layer will be high.

If to detect more patterns, more types of filters will be needed. Here is the part where the depth of the next layer comes in. Let’s say you use 3 filters, which is **X**, **O** and **I** detector to slide through the images, then the next layer of the network will be **depth=3**.

The filter can also be the filter for detecting color contrast, texture, etc. of the images, depending on the prediction task that you want the CNN to learn

![ALT TXT](https://miro.medium.com/max/866/1*4bkq6f6ZU3PkPzEHXfJrLQ.png)