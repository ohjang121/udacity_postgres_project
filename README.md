# Project 1: Data Modeling with Postgres

Objective: Build an ETL pipeline for a music app (Sparkify) using Python & Postgres. Two datasets used are both in JSON format, and key parts are extracted from the datasets to build a star schema optimized for queries on song play analysis.

## Schema & Table Design

The database name is `sparkifydb`. The project's star schema contains 1 fact table and 4 dimension tables - create, insert, and drop SQL logic defined in `sql_queries.py`:

### Fact Table(s)

1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
    - columns: *songplay_id (pkey), start_time (foreign key to **time**), user_id (foreign key to **users**), level, song_id (foreign key to **songs**), artist_id (foreign key to **artists**), session_id, location, user_agent*
    
### Dimension Table(s)

1. **users** - users in the app
    - columns: *user_id (pkey), first_name, last_name, gender, level*
2. **songs** - songs in music database
    - columns: *song_id (pkey), title, artist_id, year, duration*
3. **artists** - artists in music database
    - columns: *artist_id (pkey), name, location, latitude, longitude*
4. **time** - timestamps of records in **songplays** broken down into specific units
    - columns: *start_time (pkey), hour, day, week, month, year, weekday*
    
`create_tables.py` creates and connects to the `sparkify` database to build the shell tables so that data can be loaded into the tables.

## ETL Process

`etl.ipynb` contains the step-by-step guidance to build the ETL Process for `sparkifydb`, which gets formalized in `etl.py` for execution. The two datasets populate the following tables:

* `data/song_data`: songs, artists
* `data/log_data` time, users
* combined: songplays

Note that all data in `data/song_data` only have 1 row per file, so the logic only has to load the first index (values[0]) per file iteration. Each file in `data/log_data` contains several lines, hence iteration per file is required to load all data into the tables.

## Steps to run the scripts

1. The Project Workplace already has necessary libraries installed, but for a brand new environment, it is required to install all libraries that are not built-in (e.g. psycopg2).
2. Run `create_tables.py` to create shell tables: 
```
python create_tables.py
```
3. Run `etl.py` to perform the ETL Process
```
python etl.py
```

## Example Queries

* How many distinct users are Male?

`select count(distinct user_id) from users where gender = 'M'`

* List mobile user_agents

`select user_agent from songplays where user_agent ilike '%mobile%' group by 1`


