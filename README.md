# my_debtors TeamLorispp58

A platform that allows schools in a certain locality list directory of people owing them - to help them avoid going to other schools.

## Features Requirements

**Unauthenticated Users**

- Visit the platform to view basic information about it
- View and Interact with the documentation
- Register to view more details
- No access to data

**Authenticated Users**

- Full access to the platform
- Verify details before full access to platform
- Post new data about a debtor
- Allow debtors to challenge - contend
- Comment on post by others
- Copy should be disabled

## Tech Stack

**Design:**
<img src="https://img.shields.io/badge/FIGMA-orange?style=for-the-badge&logo=figma&logoColor=white" alt="FIGMA Badge"/>

**Client:**
<img src="https://img.shields.io/badge/HTML5-darkorange?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 Badge"/>
<img src="https://img.shields.io/badge/CSS3-blue?style=for-the-badge&logo=css3in&logoColor=white" alt="CSS3 Badge"/>
<img src="https://img.shields.io/badge/JAVASCRIPT-grey?style=for-the-badge&logo=javascript&logoColor=white" alt="Javascript Badge"/>

**Server:**
<img src="https://img.shields.io/badge/PYTHON-skyblue?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
<img src="https://img.shields.io/badge/DJANGO-darkgreen?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>

**Database:**
<img src="https://img.shields.io/badge/MYSQL-blue?style=for-the-badge&logo=mysql&logoColor=white" alt="Mysql Badge"/>

**Project Management and Version Control:**

<img src="https://img.shields.io/badge/GITHUB-black?style=for-the-badge&logo=github&logoColor=white" alt="github Badge"/>

## Documentation

- [Project Documentation](https://docs.google.com/document/d/1_GdAB9qmQZCOtyvn2LBKBQkuh2_1t4vgkf1nh8Ej-I8/edit?usp=sharing)
- [Figma Link](https://www.figma.com/file/8b4Bfra3koQwecQYQg8jMv/My-Debtors-WiFi?node-id=79%3A37&t=SseGuCzteGGu7DYg-1)
- [Data Schema](https://docs.google.com/document/d/1jrnUNzCB5b0qH2yzSGrk7mR_qb9eqgFwDNTodXJRlOc/edit?usp=sharing)

## Project Team Members

- [@Niqabigeek](https://www.github.com/niqabigeek)
- [@Anitanwosu](https://www.github.com/anitanwosu)
- [@victoryidahor2020](https://www.github.com/victoryidahor2020)
- [@Santibenson](https://www.github.com/Santibenson)
- [@cutespot3200](https://www.github.com/cutespot3200)
- [@TheGreatWizard16](https://www.github.com/TheGreatWizard16)
- [@Ibukundev](https://www.github.com/Ibukundev)
- [@Ba-Mobolanle](https://www.github.com/Ba-Mobolanle)
- [@MahdiyaOyiza](https://www.github.com/MahdiyaOyiza)
- [@Hamsen22](https://www.github.com/octokatherine)
- [@Jhaniee](https://www.github.com/Jhaniee)
- [@henryhife](https://www.github.com/henryhife)
- [@Add Name](https://www.github.com/octokatherine)
- [@pizzii](https://www.github.com/pizzii)

## Run Locally

Clone the project

```
git clone https://github.com/zuri-training/TeamLorispp58.git
```

Go to the project directory

```
cd TeamLorispp58.git
```

Create a Virtual Environment

```
python -m venv env
```

Activate Virtual Environment

```
env\scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```


Create .env file in SDM project level containing SECRET_KEY='' 


Migrate Database 

```
python manage.py migrate
```
Create Super User 
```
python manage.py createsuperuser
```
Finally, Start The Server.
```
python manage.py runserver
```

## How to Contribute
  1. Create a new branch to make your changes:<br/>
  
     `git checkout -b <your-name/task>`<br/> 
     
      and make the required changes.<br/>
  
  2. Stage the file: <br/>
  
     `git add <your-changed-file>`<br/>
  
  3. Make sure your commit message is detailed with what you changed and where you changed it and commit your file: <br/>
  
    `git commit -m <your-message>`
    
  4. Push your local changes: <br/>
  
     `git push origin <your-branch-name>` <br/>
  
     If an error occurs here, it means that someone has made changes to the original file while you were working. <br/>
    
     Simply run:<br/>
     
     `git pull origin main`  to sync your local file with the current main file<br/>
     
     run `git push origin <your-branch-name>` again.
    
  5. Visit the remote url on Github to create a pull request.
  
  6. Wait for a team member to review your pull request.
  
  7. Merge pull request after review.


## Acknowledgements 🚀 

<p>
  <img src="https://res.cloudinary.com/zuri-team/image/upload/zuriboard/tenant-logo/wmqxdxt4skv05wsvc21o.png"
       alt="Zuri Logo"
  >
</p>
