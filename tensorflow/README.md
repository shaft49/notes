# Tensorflow Course from Python Engineer
Click [here](https://www.youtube.com/playlist?list=PLqnslRFeH2Uqfv1Vz3DqeQfy0w20ldbaV) to see the full course. See the Notebook for summary

## If you want to suppress the warning

    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

## Lecture 1: How to Install Tensorflow and use virtual environemnt in conda

## Lecture 2: Basics of Tensors

A tensor is the center object in the tensorflow library. All operations are based on the tesnsors. A tensor is like a numpy n-d array.
1. nd-array
2. GPU Support
3. Computation Graph / Backpropagation
4. immutable

## EagerTensor

    It evaluates the operation immediately without building the computational graph.

## Variable Parameters

    Tensorflow variable parameter is used to store the model parameteres while training
    But most of the cases we'll use Keras and we don't have to worry about this.


To see the different functions please check out the notebook.

    tf.constant tf.zeros tf.one tf.random tf.eye tf.range tf.add tf.subtract tf.divide tf.multiply tf.tensordot tf.matmul tf.cast
    slicing / indexing
    tf.reshape
    numpy to tensor and vice versa