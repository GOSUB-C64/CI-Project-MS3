<!-- Image sourced from Hello World! 
    in 100 Programming Languages | beanz Magazine kidscodecs.com -->
<img src="/static/images/screenshots/helloWorldBread.jpeg" width="200px" height="200px" style="margin: 0;">

# World of Breads
* Milestone Project #3 
#
<div id="top"></div>

# Contents

+ <a href="#context">Context</a>
+ <a href="#ux">UX</a>
  + <a href="#summary">Summary</a>
  + <a href="#design">Design</a>
  + <a href="#user">User Stories / Goals</a>
  + <a href="#dev">Developer's / Goals</a>
  + <a href="#wire">Wireframes</a>
+ <a href="#feats">Features</a>
  + <a href="#feats">At present</a>
  + <a href="#feats">In future</a>
+ <a href="#tech">Technologies used</a>
+ <a href="#tests">Testing</a>
  + <a href="#auto"> Automated</a>
  + <a href="#man">Manual</a>
  + <a href="#res">Responsiveness</a>
  + <a href="#resolved">Issues solved</a>
  + <a href="#unsolved">Unsolved Issues</a>
+ <a href="#deploy">Deployment</a>
+ <a href="#cred">Credits</a>


<div id="context"></div>

# Context

'World Of Bread' was an idea I came up with because of my background as a chef and the love of the art of making fantastic loaves of bread with such simple ingredients as flour and water and just the sheer pleasure of eating it.


<div id="ux"></div>

# UX


<div id="summary"></div>

## Summary

The website was designed with simplicity at heart.
Any user can come to the site and 'add' to the growing database of breads.

A user can:
+ enter their own bread recipe
+ take a recipe they want from the collection.
+ edit other users' recipes to shape the community's experience.
+ not delete any recipes.



<div id="design"></div>

## Design
Colours chosen to reflect simplicity.




<div id="user"></div>

# User Stories

## Ideas to assist in developing MS3 project.
(overall goal - I want the site to grow) 

+ user story 1

    On accessing the site the user should be able to see a welcome image which is related to the overall purpose of the website.

+ user story 2

    As a user (who is interested in what this site is all about) I'd expect to see a short description of the reason for the site's existence and what the user can achieve during their visit.

+ user story 3

    As a contributing user, I'd like to ADD to the website by inputting information so it is grouped with the rest.

+ user story 4

    As a returning visitor I'd like to see my recently added information.

+ user story 5

    As a contributing user, I'd like to have the ability to edit/update my recently added contribution.

+ user story 6

    As a contributing user, I'd like the power to delete my recently added information if I've changed my mind.

+ user story 7

     As a returning user - I'd like the ability to search through all the available information using certain search criteria; for example... search all records on the world encyclopedia website for information on 'forests' - it should list ALL forests.

+ user story 8

    As any user to the site - I must not be able to change/remove any other records on file that do not belong to me.

+ user story 9

    As a first time user - I should be able to register with the site and then log in.

+ user story 10

    As a returning user I should have the ability to 'login' and/or 'logout' with confirmation on screen

+ user story 11

    As any user I should be able to easily navigate to what I want to do next, easily.

+ user story 12

    As a contributing user after adding to the site there should be a thankyou message thanking the user for their contribution.

<div><a href="#top">(TOP)</a></div>





<div id="dev"></div>

## Developer's Goals




<div id="wire"></div>

## Wireframes

 + To view the wirefrmes for this project [click here](https://github.com/GOSUB-C64/CI-Project-MS3/tree/master/static/project_wireframes/data-centric-MS3-project-wireframes.pdf)

The final implementation based on the original wireframe design had to be augmented for practicality and timing reasons in that I had to reduce the overall functionality of the website due to project time constraints.

Unused (but: to be added at a later date)

+ Registration
+ Log in
+ Log out
+ Searching ability


Of the pages that have been implemented, changes from the original design (wireframes) are as follows...

+ homepage shows one row of 4 cards instead of the initial 2 rows of 3 cards due to wanting to get more information displayed to the user about the recipe.
+ display_breads.html - lists all breads in database. This page needed to have more breathing space for the content compared to what was originally thought as some 'methods/instructions' are quite long in the recipe.
+ display_recipe.html - which details the ingredients and method on how to make the selected bread yourself accompanied by an image of the bread.
+ add_recipe - final version remained close to concept with only a few extra fields needed for clarity -e.g. a cooking temperature.
+ edit_recipe - here you can edit the bread recipe you've just clicked on to change any details you like. This page is quite similar to the edit_recipe page so most of the design was already done and reused.


All functionality of C.R.U.D. has been put in place.

<div id="feats"></div>

# Features

## present features

+ #1 Users can view all recipes in alphabetical order in an accordian style page control.

+ #2 Users can add their own bread recipes to the collection and then view them.

+ #3 Users can view the first 4 recipes stored in the collection that have a field of 'is_featured' set to true.

+ #4 The input for the 'country of origin' section has been controlled by a selector.


## future features

+ #1 Users will be able to print out a readable copy of the chosen recipe.

+ #2 Users' image url's will be processed so that only a relative url is used. This will ensure optimal page loading times.

+ #3 A login/logout and registration ability should be added to keep site secure.



<div id="tech"></div>

# Technologies used

These are the technoloigies that were used to create this website. Click on any one of them for more information.

+ [HTML](https://www.tutorialrepublic.com/html-tutorial/)
+ [CSS](https://www.tutorialrepublic.com/css-tutorial/)
+ [Javascript](https://www.tutorialrepublic.com/javascript-tutorial/)
+ [jQuery](https://www.tutorialrepublic.com/jquery-tutorial/)
+ [Python3](https://www.python.org)
+ [PyMongo](https://pypi.org/project/pymongo/)
+ [MongoDB](https://www.mongodb.com/2)
+ [Heroku](https://www.heroku.com/what)
+ [Gitpod](https://www.gitpod.io/)
+ [Github](https://www.howtogeek.com/180167/htg-explains-what-is-github-and-what-do-geeks-use-it-for/)
+ [Font Awesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/)
+ [Favicon](https://favicon.io/)
+ [Image Resizer](https://imageresizer.com/)
+ [LightHouse](https://developers.google.com/web/tools/lighthouse/)
+ [Balsamiq](https://stackshare.io/balsamiq)
+ [Materialize CSS](https://materializecss.com/)
+ [Flask](https://www.tutorialspoint.com/python_web_development_libraries/python_web_development_libraries_flask_framework.htm)
+ [Jinja Templaing](https://docs.appseed.us/what-is/jinja/)


# Testing

## Automated

+ All HTML was tested using a [HTML Validator](https://validator.w3.org/nu/#textarea) by entering the deployed heroku website address and running the checker.
+ Found 6 <img alt=""> errors which were solved by adding some Jinja expressions into the quotes for example ```<img src="/images/image.jpg" alt="{{ expression }}">```
+ All CSS was tested using [this validator](https://jigsaw.w3.org/css-validator/validator) and all tests passed successfully.
![Passed](/static/images/screenshots/css_validator.png)
+ Python code was ran through [this validator](https://extendsclass.com/python-tester.html) and no syntax errors found.
![Passed](/static/images/screenshots/python_validator.png)


## Manual Testing

+ Test #1: VISUAL - do all pages on the site look good to the eye?
    + Yes.
+ Test #2: DATA VERIFICATION: Is the app able to receive data back from the Mongo Database?
    + Yes.
+ Test #3: EDITING A RECORD: After editing a record and updating the database, did viewing the record again confirm this?
    + Yes.


## Testing user stories

### user story 1

+ On accessing the site the user should be able to see a welcome image which is related to the overall purpose of the website.
    + **Comment** (To be implemented later - due to time restrictions)

### user story 2

+ As a user (who is interested in what this site is all about) I'd expect to see a short description of the reason for the site's existence and what the user can achieve during their visit.

    + **Comment** (To be implemented later - due to time restrictions)

### user story 3
+ As a contributing user, I'd like to ADD to the website by inputting information so it is grouped with the rest.

    + **Comment** *"yes this functionality was added and tested by filling in the input fields of the form and getting a status message of 'added successfully' when form was submitted to the database"*

### user story 4
+ As a returning visitor I'd like to see my recently added information.

    + **Comment** *"If you click on 'All Recipes' you can see your entry listed with some others alphabetically"*

### user story 5
+ As a contributing user, I'd like to have the ability to edit/update my recently added contribution.

    + **Comment** *"Yes you can, just find your entry on the home page and click any content within the card and you'll be taken to the 'disply_recipe' page where you can see the recipe in its entirety and from here can click the 'edit' button at top right to edit your contribution"*

### user story 6
+ As a contributing user, I'd like the power to delete my recently added information if I've changed my mind.

    + **Comment** *" TBA "*

### user story 7
+ As a returning user - I'd like the ability to search through all the available information using certain search criteria; for example... search all records on the world encyclopedia website for information on 'forests' - it should list ALL forests.

    + **Comment** *"not implemented due to time restraints"*

### user story 8
+ As any user to the site - I must not be able to change/remove any other records on file that do not belong to me.

    + **Comment** *"no user autentication implemented at the moment but will be at a later date"*

### user story 9
+ As a first time user - I should be able to register with the site and then log in.

    + **Comment** *"no user autentication implemented"*

### user story 10
+ As a returning user I should have the ability to 'login' and/or 'logout' with confirmation on screen

    + **Comment** *"no user autentication implemented"*

### user story 11
+ As any user I should be able to easily navigate to what I want to do next.

    + **Comment** *"The site is fairly intuitive with nav menu and the user easily not easily distracted due to the simplicity of the site"*

### user story 12
+ As a contributing user after adding to the site there should be a thankyou message thanking the user for their contribution.

    + **Comment** *"Yes a message pops up in the flash messages thanking the user for their contribution"*


# Deployment

+ GitHub Pages wont suffice for this project as it doesn't support the Python3 programming language, a non-relational database like SQL, or Jinja Templating.

Outlined below are the steps needed to deploy a website to Heroku.
1. The first thing we need to do is tell Heroku what dependencies are need to run our app so in the Command Line Interface (which I'll refer to as the **CLI** going forward) type ```pip3 freeze --local > requirements.txt```
2. Now we need to give Heroku a 'Procfile'. Heroku automatically looks for this file so it can know how to run our app. You can ceate this file by typing ```echo web: python app.py > Procfile``` into the CLI and make sure to give the filename an uppercase 'P' else it wont work.
3. These files should now show up in your files list in the file explorer.
4. Important to note that the Procfile sometimes adds a blank line to the last line of the file (the only line in this case) so remove it as it may cause runtime problems with Heroku trying to run apps.
5. Next go to the Heroku website and log in > create new app > and give it a unique name.
6. Next select the region then **create app**
7. Next we need to connect our app to Heroku and we can do it in a couple different ways...
    +  ## Using the Heroku Toolbelt via the CLI, so type...
        + ```npm install -g heroku```
        + next, when Heroku has installed, type ```heroku login -1``` and enter your Heroku login details.
        + To see any apps that was created earlier type ```Apps``` in the CLI
        + To rename an app type ```heroku apps:rename ``` then the new app name.
        + Next, the web files will need to be 'pushed' to Heroku.
        + But first the Heroku app needs to be linked back to Git local repository.
            + After getting the files all staged by typing ```git add .``` or ```git add -A``` followed by a commit message ``` git commit -m "your commit message to git goes here" ```
            + next - retrieve the Heroku git URL from the settings menu page in Heroku website
            + In the CLI type ```git remote add```, then a name for our new remote, for example **heroku** then paste in the Heroku Git URL.
            + To check this has set up properly, type ```git remote -v``` and you should see all available remote connections we can use to push our website to.
            + To push to the newly created remote on Heroku - type ```git push -u heroku master``` and this will push our code to Heroku just like pushing to Github.
            + Because the files **requirements.txt** and **Procfile** were created earlier, there shouldnt be any difficulties in pushing your code to Heroku
            + see [here](https://devcenter.heroku.com/categories/deploying-with-git) for more information on deploying from Git to Heroku.


    + ##  Automatic Deployment from GitHub repository.
        + Click the **deploy** menu tab in the Heroku dashboard screen.
        + Next click on the **connect to Github** button 
        + Your Github profile will appear and next to that you can select your repository name that you want Heroku to connect to.
        + Click **search** then click **connect**
        + Next we have to inform Heroku of any hidden environment variables so that our app can run problem free.
        + Still on Heroku, click on the **Settings** menu tab, and then click on **Reveal Config Vars**
        + Here we can securely tell Heroku which variables are required.
        + In a file called *env.py*, there should be a few different variables that were created for seamless connection to Git and you may have other environment variables for other platforms such as databases(MongoDB)
        + The first variable is **IP**, with the value of **0.0.0.0**
        + Next, the **PORT**, which is **5000**
        + For the **SECRET_KEY**, let's copy that from the *env.py* file, then paste it into Heroku.
        + Next the **MONGO_URI** string goes here.
        + Finally - **MONGO_DBNAME** is the name of the database to connect to.
        + Next in the **deploy** menu tab click **Enable automatic deployment**
        + Lastly click on **Deploy branch** for Heroku to connect to Github.
        + You should see this setting up on screen.
        + When done you can click **Open App** if all went well you should be able to see your app with your new Heroku URL.
  

# How to download and run repository on Local Machine

+ There are 2 main ways to do this:
    + Clone a copy from Github.
    + Use a **browser plugin or addon** which simplifies matters.

## Clone a copy
1. Go to [this Github repository](https://github.com/GOSUB-C64/CI-Project-MS3) and click on the **Code** button
2. This will open up the small *Clone* window.
3. Keeping the 'HTTPS' tab selected, click to copy the provided url link.
4. Next , open your preferred IDE with a previously created new Github repository and in the CLI navigate to the directory you'd like to clone to.
5. Type ```git clone``` and paste in the copied link from the clipboard and execute that line.
6. When the repo has been cloned you should see all the files associated with this workspace.
7. Next you'll have to create the **env.py** file spoken of previously and add these settings..
    + ```import os```
    + ```os.environ.setdefault("IP", "0.0.0.0")```
    + ```os.environ.setdefault("PORT", "5000")```
    + ```os.environ.setdefault("SECRET_KEY", "your-secret-key-goes-here")```
    + ```os.environ.setdefault("MONGO_URI", "mongodb+srv://root:your-password-goes-here@myfirstcluster.9yyun.mongodb.net/world_of_bread?retryWrites=true&w=majority")```
    + ```os.environ.setdefault("MONGO_DBNAME", "name-of-your-database-goes-here")```
8. After this has been entered and all is correct, you can push back to your own Github repo.


## Use a browser plugin or addon

1. If using Google Chrome:
    + Click 3 dots button under the **x** button for exiting browser to access the main menu
    + Find More Tools > Extensions
    + From the main menu (burger icon - top left) find and click **open web store**
    + From here search for **gitpod** extension and click *Gitpod - Dev Environments in a Browser Tab* to install to your Google Chrome Browser.
    + Once its installed and running go to [this Github repository](https://github.com/GOSUB-C64/CI-Project-MS3)
    + Now click the green Gitpod button which should have appeared next to the CODE button.
    + The rest of the process is automatic.
    + After it has fully finished downloading, you can simply run the app by typing ```python3 app.py``` in the CLI terminal window.
    