---
title:      Python/JupyterLab Setup
layout:     single
---
## Install and Configure Anaconda

You will use Jupyter Notebook for your electronic log book (ELN). It provides the [Python](https://www.python.org){:target="_blank"} programming language for computational work, and [Markdown](https://daringfireball.net/projects/markdown){:target="_blank"} with [L<SUP>A</SUP>T<SUB>E</SUB>X](https://www.latex-project.org){:target="_blank"} support for writing notes.

The Anaconda package provides the Python language with lots of useful libraries, and [Jupyter Notebook](https://jupyter.org){:target="_blank"}.

### Install
- (If you have an older version of Anaconda, uninstall it (Windows: Settings -> Apps, macOS: drag anaconda to the trash in file manager and empty trash) and do a fresh re-install.) 
- Download the installer for your operating system (Windows, macOS, or Linux) from [https://www.anaconda.com/download](https://www.anaconda.com/download/){:target="_blank"}. 
- Run the installer, and stick with the default options. (In the process, you should see that you are installing Python version 3.8.) 

### Create an Anaconda Environment, and Set it Up
- Run Anaconda Navigator.
- Click on "Environments" in the panel to the far left.
- Click on "Create", select Python 3.8, and give your environment a name (like "Log Book").
- At the top of the large panel on the right, select "Not installed", and click on "Update index ..." to populate the list of available packages.
- Use the search bar to find and select the following packages:
  - Search for "numpy", and select "numpy" and "numpy-base".
  - Search for "scipy", and select "scipy".
  - Search for "matplotlib", and select "matplotlib" and "matplotlib-base".
  - Search for "pandas", and select  "pandas".
  - Then, click Apply.
- Click on "Home" in the panel to the far left, and ...
  - Click the "Install" button under "CMD.exe Prompt".
  - Launch "CMD.exe Prompt"
    - Enter "conda install -c conda-forge jupyterlab=3" at the prompt and hit <Enter>.
    - Once it is finished installing, typle "exit" <Enter> to close the window.
  - Click the "Refresh" button at the upper right of the Anaconda Navigator window, and you should see that there is a "Launch" button under JupyterLab 3.x.x.

### Alternative to Anaconda

Anaconda is the preferred method of using Jupyter Notebook for your electronic log book. If you run into difficulty installing and using Anaconda/Jupyter on your laptop, There is a backup plan.  Anyone with a google account can use [Google Colab](https://colab.research.google.com){:target="_blank"} to sore and run Jupyter notebooks in the cloud. Notebooks are stored in your Google Drive, and with a small addition to a notebook, you can open data files on your Drive. Please let me know right away if you find that you need to pursue this alternative. 

### Set up your log book for your first experiment

- Run Anaconda Navigator, select the environment you set up for this course, and launch JupyterLab.  A JupyterLab console should open in a tab in your web browser.
- Download the Log Book Tutorial  download, and upload it to JupyterLab:
  - Show the File Manager panel by clicking on the folder icon in the vertical button bar to the far left of the JupyterLab console. 
  - Click on the "Upload Files" button at the top of the file browser panel.
- Double-click on the LogBookTutorial.ipynb link to open the notebook. 
- Helpful Hint: The "Table of Contents" button in the vertical button bar to the far left of the JupyterLab console shows a clickable list of the headers in the current notebook. This makes navigating long notebooks easier. 
