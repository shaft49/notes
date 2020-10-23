# Preparation for Data Science Interviews

## Theoretical Interview Question [link](https://github.com/alexeygrigorev/data-science-interviews/blob/master/theory.md)

---

### Supervised Machine Learning

- Dataset will be labelled. Both Feature (X) and label (y) will be given.

---

### Linear Regression

- Linear Regression: y = mx + c
- Polynomial Regression: ax^2 + bx + c = 0

---

### **What if we want to build a model for predicting prices? Are prices distributed normally? Do we need to do any pre-processing for prices?**

Data is not normal. Specially, real-world datasets or uncleaned datasets always have certain skewness. Same goes for the price prediction. Price of houses or any other thing under consideration depends on a number of factors. So, there's a great chance of presence of some skewed values i.e outliers if we talk in data science terms.
Yes, you may need to do pre-processing. Most probably, you will need to remove the outliers to make your distribution near-to-normal.

### **What is gradient descent? How does it work?**

Gradient descent is an algorithm that uses calculus concept of gradient to try and reach local or global minima.

It works by taking the negative of the gradient in a point of a given function, and updating that point repeatedly using the calculated negative gradient, until the algorithm reaches a local or global minimum, which will cause future iterations of the algorithm to return values that are equal or too close to the current point. It is widely used in machine learning applications.

### **What is SGD  —  stochastic gradient descent? What’s the difference with the usual gradient descent?**

In both gradient descent (GD) and stochastic gradient descent (SGD), you update a set of parameters in an iterative manner to minimize an error function.

While in GD, you have to run through ALL the samples in your training set to do a single update for a parameter in a particular iteration, in SGD, on the other hand, you use ONLY ONE or SUBSET of training sample from your training set to do the update for a parameter in a particular iteration. If you use SUBSET, it is called Minibatch Stochastic gradient Descent.

### **What is Bias Variance Trade Off?**

- Bias is the difference between the average prediction of our model and the correct value which we are trying to predict. Model with high bias pays very little attention to the training data and oversimplifies the model. It always leads to high error on training and test data.
- Variance is the variability of model prediction for a given data point or a value which tells us spread of our data. Model with high variance pays a lot of attention to training data and does not generalize on the data which it hasn’t seen before. As a result, such models perform very well on training data but has high error rates on test data.
- We want Low Bias and Low Variance.
- Underfitting: High Bias and Low Variance.
- Overfitting: Low Bias, High Variance. When your model perform very well on your training set but can't generalize the test set, because it adjusted a lot to the training set.
  ![](https://miro.medium.com/max/936/1*xwtSpR_zg7j7zusa4IDHNQ.png)

- This tradeoff in complexity is why there is a tradeoff between bias and variance. An algorithm can’t be more complex and less complex at the same time.
- To build a good model, we need to find a good balance between bias and variance such that it minimizes the total error.

  ![](https://miro.medium.com/max/882/1*SKHGhoGKnBh_GPGHI2Ktvw.png)

- An optimal balance of bias and variance would never overfit or underfit the model.

  ![](https://miro.medium.com/max/1124/1*RQ6ICt_FBSx6mkAsGVwx8g.png)

---

## Classification

### **What are precision, recall, and F1-score?**

- Precision and recall are classification evaluation metrics:
- P = TP / (TP + FP) and R = TP / (TP + FN).
- Where TP is true positives, FP is false positives and FN is false negatives
- In both cases the score of 1 is the best: we get no false positives or false - negatives and only true positives.
- F1 is a combination of both precision and recall in one score (harmonic mean):
- F1 = 2 \* PR / (P + R).
- Max F1 score is 1 and min is 0, with 1 being the best.
