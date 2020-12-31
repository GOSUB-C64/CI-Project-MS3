<!-- Image sourced from Hello World! 
    in 100 Programming Languages | beanz Magazine kidscodecs.com -->
<img src="/static/images/helloWorldBread.jpeg" width="200px" height="200px" style="margin: 0;">

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



# Testing


