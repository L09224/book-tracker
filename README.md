# Welcome to Book Tracker!

## A Book Tracking Website
![Capture](https://github.com/user-attachments/assets/be3d00d4-e4d7-49e8-9465-dfde7a421b6b)

> Book Tracker is a website that allows the users to add, update and edit books they are reading, or plan on reading.

### [Link to the deployed site](https://book-tracker-lo-007f2790e66f.herokuapp.com/)

#### - By Leander Ots

---

## Table of contents 

 1. [ Planning ](#planning)
 2. [ UX ](#ux)
 3. [ Agile Development ](#agile-development)
 4. [ Features implemented ](#features-implemented)  
 5. [ Features Left to Implement ](#features-left-to-implement)  
 6. [ Technology used ](#technology-used) 
 7. [ Testing ](#testing)  
 8. [ Bugs ](#known-bugs)  
 9. [ Deployment](#deployment)
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)

---
# Planning

### Data Structure

This site uses three models:

- User model: This is Django's default user model, and is used for to signup for an account, and all the actions that go with managing a book list
- Book model: This represents the actual books in the database. Within the current website they are added by an admin. The user cannot add new books to the site's database
- UserBook model: This tracks the relationship between users and the books in the database. The user can pick a book from the database, and add it to their own library

![Capture1](https://github.com/user-attachments/assets/e7d3d5a0-e5fd-4452-ab89-78d2e33764d5)

- The above served as a MVP guide (created with dbdiagram) for how the data should interact. Ultimately not all of these fields were as useful (e.g. description). This is a MVP structure as initially i wanted to pull my books from an API. However the decision was made to first focus on a functioning site, before trying to put together more complex features

### Design
![Capture2](https://github.com/user-attachments/assets/6bb9ef93-3c64-4854-87ae-2822615bca7a)

![Capture3](https://github.com/user-attachments/assets/b75bf812-526e-4167-9f6a-b0618680f082)




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
- 
- 





