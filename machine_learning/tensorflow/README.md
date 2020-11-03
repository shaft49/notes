# Tensorflow Course from Python Engineer

- Click [here](https://www.youtube.com/playlist?list=PLqnslRFeH2Uqfv1Vz3DqeQfy0w20ldbaV) to see the full course. See the Notebook for summary
- [Github Repo Link]()https://github.com/python-engineer/tensorflow-course

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

## Save & Load Models

- Option 1: Save Whole Model

  - Tensorflow Saved Model
    > model.save('model_name')
  - HDF5 Format
    > model.save('model_name.h5')

  > model = keras.models.load_model('model_name.h5')

- Option 2: Save Only Weights

  > model.save_weights('model_name.h5')

  - Need to initialize the whole model before loading the weights
    model = Same model that you use to save weights

  > model.load_weights('model_name.h5')

- Option 3: Save only architecture, to_json, you need to train it again before you can use it to predict

        json_string = model.to_json()
        with open('model_name.json', 'w') as write_file:
            write_file.write(json_string)

        with open('model_name.json', 'r') as read_file:
            loaded_json_string = read_file.read()

        model = keras.models.load_from_json(loaded_json_string)

  > Now you need to train the model again.

## Functional API

Important for transfer learning

- [Documentation Link](https://www.tensorflow.org/guide/keras/functional)

  base_model = keras.applications.VGG16()
  x = base_model.layer[-2].output
  new_outputs = keras.layers.Dense(1)(x)
  new_model = keras.model(inputs = base_model.inputs, outputs = new_outputs)
