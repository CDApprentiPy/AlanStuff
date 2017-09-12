# Week 2 - Monday

## Daily Schedule
9  am - Algorithms
10 am - Lecture: ERD
11 am - Group Work
12 pm - Luncheon
1  pm - Lecture: MySQL + MySQL Workbench
    - Lecture
        - MySQL, Workbench, and MAMP
    - Group Activity:
        - Install MySQL and MAMP successfully
2  pm - Open
3  pm - Open
4  pm - Demo
5  pm - EOD Check In

### Lectures
-AM - ERDs
    - Context: Persisting Data
        - Database!
    - Diagrams
        - Help us organize our data
    - Relationships
        - 1:1
        - 1:X
        - X:X
    - Data Types:
        - VARCHAR
            - stores nonnumeric data up to 255 in length
                - adjusts to use appr
                opriate amount of room
            - Use text for big varchars
        - CHAR
            - stores characters in a fixed size bucket
        - INT
            - big/tiny/float
        - DATETIME
    - Normalizations:
        - Try to not repeat data!
        - Columns hold 1 piece of data
        - Columns should have unique values unless PK or FK
        - Cannot have a non-key column dependant on another non-key column
    - Conventions:
        - table names
            - lowercase and plural
        - PK 
            - id
        - FK
            - singular_table_name_id
        - cr@ and up@ EVERYTIME!

-PM - MySQL + MAMP + MySQLWorkbench
    - What is SQL?
        - a query language 
    - How do MAMP, MySQL, and Workbench fit together?
    - Install MySQL and stuff