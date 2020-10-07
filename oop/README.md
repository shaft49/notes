# Object Oriented Programming
> Go to this link to learn basics on OOP https://www.youtube.com/watch?v=SiBw7os-_zI

## Why Not use the Structures?
> The main issue with the structures is that you cannot define functions within one.

#### Objects are instances of a class

#### Classes are templates for objects

## Four main principles of OOP

* Encapsulation
* Abstraction
* Inheritence
* Polymorphism

### Encapsilation

Encapsulation refers to bundling data with methods that can operate on that data within a class. Essentially, it it the idea of hiding data within a class, preventing anything outside that class from from directly interacting with it. Rather they need interact through methods.

To make an attribute read-only, you would define a getter method but not a setter method. 

### Abstraction

Abstraction refers to only shoewing essential details and keeping everything else hidden. It is like driving a car. It is enough to know simple details to drive the car. You don't need to know how this was made in the first place.

#### Interface: Interface and Implementation


Interface refers to the way sections of code can communicate with another. This typically is done through methods that each class is able to access.

Implementation of these methods, or how these methods are coded, should be hidden.

* Advantage is that it prevents ripple effect [to change in one module you need change in multiple modules]. And each module can individually developed.

### Inheritence
inheritence is the principle that allows classes to derive from other classes.

#### Access Modifiers

* Public: Can be accessed from anywhere in the program. 
* Private: Can be accessed within the class it is defined.
* Protected: Can be accessed within the class it is defined, as well as any subclass of that class.


### Polymorphism
Polymorphism describes methods that are able to take on many forms.
* Dynamic Polymorphism: Occurs during the runtime. Method signature is in both a subclass and a superclass. Methods share the same parameters but have different implementation. Subclass's method overrides the superclass's method. Which implementation of a method (superclass & subclass) will be used is determined dynamically in the runtime.

> This is known as function overriding.
* Static Polymorphism: Occurs during the compile-time. Multiple methods with the same name but different arguments are defined in the same class.

    * Different Number of Parameters
    * Different Types of Parameters
    * Different Order of Parameters

>This is known as method overloading.