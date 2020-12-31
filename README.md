# Cosseted Classics
## I have designed this site to give the Classic owner the ability to showcase and sell their cherished classic, be it, a motor bike, car or a boat, or just some of the parts for any the above.
## The site could be further developed to show clips of the classics running, giving a walk around the classic. 

# Site Goals
## The site is designed to allow users to easily search for classics for sale, and then for the logged in user to find classics for sale and to be allowed to buy, sell classics and edit their current classified adds.
## The users are only able to see approved items in the list. This happens once the administrator has approved the advert, only the administrator has the ability to approve adverts and delete them. Each user has a different profile and sees only the menus applicable to their group.

# UX / User Experience

## First Time Visitor Goals
### As a First Time Visitor, I want them to be able to be able to, login and create an account easily.
### Once logged in they need to be able to find classics for sale. They can then navigate easily to the items for sale, the classified adds. 

## Returning Visitor Goals
### As a Returning Visitor, I want them to be able to find what the want and to be able to sell and buy items quickly and easily.
### The returning user would need to be able to view their profile and to be able to remove any un-needed adds from the site, this can be done from the both; the classified adds and the user profile pages.

# Design / Features

## The site has been designed allow users to only see approved adverts for classics. The adverts are approved by the admin account holder.
## New sales types can be reviewed and added once again only by the Admin, they can also be deleted if they are no longer needed.

## Colour Scheme
### I decided to use a light blue background, no idea why it seems to be calming and relaxed maybe it represents a clear blue sky on a nice day.
### Test was decided to be set to white, the contrast seems to work quite well. White on blue clouds in the sky, it is calming I feel.
## Typography
### Standard fonts from Materialize, I have no need to over complicate this project, I feel standard san serif font is easier to read and therefore better for the user. No need to keep the users confused with stupid hard to read font types, if I did that the users would not be users for long.
## Imagery
### Imagery is important. The images used where all taken from Google searchs and then adapted to my requirement using MS Paint.
## Home Page Wireframe - View
### Below you can see the desktop wireframe;
<img src="/static/images/desktopversion.png">;
## Mobile Wireframe - View
### Below you can see the mobile device wire frame;
<img src="/static/images/mobileversion.png">;
## Features
### Responsive on all device sizes
#### I checked the site out using google chrome and it was resposive

# Interactive elements

## Technologies Used
### Languages Used
#### HTML5
#### JavaScript
#### CSS3
#### DNSPYTHON
#### Flask-pymongo
#### Werzoeug
## Frameworks, Libraries & Programs Used
### Materialize
#### Materialize was used to assist with the responsiveness and styling of the website.
### Font Awesome:
#### Font Awesome was not used as the one icon I wanted did not display correctly so I made my own.
## GitPod
### GitPod was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
## GitHub:
### GitHub is used to store the projects code after being pushed from Gitpod.
## PC Paint:
### PC Paint was used to create the wireframes during the design process this was due to the free version of Balsmic running out, but in fairness it worked as well and was able to show the basic page layout.

# Testing
## I have started to create the base of the website, I had an issue getting the site to work correctly when in mobile mode, the hamburger is displayed, but when you click on it the dropdown menu is not displayed, therefore the js file does not load and work correctly. Once I cure that by adding the correct links to JS the site worked correctly.
## After lots of work and re listening to lessons, I found the correct way to get the Mongo Data Base talking to my GitPod project and then deployed on Heroku, still having issue with Heroku. After re-listening to the lessons, I found that I did not have the correct requirement in the requirements.txt file after listing them correctly the deployment worked .
## Working on GitPod template hoping to get the sign in sorted, all seems to work after some teething problems, these down to some naming errors in the app.py file, once corrected all is well.
## Getting the website to right to the MongoDB, I needed to used the correct logic and re-listen to the tutorials in order to get the logic sorted. Once I got the correct logic, it was easy.
## Adding sell item and sell classic to the app.py file and getting them to right to the data base I needed to re-listen to the tutorials again.
## Edit Sales item, the field should be populated from the MongoDB, this is not happening, after talking with the tutors, I was able to solve this error, code amended and now it works.
## The edit button throws an error, the error is “an unexpected argument”, this was due to an error in the app.py. Once I reverted back to the pre error version of the app.py file I was able to see what had gone wrong and fix it.
## After talking with my mentor I decided to simplify my site as I had too many categories in it, and it made fault finding very tricky as it felt like I was chasing my tail.
## I have added a view sales categories very similarly to the add tasks section in the mini project, the mini project was very helpful in this part of the project.
## I had an issue where the admin had to approved adverts in order tp show them, this was due to the admin approving the adds, the admin took ownership of the advert, this is not an issue that was apparent too early on in my design until I created the user profile section, the admin owned all the ads, and the person that created them did not. This was sorted out once I was aware of the issue.
## The site was then tidied up ready to submit it, new adds added and text made consistent throughout the site.

### Lighthouse Report
#### From the report you can see that performance is good, accessibility is not good this was due to the way the links were done as the photos were all external links and therefore out of my control. I feel the site is working as well as it can, and it does not have any speed issues, as the code is very clean with no really links to unnecessary site.
<img src="/static/images/lighhouse_review_of_site.png">;

## Returning Visitor Goals
### A returning visitor would need to be able to see the adds quickly and be able to view them easily.

## Frequent User Goals
### As a Frequent User, I decided that they would need access to see if their items were still valid and to review the add to be sure it was correct.

## Further Testing

### I have run through the site’s operation one last time to make sure that it adds adverts and deletes them from the MongoDB site as it should, looking at the site on differing screaan sizes from Google Chrome the menus all work fine and the site looks good.

# Known Bugs 

## The contact details and company information needs to be created, I ran out of time due to spending all my time on the data base interactions and getting the site to function correctly.
## As the site is not a real one most of the information in the footer is made up and some of it does not have any links. This information could be added later if needed, but I have simply run out of time to even consider them.
## Users are not able to sort the classified adds by type, this I would like to have added but due to the time constraints I could not do this.
## Users with accounts could have emails sent to them regarding items for sale and then new item that might be of interest to them, this is currently above my knowledge and possibly outside of the scope of this project, but the site could be made to be me more useful to people searching for classics for sale.
## he user interface could be tidied up to look much smarter, adding more photos and showing the adds differently but once again due to my slackness and having time constraints I have been unable to do this. Maybe the next oroject will be much better, if I am able to continue, which I hope I am.

# Deployment

## Initial Development
### After running out of free time in Gitpod, I decided to not go over my 100hr a month limit that I would try to develop the site off line and on my hard drive, using Geany to edit the code. This proved very useful, once the code was working I uploaded it to GitPod and did the normal; git add ., git commit, and git push commands to save the work.
## GitHub Pages
### The project was deployed to GitHub Pages.
## Deployment On GitHub from GitPod
### The first step was to create a template, which as this was a copy of the last site I created I simply copied the last site.
### The next step was to start gitpod from github.
### Once I had the site on gite hub I was able to copy the files from the old site to the new site.
### Once the design and development work was done, I did a final "git add -A", then a "git commit -M "" (not forgetting to add the message that made sense to me and hopfully to others at a later date), and then the "git push" the site was then loaded onto github.
### Once on github and after leaving it guthub took sometime to update, I checked the files to makesure they were correct.
### Then a link to the deployed site was made from the "Settings" menu in github. As per other projects.
### This link was then given to the "code institute" to assess.
## Deployment of MongoDb
### Connecting MongoDB to GitPod, click on the Connections tab. 
<img src="/static/images/connect_clusters.png">;
### The select the “Connect you application” option. 
<img src="/static/images/connect_tocluster.png">;
### Click on the copy button to copy the link.
<img src="/static/images/copy_cluster.png">;
### Add this link to the env.py file, paste the link in MONGO_URI section, making sure to add both the collection name and the password. In the correct places, it is imperative that the whole word is replaced, :<password> must be replaced with your password to enter MongoDB, and <dbname> replaced with the collection name you want to connect to.
<img src="/static/images/envfile.png">;
### Once ManogDB and GitHub/GitPod are connected and the site has some content you can test the interaction between the two sites and make sure it works correctly.
## Deployment of Heroku
### Enter the correct Config Variables into Heroku, ensuring that the MONGO_URI was correct and matched the information contained in the env.py to ensure that both site are able to communicate correctly.
<img src="/static/images/definevariablesheroku.png">;
### Next enter the deployment section, and locate the correct GitHub and make sure that they are connected in Heroku.
<img src="/static/images/connectherokutogithub.png">;
### The site was building but did not display, after reviewing the requirements.txt file I found that I had some requirements missing, once I did a freeze of the requirements.txt file the project was viewable on Heroku.
## Deployment locally on to my Window 10 PC
### First step to download python I did this. Running my project on my local version of python did not go well, due to the time constraints I have elected not to do this, and to get this working outside of this project as I need this to do the projects I need to work on personally. I installed flask and werzeug but still seem to have issues, I will get this working.
 

# Credits
## Code
### I did not use a full-screen hero image in this version of my project just a small made up image found from a Google search.
### I found code for the project from the mini project, which has been invaluable to helping me understand the logic and to getting my site to perform in a similar way to the mini project, with some subtle differences. I have tried to show the code used, and the ideas taken from the mini project, I have many ideas that could be used to improve the site, but I feel they are way above my level and possibly will be part of the next part of the course. This is what has happened on the other mile stone projects.
### I also used the tutors from the code institute to help with some problems and was able to talk with Tim Henderson the guy that gave the mini project lessons, this was very helpful.

## Materialize
## I used the Materialize Library throughout the project mainly to make site responsive using the Materialize Grid System.
## Materialize has been invaluable in making a responsive and useable website.

# Content
## Most of the content is generated from the MongoDB, but it has been formatted to fit into the site and be displayed correctly.

# Media
## All Images were created using MS Paint to edit them to create the collage of pictures. They initially all came from a Google search and then were copied and pasted into the collage of images.
## The other images were had urls to the image and were found using Google.
# Acknowledgements
## My Mentor for continuous helpful feedback. I was able to learn so much from our short meetings, they have been invaluable to me. My mentor was able to help me think differently and to use different tools and code that were able to help me with the project. Without his help I would still be pulling my hair out, I cannot thank him enough. I only hope I have not let him down with my readme file.
## Tim Nielson for help and making the mini project, the mini project was invaluable to getting my project working correctly, and helping me understand some of what I was doing.
## Tutor support at Code Institute for their support, while I have not used them for any of my projects until now, when I contacted them regarding this project they were very helpful. And after some hard work on their part able to understand my thinking and help solve the problem. So thank you for for your understanding and help.
## Code institute for putting this course together, each project has helped me grow and given me a better understanding of what I have learnt so far. I don’t really ever want the journey to stop, so if I can proceed to the final segment it will be great, BUT, also I feel I will need to continue on some more courses.....



