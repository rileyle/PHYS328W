---
title:      Python/JupyterLab Setup
layout:     single
---
## Install and Configure Anaconda

You will use Jupyter Notebook for your electronic log book (ELN). It provides the [Python](https://www.python.org){:target="_blank"} programming language for computational work, and [Markdown](https://daringfireball.net/projects/markdown){:target="_blank"} with [L<SUP>A</SUP>T<SUB>E</SUB>X](https://www.latex-project.org){:target="_blank"} support for writing notes.

The Anaconda package provides the Python language with lots of useful libraries, and [Jupyter Notebook](https://jupyter.org){:target="_blank"}.

### Requirements

You will need a Windows 10 laptop or a MacBook. If you have a Chromebook, let me know right away. We will need to figure out an alternative.

### Install

- (If you have an older version of Anaconda, uninstall it (Windows: Settings -> Apps, macOS: drag anaconda to the trash in file manager and empty trash) and do a fresh re-install.) 
- Download the installer for your operating system (Windows, macOS, or Linux) from [https://www.anaconda.com/download](https://www.anaconda.com/download/){:target="_blank"}. 
- Run the installer, and stick with the default options. (In the process, you should see that you are installing Python version 3.8.) 

### Create an Anaconda Environment, and Set it Up

- Run Anaconda Navigator.
- Click on "Environments" in the panel to the far left.
- Click on "Create", select Python 3.8, and give your environment a name (like "Log Book").
- At the top of the large panel on the right, select "Not installed", and click on "Update index ..." to populate the list of available packages.
- Use the search bar to find and select the following packages (which may already be installed):
  - Search for "numpy", and select "numpy" and "numpy-base".
  - Search for "scipy", and select "scipy".
  - Search for "matplotlib", and select "matplotlib" and "matplotlib-base".
  - Search for "pandas", and select  "pandas".
  - Then, click Apply.

### Set Up Your PHYS328W_yourname Folder

I have shared a folder with you on OneDrive where you should keep all of your Jupyter notebooks for this course.

- If OneDrive is not already installed on your laptop, install it or from the [Microsoft](https://www.microsoft.com/en-us/microsoft-365/onedrive/download){:target="_blank"} (Windows 10) or the [Mac App Store](https://apps.apple.com/us/app/onedrive/id823766827?mt=12){:target="_blank"} (MacBook).
- Sign in to OneDrive in your favorite Web browser, and follow the "Shared" link in the panel on the left.
- You should see a folder with a name starting with PHYS328W. Check the circular check box to the left of the folder, and click "Add Shortcut to My Files".
- Open OneDrive in File Explorer (Windows) or Finder (MacOS) and verify that your PHYS328W shared folder shows up. Initially, it should contain empty subfolders for the JupyterLab Tutorial and each lab. If not, ask for help.

### JupyterLab Tutorial

- Run Anaconda Navigator, select the environment you set up for this course, and launch JupyterLab.  A JupyterLab console should open in a tab in your web browser.
- Download the [JupyterLab Tutorial](JupyterLabTutorial.ipynb) to the Tutorial subfolder of your shared PHYS328W_yourname folder, and open it in JupyterLab:
  - Show the File Manager panel by clicking on the folder icon in the vertical button bar to the far left of the JupyterLab console. 
  - Navigate to PHYS328W_yourname/Tutorial.
  - Double-click on JupyterLabTutorial.ipynb to open the notebook. 
- Helpful Hint: The "Table of Contents" button in the vertical button bar to the far left of the JupyterLab console shows a clickable list of the headers in the current notebook. This makes navigating long notebooks easier. 
