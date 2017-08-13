import sqlite3

#connect to the database file
database_file = "birb_db.sqlite"
connection = sqlite3.connect(database_file)
curse = connection.cursor()

#setting up variables to create the table containing "players" scores
#scores_table = "scores"
#scores_player = "player"
#string_type = "TEXT"
#scores_score = "score"
#int_type = "INTEGER"
#
#params = scores_table, scores_player, string_type, scores_score, int_type
#
##create table to contain the scores
#curse.execute("CREATE TABLE ? (? ?, ? ?)", params)

curse.execute("CREATE TABLE scores (player TEXT, score INTEGER)")
