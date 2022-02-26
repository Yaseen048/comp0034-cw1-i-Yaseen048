[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6713246&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

The template repository contains a basic structure for coursework 1.

**Do not** use this to determine what to put in the coursework, you must refer to the coursework specification on
Moodle.

## Instructions for using the starter code

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
   or [Cloning a repository in VS Code](https://code.visualstudio.com/docs/editor/github#_cloning-a-repository)
2. Add a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [use python in your shell.](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. PyCharm, VisualStudio Code, Xcode and NetBeans have
   already been added.
5. Copy the prepared data set from COMP0035 coursework to this repository. You may need to use 'git add' to add the file
   to be tracked by git.
6. Commit and push the data set to GitHub. This is your first commit for coursework 1. Remember to use source code
   control throughout the coursework.
7. `dash_app.py` has been included to allow you to test that your project set up is sufficient to run Dash. Once you are
   happy that you have set up the project then you should delete the contents of app.py and replace with your coursework
   code.
    - To run the dash app from the terminal or shell make sure you are in directory of your repository and type and
      run `python dash_app.py`
    - To run the dash app from PyCharm, right click on the file name `dash_app.py` in the Project pane and
      select `Run dash_app`. Or open `dash_app.py` and click on the green run arrow near line 29.
    - To run the dash app from VS Code, use the Run option from the left pane.
8. By default, the dash app should launch on port 8050 of your localhost with the IP
   address [127.0.0.1:8050](http://127.0.0.1:8050/). Open the URL in a browser. Note: If you get an error like
   this: `OSError: [Errno 48] Address already in use` then another application is already using the default port (this
   will also happen if you forget to stop a previous Dash app and try to start another!). You can try another port by
   modifying the line of code that runs the Dash app to specify a different port number
   e.g. `app.run_server(debug=True, port=1337)`

## Before you submit the coursework

Remove the instruction text above and complete this README.md using the guidance in the coursework specification.

## Target audience and questions

The target audience for this dash app are cinema CEOs to help them understand how cinemas and the movie industry were affected due to covid-19 in the UK.

The dashboard is intended to address the following questions:
- How were sales of movies in cinemas affected due to covid-19?
- How was the release of movies affected due to covid-19?
- What were the main movie distributors of films in cinemas during the pandemic?


## Visualisation design

The target audience (cinema CEOs) should have alot of experinece dealing with statistics and graphs as part of theier job is to make big decisions which are often supported by data. Because of this, most CEOs should be able to understand most types of graphs.

The following questions above will be addressed by a bar chart, histogram and pie chart respectivley which cinema CEOs should be comfortable with seeing.

The first question addresses sales of movies and is represensted by a bar chart. I have chosen a bar chart due to its simplicty. The bar chart only tells you how much money was made from a movie which is sufficient to give cinema CEOs an undertsanding of the general perfomance of films in cinemas at a given time. No additional information is needed as the questions is about how much money was made and not why.

The second questions addresses the release of movies in cinemas and is representated by a histogram. This type of chart was chosen beacuse it is easy to look at (comparable to a bar chart) but addresses slighlty more information. The bar chart focuses mainly on one variable (sales - weekend gross) but to answer the second question we need to look at how long the since the movies were orignally released and how many of the movies were new. To do this we define new movies as movies that were released within 3 months, recent movies as movies released between 3 and 12 months, and old movies as movies released over 12 months ago. A histogram helps depict this as the new, recent and old movies can be represented by different class size on the histogram. 

The final questions addresses the main movie distributors. This means we take a look at who dominated the movie industry. To show this, a pie chart makes easy to show what portion of films at a given time in cinema were made by a movie distributor. 



## Evaluation
