Tuesday:
    - Algorithms
        - Topic: Queues
    - AM Lecture
        - Topic: ORMS!
        - Group Activity: 
    - PM Lecture
        - Topic: 
        - Group Activity:
    - EOD:

## Lectures
-AM: ORMS!
    - "Vietnam of CS"
        - http://blogs.tedneward.com/post/the-vietnam-of-computer-science/
    - OOP! 
        - What is it?
            - exists to convert incompatible datas using OOP-y concepts
        - Advantages of treating DB/tabls as objects?
            - Easy column:field translation (Imagein doing an insert across like 50 columns?)
            - DATETIME is ~easier/convenienter
            - 1:X realtionships look nice
            - Can reduce DB queries (tradeoff between handling less effective query and number of queries)
            - Can abstract your data queries to be friendly to muliplt dbs
        - Cons of stuff
        
            - State management
            - X:X lol!
            - Limited to using ORM verbage -> Creates some inefficient queries
                - Queries must be abstracted
            - Relying on ORM can lead to poorly constructed dbs to easily be ORM-friendly
            - Complexity leads to poor/ineffective use
            - object-relational impedence mismatch https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch
        - Which is better?
            - Legit "It Depends"
                - will see Dapper in C# that is ORM that uses raw SQL
    - Models in MTV
        - So, OOP boilerplate/ORM life in Django suggests that we should use an ORM because (XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX), where does this fit in in the MTV concept?
        - Models are supposed to represent the objects that help us interact with our DB
        - 2 components
            - Model and ModelManager
        - Models things
            - https://docs.djangoproject.com/en/1.11/topics/db/models/
            - django knows whats up, so it will do some sneaky stuff
                - automatically gives you an id field
            - relationships
                - 1:1
                    - OneToOneField on dependant model
                - 1:X
                    - put a foreign key field in the dependant model
                        - manufacturer = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
                - X:X
                    - put a manytomany field in ONE of the models
                        - toppings = models.ManyToManyField(pizza)
                    - This is great for when the joining table doesn't needanythign else
                    - If you 
        - MM things
            - API for connecting with db
            - default name is objects
            - available throught the CLASS not the INSTANCE
            - CRUD
                - C
                    - create() & save()
                    - add() in 1:many
                - R
                    - .all()/.get() & .filter()/.exclude()
                    - JOINS
                        - use __ to spane a table
                        - Blog.objects.filter(entry__authors__name='Lennon')
                    - 1:X
                        - _set to see the manys on the other end of a relationship
                    - Q objects for trickier queries
                - U
                    - save()
                - D
                    - delete()
        - Can also raw SQL
            - https://docs.djangoproject.com/en/1.11/topics/db/sql/