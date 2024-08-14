# Welcome to Book Tracker!

## A Book Tracking Website
![Capture](https://github.com/user-attachments/assets/be3d00d4-e4d7-49e8-9465-dfde7a421b6b)

> Book Tracker is a website that allows the users to add, update and edit books they are reading, or plan on reading.

### [Link to the deployed site](https://book-tracker-lo-007f2790e66f.herokuapp.com/)

#### - By Leander Ots

---

## Table of contents 

 1. [ Data Structure Planning ](#data_planning)
 2. [ User Experience Design Planning ](#design_planning)
 3. [ Agile Development ](#agile-development)
 4. [ Features implemented ](#features-implemented)  
 5. [ Features Left to Implement ](#features-left-to-implement)  
 6. [ Technology used ](#technology-used) 
 7. [ Testing ](#testing)  
 8. [ Bugs ](#known-bugs)  
 9. [ Deployment](#deployment)
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---
# Data Structure Planning

This site uses three models:

- User model: This is Django's default user model, and is used for to signup for an account, and all the actions that go with managing a book list
- Book model: This represents the actual books in the database. Within the current website they are added by an admin. The user cannot add new books to the site's database
- UserBook model: This tracks the relationship between users and the books in the database. The user can pick a book from the database, and add it to their own library

![Capture1](https://github.com/user-attachments/assets/e7d3d5a0-e5fd-4452-ab89-78d2e33764d5)

- The above served as a MVP guide (created with dbdiagram) for how the data should interact. Ultimately not all of these fields were as useful (e.g. description). This is a MVP structure as initially i wanted to pull my books from an API. However the decision was made to first focus on a functioning site, before trying to put together more complex features

# Design Planning

![Capture2](https://github.com/user-attachments/assets/6bb9ef93-3c64-4854-87ae-2822615bca7a)

![Capture3](https://github.com/user-attachments/assets/b75bf812-526e-4167-9f6a-b0618680f082)

Initially there was just a need for a home page and a my library page. However since i did not use an API, a page that displays all books available on the site was added, so that users can get a short summary of what each book is about. The main page is however the 'My Library' page, where users can add, update or delete entries to their personal reading list.

For mobile devices a hamburger icon replaced the clickable navbar items, as well as get rid of certain items that might take up space, like the image on the homepage. The worry was however how the table in the library would look in small devices. Ultimately i went for a scrollable table.

The purpose of the site was to be as clear as possible, and include as much easy functionality, such as e.g. the logo bringing the user back to the homepage. I also wanted to build something that, if i wanted to, I could expand on later with extra functionality.

---

# Agile Development

## Overview

![capture4](https://github.com/user-attachments/assets/5935aef0-640f-481c-ad64-a6703f98e592)

I used the GitHub projects page for my user stories. I started using the project page after my initial deployment. The main purpose was to go over features that needed to be added to ensure a MVP. Over time I would add issues that might pop up, or ideas I had that would imporve functionality.

### [Link to project board](https://github.com/users/L09224/projects/3/views/1)

## MoSCoW Prioritisation

- Must have: Full CRUD for book updates, user registration and login/log out functionality, ability for users to view and explore books, data security
- Should have: responsive design, error messages for if things don't work, clear messages for when a book entry is updated
- Could Have: sort and filter books, different home page message depending on if a user is logged in, logo & favicon, hero images
- Won't have: footer links for privacy policy and contact info, connection to API for importing books

---

# Features Implemented

- Home page with login and sign up features
- Full CRUD functionality on managing books in a user's library
- Responsive design: the site has been tested for responsive design on widths of 320px, 480px, 768px, 1024px and 1280px
- Easy to navigate the book list on both the 'books' page and 'my library' page due to the ability to sort alphabetically, by page number or author
- Consistent styling accross all pages. The user will not see any link or redirect to an admin template
- CSRF protection
- Clear messaging for when a user adds, updates or deletes entries on their book list, as well as error messages if something goes wrong
- Clear messaging for when a user is logged in on the homepage

![Capture5](https://github.com/user-attachments/assets/5f9c11ae-112c-43e5-9caf-c86bce9c61df)
![Capture6](https://github.com/user-attachments/assets/a2dc16c7-7519-4e06-be7f-41f78c5168c6)
![capture7](https://github.com/user-attachments/assets/c7521dfb-6f9a-40c8-bfae-e77ff690a07a)


---

# Features left to implement 

All MVP features were implemented, however if more time was available for the project, I would implement either:

1. An API that populates the site book list
2. A form that allows users to recommend books to be added to the book list, with admin approval

---

# Technology used
- balsamiq - to create the wireframes
- dbdiagram.io - To create my ERDs
- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for ensuring that updating a book to 'completed' also changes to read pages to 100%
- Django - framework used to build this project
- PostgreSQL - for the database
- GitHub - for storing the code and for the project board
- Heroku - for hosting and deployment of this project
- Cloudinary - hosting the static files
- Coolors - for creating a palette for the site
- Favicon.io - for generating my favicon templates from my logo
- design.com - for letting me generate a logo for the site
- chatGPT - for troubleshooting when no google-fu solves an issue

---

# Testing

- Testing for responsiveness was done in Firefox via the Accessibility Properties. Responsiveness was tested at different resolutions to ensure no breaks in the site at common resolutions.
- HTML code validated with w3 validator
- CSS code was validated with Jigsaw and received CSS level 3 + SVG
- Python code checked with Pep8
- JS code passed through JSLint


---

# Deployment

- Repo created in Github, updated in Gitpod
- Deployed on Heroku
- Connected Secret Keys to config vars
- Connected Code Institute PostGres Database
- Connected cloudinary static file host

---

Credits and Thank yous

- Thank you to Lewis Dillon for all the help, as well as David Calikes for being there for any issues that popped up. Also a big thank you yo our CI cohort, who have been a wonderful group always ready to help classmates
- Django Documentation
- we3schools
- Code Institute - Love Running, I think before I blog



