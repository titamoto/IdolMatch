# IdolMatch 💗
IdolMatch is a CLI app tests matches you with a BTS member based on your personality type.

**Disclaimer:** This app is intended for entertainment purposes only.  
It does not guarantee the formation of happy relationships with BTS members or any other K-pop angelic geniuses.  
The test's accuracy is **not** scientifically validated.   

## How to Install 
To install this app follow the steps below.

1. clone the repo by typing this command in your terminal:

```bash
$git clone https://github.com/titamoto/IdolMatch.git
```

or if you want to clone using SSH:

```bash
$git clone git@github.com:titamoto/IdolMatch.git
```

2. go into the directory inside the directory created by cloning this repo:

```bash
$ cd IdolMatch/
```

3. install dependencies and launch virtual environment:

```bash
$ pipenv install && pipenv shell
```

4. run `seeds.py` file to seed the database:

```bash
$ python lib/seeds.py
```

5. start the app by running `cli.py` file:

```bash
$ python lib/cli.py
```
Note: if `python filename.py` command doesn't work for you to run .py files, try `python3 filename.py` instead.

## How to Use
Follow the instructions in the terminal. Basic walkthrough:
1. login with email whether you are a new user or have been already registered
2. see your previous result (for returning users) or start the test
3. answer the questions one by one by typing number from 1 to 5 into the terminal
4. see your result as your personality type and BTS members matching with you (if any)
5. redo the test until you match with your favorite idol
6. quit the app and think over your life choices

## Credits
The app uses following Python packages:    
 - [SQLAlchemy](https://www.sqlalchemy.org) for the database management.    
 - [Faker](https://faker.readthedocs.io/en/master/) for creating mock data.  
 - [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/) for building command line interface features. 
  
The personality type assessment is based on Open Extended Jungian Type Scales 1.2 developed by [Eric Jorgenson](https://openpsychometrics.org/). 

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
