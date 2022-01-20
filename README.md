# Assignment #1

The first assignment is about setting up accounts and your programming
environment.  Here are the steps:

0. Install `git` and `python` on your computer.
   For Linux and Mac, `bash` is built-in.
   For windows, you can enable the Windows Subsystem for Linux (WSL) and then install Ubuntu.
   See, e.g., [this page](https://ubuntu.com/wsl) for installation instructions.
   We also suggest using [Anaconda](https://www.anaconda.com/products/individual) to get `python` and related packages

1. If you do not have an account on GitHub yet, please
   [register](https://github.com/signup).

2. Then, join the right session in GitHub classroom:

   - [Session 1](https://classroom.github.com/classrooms/97425980-phys-105a-session-1)
   - [Session 2](https://classroom.github.com/classrooms/97425980-phys-105a-session-2)

3. Once you join GitHub classroom, you can accept the assignment by
   clicking:

   - [Session 1](https://classroom.github.com/a/vxHYdJF3)
   - [Session 2](https://classroom.github.com/a/5l3Frsbk)

4. Follow the instruction on GitHub to `clone` your home work
   repository.
   Specifically, if you use command line, you will clone your copy of
   the assignment by

       git clone git@github.com:uarizona-2021spring-phys105a/01-[YOUR_GITHUB_USERNAME].git

   where `[YOUR_GITHUB_USERNAME]` above is your GitHub username, and
   the repository `01-[YOUR_GITHUB_USERNAME].git` was automatically
   generated for you by GitHub Classroom.

5. To actually work on your assignment, go into the
   `01-[YOUR_GITHUB_USERNAME]` directory and edit the text file
   `assignment.py` to print "hello world".
   Hences on how to print strings from python can be found in the
   [hands-on note](https://github.com/uarizona-2022spring-phys105a/phys105a/blob/main/01/Handson.ipynb).

6. Finally, to submit the assigment, you need to add your script back
   to the repository and push it back to GitHub.
   If you use command line, you may use

       cd `01-[YOUR_GITHUB_USERNAME]` # change-directory into the repository
       git add .                      # add changed files to the "index"
       git commit -m 'Finished'       # commit your changes
       git push                       # push to GitHub, i.e., submission
