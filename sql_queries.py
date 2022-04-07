# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, -- autoincrement surrogate key, not in the log file
                                      start_time TIMESTAMP NOT NULL, -- log.ts
                                      user_id INT NOT NULL, -- log.userId
                                      level VARCHAR, -- log.level
                                      song_id VARCHAR, -- song.song_id
                                      artist_id VARCHAR, -- song.artist_id
                                      session_id INT, -- log.sessionId
                                      location VARCHAR, -- log.location
                                      user_agent VARCHAR -- log.userAgent
                                      );
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id INT PRIMARY KEY, -- log.userId 
                                  first_name VARCHAR, -- log.firstName
                                  last_name VARCHAR, -- log.lastName
                                  gender VARCHAR, -- log.gender
                                  level VARCHAR -- log.level
                                  );
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR PRIMARY KEY, -- song.song_id
                                  title VARCHAR NOT NULL, -- song.title, log.song
                                  artist_id VARCHAR, -- song.artist_id
                                  year INT, -- song.year
                                  duration FLOAT NOT NULL -- song.duration, log.length (maybe)
                                  );
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY, -- song.artist_id
                                    name VARCHAR NOT NULL, -- song.artist_name
                                    location VARCHAR, -- song.artist_location
                                    latitude FLOAT, -- song.artist_latitude
                                    longitude FLOAT -- song.artist_longitude
                                    );
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP PRIMARY KEY, -- log.ts
                                 hour INT, 
                                 day INT,
                                 week INT,
                                 month INT,
                                 year INT,
                                 weekday INT
                                 );
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, 
                       start_time,
                       user_id,
                       level,
                       song_id,
                       artist_id, 
                       session_id, 
                       location, 
                       user_agent)
VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
INSERT INTO users (user_id, 
                   first_name, 
                   last_name, 
                   gender, 
                   level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
INSERT INTO songs (song_id,
                   title, 
                   artist_id, 
                   year, 
                   duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, 
                     name, 
                     location, 
                     latitude, 
                     longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
INSERT INTO time (start_time, 
                  hour, 
                  day, 
                  week, 
                  month, 
                  year, 
                  weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id,
a.artist_id
FROM songs s
JOIN artists a on s.artist_id = a.artist_id
WHERE s.title = %s
AND a.name = %s
AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
