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

# User Stories / Goals of the user

### These are about how the site is to work from a user point of view.

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

The long-term goal for the developer/website owner is to eventually have a substantial pool of bread recipes from every corner of the planet.


<div id="wire"></div>

## Wireframes

 + To view the wirefrmes for this project [click here](https://github.com/GOSUB-C64/CI-Project-MS3/tree/master/static/project_wireframes/data-centric-MS3-project-wireframes.pdf)

The final implementation based on the original wireframe design had to be augmented for practicality and timing reasons in that I had to reduce the overall functionality of the website due to project time constraints.

Unused (but: to be added at a later date)

+ Searching ability


Of the pages that have been implemented, changes from the original design (wireframes) are as follows...

+ **home.html**
    + shows one row of 4 cards instead of the initial 2 rows of 3 cards due to wanting to get more information displayed to the user about the recipe.
+ **display_breads.html**
     - lists all breads in database. This page needed to have more breathing space for the content compared to what was originally thought as some 'methods/instructions' are quite long in the recipe.
+ **display_recipe.html**
     - which details the ingredients and method on how to make the selected bread yourself accompanied by an image of the bread.
+ **add_recipe.html** 
    - final version remained close to concept with only a few extra fields needed for clarity -e.g. a cooking temperature.
+ **edit_recipe.html**
     - here you can edit the bread recipe you've just clicked on to change any details you like. This page is quite similar to the edit_recipe page so most of the design was already done and reused.
+ **login.html** 
    - A page used to Log the user in to the site - A session cookie is created here.
+ **logout.html**
    - A page to safely log the user out. session cookie deleted
+ **profile.html**
    - This page will ONLY list those recipes created by the user in session. The user also has the ability to edit or delete their own additions to the database.

## *all html pages inherit from the base.html*

***All functionality of C.R.U.D. has been put in place***

<div id="feats"></div>
<div><a href="#top">(TOP)</a></div>


# Features

## present features

+ #1 Users can Register for a simple account.

+ #2 Users can Login to their account profile.

+ #3 Users can Logout of their profile.

+ #4 Users can see their own content via their profile.

+ #5 Users can view all recipes in alphabetical order in an accordian style page control.

+ #6 Users can add their own bread recipes to the collection and then view them.

+ #7 Users can edit ONLY their own recipes via their profile page.

+ #8 Users can delete ONLY their own recipes via their profile page.

+ #9 Users can view the first 4 recipes stored in the collection that have a field of 'is_featured' set to true.

+ #10 The input for the 'country of origin' section has been controlled by a selector to avoid any typos.


## future features

+ #1 Users will be able to print out a readable copy of the chosen recipe.

+ #2 Users' image url's will be processed so that only a relative url is used. This will ensure optimal page loading times.

+ #3 A login/logout and registration ability should be added to keep site secure.

+ #4 To have a bread recipe properly featured, users would use their 1 up-vote and the recipe with most votes at end of week would be featured on the homepage until it doesn't qualify.


<div id="tech"></div>
<div><a href="#top">(TOP)</a></div>


# Technologies used

These are the technoloigies that were used to create this website. Click on any one of them for more information.

+ [HTML](https://www.tutorialrepublic.com/html-tutorial/)
    - ***Hypertext Markup Language is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript***
+ [CSS](https://www.tutorialrepublic.com/css-tutorial/)
    - ***CSS is short for Cascading Style Sheets, and is the preferred way for setting the look and feel of a website***
+ [Javascript](https://www.tutorialrepublic.com/javascript-tutorial/)
    - ***JavaScript is the Programming Language for the Web. JavaScript can update and change both HTML and CSS***
+ [jQuery](https://www.tutorialrepublic.com/jquery-tutorial/)
    - ***jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax***
+ [Python3](https://www.python.org)
    - ***Python is an interpreted, high-level and general-purpose programming language***
+ [PyMongo](https://pypi.org/project/pymongo/)
    - ***pymongo is a native Python driver for MongoDB***
+ [MongoDB](https://www.mongodb.com/2) 
    - ***this is where the database was created***
+ [Heroku](https://www.heroku.com/what)
    - ***A hosting platform like Github pages but with the ability to support more frameworks***
+ [Gitpod](https://www.gitpod.io/)
    - ***Gitpod is an online IDE that supports many languages and Git commands***
+ [Github](https://www.howtogeek.com/180167/htg-explains-what-is-github-and-what-do-geeks-use-it-for/)
    - ***GitHub provides hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features***
+ [Font Awesome](https://fontawesome.com/)
    - ***A great free source of icons and fonts for use in web development***
+ [Google Fonts](https://fonts.google.com/)
    - ***A wealth of amazing free fonts for developer usage***
+ [Favicon](https://favicon.io/)
    - ***Make your browser tabs stand out and develop free icons for your project***
+ [Image Resizer](https://imageresizer.com/)
    - ***A great online image resizer - just upload > resize > download***
+ [LightHouse](https://developers.google.com/web/tools/lighthouse/)
    - ***Software used to creat a performance audit for your website***
+ [Balsamiq](https://stackshare.io/balsamiq)
    - ***Making wireframe designing simply effortless!***
+ [Materialize CSS](https://materializecss.com/)
    - ***A modern responsiveness css framework which is based on Material Design by Google*** 
+ [Flask](https://www.tutorialspoint.com/python_web_development_libraries/python_web_development_libraries_flask_framework.htm)
    - ***Flask is a web application framework written in Python.  Flask is based on the Werkzeg WSGI toolkit and the Jinja2 template engine***

<div><a href="#top">(TOP)</a></div>

<div id="tests"></div>
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

    + **Comment** *"You can see your added recipes in your profile page - just click on the **profile menu button** at top right. If you click on 'All Recipes' you can see your entry listed with some others alphabetically"*

### user story 5
+ As a contributing user, I'd like to have the ability to edit/update my recently added contribution.

    + **Comment** *"Yes you can, just find your entry on the home page and click any content within the card and you'll be taken to the 'disply_recipe' page where you can see the recipe in its entirety and from here can click the **edit** button at top right to edit your contribution.  You can edit your recipes from your profile page"*

### user story 6
+ As a contributing user, I'd like the power to delete my recently added information if I've changed my mind.

    + **Comment** *" You can now delete your recipes as and when you want thru your profile page"*
    
    Users can ONLY edit/delete their own added content and not that of any other users'.

### user story 7
+ As a returning user - I'd like the ability to search through all the available information using certain search criteria; for example... search all records on the world encyclopedia website for information on 'forests' - it should list ALL forests.

    + **Comment** *"not implemented due to time restraints"*

### user story 8
+ As any user to the site - I must not be able to change/remove any other records on file that do not belong to me.

    + **Comment** *"see user story 8"*

### user story 9
+ As a first time user - I should be able to register with the site and then log in.

    + **Comment** *"Registration is now possible when entering the site via the navbar menu"*

### user story 10
+ As a returning user I should have the ability to 'login' and/or 'logout' with confirmation on screen

    + **Comment** *"Logging in and out of the website is now actioned and having an account is also possible"*

### user story 11
+ As any user I should be able to easily navigate to what I want to do next.

    + **Comment** *"The site is fairly intuitive with nav menu and the user not easily distracted due to the simplicity of the site"*

### user story 12
+ As a contributing user after adding to the site there should be a thankyou message thanking the user for their contribution.

    + **Comment** *"Yes a message pops up in the flash messages (on screen) thanking the user for their contribution"*

<div><a href="#top">(TOP)</a></div>
<div id="deploy"></div>

# Responsiveness






<div><a href="#top">(TOP)</a></div>
<div id="deploy"></div>
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
  
<div><a href="#top">(TOP)</a></div>

# How to download and run repository on Local Machine

## Its important to note here that
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
7. Next you'll have to create an  **env.py** file spoken of previously and add it to your files in the root folder then add that to your git .ignore file.
8. After this has been entered and all is correct, you can **git push** back to your own Github repo.


## Use a browser plugin or addon

1. If using Google Chrome:
    + Click 3 dots to access the main menu (this can be found under the **x** button for exiting browser.
    + Find More Tools > Extensions
    + From the main menu (burger icon - top left) find and click **open web store**
    + From here search for **gitpod** extension and click *Gitpod - Dev Environments in a Browser Tab* to install to your Google Chrome Browser.
    + Once its installed and running go to [this Github repository](https://github.com/GOSUB-C64/CI-Project-MS3)
    + Now click the green Gitpod button which should have appeared next to the CODE button.
    + The rest of the process is automatic.
    + Next install all the dependancies from the included requirements.txt file...
        + type ```pip3 install -r requirements.txt```
    + After this you need to create your own **env.py** file with your own credentials so the app can be finally run on your own local system.
    
2. If using Firefox:
    + go to https://addons.mozilla.org/en-GB/firefox/ on firefox browser
    + search for **gitpod** addon in the addon search box
    + follow on screen instructions to install.

<div><a href="#top">(TOP)</a></div>



