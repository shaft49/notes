# Anconda

- [ ] [Tutorial](https://www.youtube.com/watch?v=9nEh-OXVaNI)

To install the anaconda package manager,

      https://www.youtube.com/watch?v=9nEh-OXVaNI

Some basic syntax:
conda --version
conda create -n name [Python=version] [numpy]
conda activate name
conda deactivate
conda env list => list all then envs
conda env remove -n name => remove env
conda install p1 p2 => install packages
conda list => list packages inside a env
conda search pandas
conda update pandas => latest version
conda remove pandas
conda install pip => use pip inside env for fallback

If you'd prefer that conda's base environment not be activated on startup,
set the auto_activate_base parameter to false:

    conda config --set auto_activate_base false
