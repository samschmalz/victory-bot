import sqlite3

#connect to the database file
database_file = "birb_db.sqlite"
connection = sqlite3.connect(database_file)
curse = connection.cursor()

#setting up variables to create the table containing "players" scores
scores_table = "scores"
scores_player = "player"
string_type = "TEXT"
scores_score = "score"
int_type = "INTEGER"

#create table to contain the scores
curse.execute("CREATE TABLE {p0} ('{p1}' {p2}, '{p3}' {p4})".format(p0=scores_table, p1=scores_player, p2=string_type, p3=scores_score, p4=int_type))
