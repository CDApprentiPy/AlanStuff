# Week 2 - Tuesday

## Daily Schedule
9  am - Algorithms
10 am - Lecture: MySQL Queries
11 am - Group Work
12 pm - Luncheon
1  pm - Lecture: Connecting MySQL and Flask
2  pm - Open
3  pm - Open
4  pm - Demo
5  pm - EOD Check In

### Lectures
- AM: SQL Queries
    - Syntax
        - CRUD
            - Create
                - INSERT INTO <table> (col1 name, col2 name)
                  VALUES('col1 value', 'col2 value')
            - Read
                - SELECT <stuff> From <table>
                - WHERE things..
            - Update
                - UPDATE <table> SET col1_name = "newval1", col2_name="newval2" WHERE ...
                - if where is left out it will apply to all entries
            - Delete
                - DELETE FROM <table> WHERE ...
                - if where is left out it will apply to whole table
        - Joins
            - Left Join
                - Includes all entries from "left" table regardless if matched in other table
            - Join
                - Includes all entries in both tables
    - How To
        - Demo getting a file up and running
        - Make a Query
- PM: Connecting MySQL and Flask!
    - Overview:
        - What pieces do we need to have talk to eachother
        - What tools do we have to make that happen?
        - Here is some Python we did for you. It is okay if you don't get it, you'll realize its kinda hacky later
    - Build an imaginary connector class
        - what might we need to make a connection to a db?
            - where would this go in our class?
        - what might we want to be able to do?
            - would we want different behaviors for differetn kinds fo queries?