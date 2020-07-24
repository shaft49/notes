# Pytorch
    https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&fbclid=IwAR0XT_ZKBQ3KEWOq0FsOVml-dlQLpBCXtYnI47WTuyYRv1Z-KtHoA4Gprwo
# Installation
    https://pytorch.org/get-started/locally/
    Choose according to you OS, GPU availability and package manager

To install the anaconda package manager,

    https://www.youtube.com/watch?v=9nEh-OXVaNI

    Some basic syntax:
    conda --version
    conda create -n name [Python=version] [numpy]
    conda activate name
    conda deactivate                               
    conda env list                          => list all then envs
    conda env remove -n name                => remove env
    conda install p1 p2                     => install packages
    conda list                              => list packages inside a env
    conda search pandas
    conda update pandas                     => latest version
    conda remove pandas
    conda install pip                       => use pip inside env for fallback

If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

    conda config --set auto_activate_base false

# Tensors Basics


    x = torch.empty(2, 3)
    x = torch.rand(2, 2)
    x = torch.zeros(2, 2)
    x = torch.ones(2, 2, dtype = torch.int)
    item = x[1, 1].item()

Tensors to Numpy and vice versa, assignment is call by reference

    y = x.numpy()
    a = np.onses(5)
    b = torch.from_numpy(a)

Tensors in GPU

    if torch.cuda_is_available():
        device = torch.device("cuda")
        x = torch.ones(5, device = device) #gpu tensor
        or,
        x = torch.ones(5) #cpu tensor
        y = y.to(device) #gpu tensor
        z = y.to("cpu") #cpu tensor
        numpy can handle only cpu tensor.

# Autograd

    x = torch.randn(3, requires_grad=True)
    y = x + 2
    z = y*y*2
    z = z.mean()
    z.backward() # only for scalr value, if not scalar then need to provide a vector in params
    print(x.grad)


Three ways to remove the autograd for a variable
    
    x = torch.randn(3, requires_grad=True)
    x.requires_grad_(False)
    y = x.detach()
    with torch.no_grad():
        y = x + 2

Need to erase the gradient before going to the next epoch, as gradient is cumulative sum

    x = torch.ones(4, requires_grad=True)

    for epoch in range(3):
        y = (x*3).sum()
        y.backward()
        print(x.grad)
        x.grad.zero_()

# Backpropagation

    Same as in autograd example.

# Training Steps

    0. Prepare Datasets
    1. Design Model (input size, output size, forward pass)
    2. Construct loss and optimizer
    3. Training Loop
        -forward pass: compute prediction and loss
        -backward pass: gradients
        -update weights