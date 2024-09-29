# [Trader's Diary] Built Using Django, AdminLTE.

## About Project
Trader's Diary is the trade tracking application for traders/investors. User can set 'Buy reason/ Sell reason' for each trade,
which will help later to analyse and improve their trading. The Dashboard display important stats to keep eye on the
performace. 

## Project Functionalities 
- Import feature to upload Zerodha tradebook csv file only
- Equity Curve vs Time
- Display of all trades either in grid/list format
- Search option and pagination
- Important stats such as Batting average, Win to Loss ratio, Average trade duration etc is shown on dashboard

## Technologies Used
- `Django` - For Coding Backend of Application.
- `SQLite` - Used this Default DataBase for Storing Data on temporary basis.
- `JavaScript` - For Integrating Additional functionalities in Project.
- `Bootstrap 5` - For UI Development of Project.
- `FontAwesome` - For embedding icons in Project.
- `HTML/CSS` - For Coding Basic Templates of Project.
- 'admin-lte 3.2.0' - For theme

## Usage

```BASH
git clone https://github.com/vishalsdk14/traders-diary.git
```

```BASH
python manage.py makemigrations trades
```

```BASH
python manage.py migrate
```

```BASH
python manage.py runserver
```

Copy http://127.0.0.1:8000/ in browser and run


## Note
- Currently only Zerodha tradebook csv file is supported.
- Before uploading tradebook csv, Portfolio settings needs to be set. 
