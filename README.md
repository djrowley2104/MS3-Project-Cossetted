# Cosseted Classics
## I have designed this to give the Classic owner the ability to showcase and sell their baby
## The site could be further developed to show clips of the classics running, giving a walk around the classic. 
## 
##

# Site Goals
## The site is designed to allow users to easily search for classics for sale, and then for the logged in user to find classics for sale and to be allowed to buy and sell classics.
## The users are only able to see approved items in the list. This happens once the administrator has approved the advert, only the administrator has the ability to approve adverts and delete them. Each user has a different profile and sees only the menus applicable to their group.

# UX / User Experience

## First Time Visitor Goals
### As a First Time Visitor, I want them to be able to, login and create an account easily.
### Once logged in they need to be able to find classics for sale, well after logging in they are directed to this page. 

## Returning Visitor Goals
### As a Returning Visitor, I want them to be able to find what the want and to be able to sell and buy items quickly and easily.


# Design / Features

## The site has been designed allow users to only see approved adverts for classics. The adverts are approved by the admin account holder.
## New sales types can be reviewed and added by the Admin, they can also be deleted if they are no longer needed.
## 

## Colour Scheme
### I decided to use a light blue background, no idea why it seems to be calming and relaxed maybe it represents a clear blue sky on a nice day.
Typography
### 
## Imagery
### Imagery is important. The images used where all taken from Google searchs and then adapted to my requirement using MS Paint.
## Home Page Wireframe - View
### Below you can see the desktop wireframe;
<img src="/assets/figures/Desktop.png">;
## Mobile Wireframe - View
### Below you can see the mobile device wire frame;
<img src="/assets/figures/Mobile.png">;
## Contact Us Page Wireframe - View
### Below you can see the contact page wire frame;
<img src="/assets/figures/Contactpage.png">;
# Features
## Responsive on all device sizes
### After speaking to my mentor I used software called Responsinator to check that the site was able to adapt to many different devices.

# Interactive elements

## Technologies Used
### Languages Used
#### HTML5
#### JavaScript
#### CSS3
## Frameworks, Libraries & Programs Used
### Bootstrap 4.4.1:
#### Bootstrap was used to assist with the responsiveness and styling of the website.
### Font Awesome:
#### Font Awesome was not used as the one icon I wanted did not display correctly so I made my own.
### jQuery:
#### jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
## Git
### Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
## GitHub:
### GitHub is used to store the projects code after being pushed from Gitpod.
## Photoshop:
### Photoshop was used to create the logo, resizing images and editing photos for the website.
## Balsamiq:
### Balsamiq was used to create the wireframes during the design process.

# Testing
## I have started to create the base of the website, at the moment I’m having an issue getting the site to work correctly when in mobile mode, the hamburger is displayed, but when you click on it the dropdown menu is not displayed, therefore the js file does not load and work correctly. After lots of work I found the correct way to get the Mongo Data Base talking to my GitPod project and then deployed on Heroku, still having issue with Heroku.
## Working on GitPod template hoping to get the sign in sorted.
## Getting the website to right to the MongoDB, I needed to used the correct logic and re-listen to the tutorials in order to get the logic sorted. Once I got the correct logic, it was easy.
## Adding sell item and sell classic to the app.py file and getting them to right to the data base I needed to re-listen to the tutorials again.
## Edit Sales item, the field should be populated from the MongoDB, this is not happening, after talking with the tutors, I was able to solve this error, code amended and now it works.
## The edit button throws an error, the error is “an unexpected argument”, this was dues to an error in the app.py. Once I reverted back to the pre error version of the app.py file I was able to see what had gone wrong and fix it.
## after talking with my mentor I decided to simplify my site as I had too many categories in it, and it made fault finding very tricky as it felt like I was chasing my tail.
## I have added a view sales categories very similarly to the add tasks section in the mini project.




### 

### I also used the Responsinator website to test that my site worked for differing screen sizes, once I had the working well in Google Chrome, this test was really to be sure.
### 

## Returning Visitor Goals
### 
.

## Frequent User Goals
### As a Frequent User, I decided that they would need access to repair sites and places to ride, these will be added and the site will grow as the users add their favourite places that they want to share with other people.

## Further Testing

### 
.

# Known Bugs 

### 
 
# Deployment

## Initial Development
### After running out of free time in Gitpod, I decided to not go over my 100hr a month limit that I would try to develop the site off line and on my hard drive, using Geany to edit the code. This proved very useful, once the code was working I uploaded it to GitPod and did the normal; git add ., git commit, and git push commands to save the work.
## GitHub Pages
### The project was deployed to GitHub Pages.
## Deployment On GitHub from GitPod
### The first step was to create a template, which as this was a copy of the last site I created I simply copied the last site.
### The next step was to start git pod from github.
### Once I had the site on gite hub I was able to copy the files from the old site to the new site.
### Once the design and development work was done, I did a final "git add .", then a "git commit -M "", and then the "git push" the site was then loaded onto github.
### Once on github and after leaving it guthub sometime to update, I checked the files to makesure they were correct.
### Then a link to the deployed site was made from the "Settings" menu in github.
### This link was then given to the "code institute" to assess.
## Deployment of MongoDb
### Connecting MongoDB to GitPod, click on the Connections tab. <img src="/static/images/connect_clusters.png">;
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




# Credits
## Code
### I did not use a full-screen hero image in this version of my project just a small made up image found from a Google search.

### Materialize: i used the Materialize Library throughout the project mainly to make site responsive using the Materialize Grid System.
### Materialize has been invaluable in making a responsive and useable website.
## I found code for the project from the mini project, which has been invaluable to helping me understand the logic and to getting my site to perform in a similar way to the mini project, with some subtle differences.
## I also used the tutors from the code institute to help with some problems and was able to talk with Tim Henderson the guy that gave the mini project lessons, this was very helpful..

# Content
## 
.
##.
## 

# Media
## All Images were created using MS Paint to edit them to create the collage of pictures. They initially all came from a Google search and then were copied and pasted into the collage of images.
## The other images were had urls to the image and were found using Google.





# Acknowledgements
## My Mentor for continuous helpful feedback. I was able to learn so much from our short meetings, they have been invaluable to me. My mentor was able to help me think differently and to use different tools and code that were able to help with the project.
.

## Tutor support at Code Institute for their support, while I have not used them for any of my projects, when I have contacted them regarding other issues they have been very helpful.



