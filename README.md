# IC Holding Job Application Tasks

## Information

The project created to accomplish the job application of the "IC Holding".

## Q1 - API Implementation, Query Optimization and Improvement

LocationRecord

- id PK
- people FK
- datetime DateTimeField
- latitude FloatField
- longitude FloatField

Peoples

- id PK
- first_name CharField
- last_name CharField

Using the models above, we want you to create a function that returns the list of last points per person that have sent location data in the last 12 hours. In this function, please implement the necessary queries using the Django ORM Framework. This function will return the list that consists of last point objects like the example below. Note that, because the LocationRecord model takes too many queries, every query to this model is very costly in terms of performance. You must use Python as a programming language, Django as a web framework, and you can use any database management system.

We also want you to suggest a different method to get this data in a more efficient way. For example, you can suggest a tool, architecture, or model structure change.

For this task, you must deliver the aforementioned function and given models within a zip file to get the data in a more efficient way, if any. An explanatory document about your ideas or suggestions is more than welcome.

## Q2 - Architecture Optimization and Improvement

Person

- id PK
- first_name CharField
- last_name CharField

Task

- id PK
- title CharField
- description TextField

In this task, we want you to create a simple database model design. There are already two models named `Person` and `Task` as can be seen above.

Beforehand, tasks were assigned to only one person so that there were no task models; but from now on, tasks will be assigned to different people and we must store the frequency and last completion time of tasks by person. You must redesign these models and their fields to provide this ability. If you need to create new fields or new models, you can create them.

After the database model design, we want you to create a function that returns the list of frequency values for all Person-Task pairs.

For this task, you must deliver an entity-relationship diagram and a function to get the requested data.
