# Q1 - API Implementation, Query Optimization and Improvement

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

## Install & Dependence

Before running the project, make sure you have the python 3.11.9 installed as virtual environment.

1. As first step, install required packages by running the following command in the terminal:

  ``` bash
  pip install -r requirements.txt
  ```

2. Create the database by running the following command in the terminal:

  ``` bash
  python manage.py migrate
  ```

## Use

First of all, you need to populate the database with some data. You can do this by running the following command in the terminal:

``` bash
python manage.py populate_data <number_of_people> <number_of_years>
```

Example for creating 3 people and 10 years of location data per minute:

``` bash
python manage.py populate_data 3 10
```

It will take approximately 14-15 minutes to create the data for this example. You can change the number of people and the number of years as you wish. The output will be like this:

``` bash
Populating dummy 3 person and location data for 10 year(s) per person...
Populating data in bulk...
Populating (Max: 15768000): 15768000
First record time: 2024-08-20 18:42:32.745819+00:00
Last record time: 2014-08-23 18:43:32.745819+00:00
Successfully populated location data. Passed Time: 0:14:18.991196
```

After populating the database, you can run the following command to get the last location data of the people who have sent location data in the last 12 hours:

``` bash
python manage.py show_last_12_h <person_id> <day> <verbose>
```

Example usage 1:

``` bash
python manage.py show_last_12_h 1 0 1
```

This example fetches and displays location data for person ID 1 within the last 12 hours with verbose output. Example output:

``` bash
Fetching location data for person ID 1...
Finished fetching location data for person ID 1 in 1.543923 seconds.
Time between first and last record is 11:18:00
First record: 20.08.2024 18:42:32
Last record: 20.08.2024 07:24:32

All records:
[{'id': 1, 'latitude': -21.133479, 'longitude': -120.73569, 'datetime': '20.08.2024 18:42:32'}, {'id': 2, 'latitude': 48.852559, 'longitude': -53.964061, 'datetime': '20.08.2024 18:41:32'}, {'id': 3, 'latitude': 30.245824, 'longitude': 54.379938, 'datetime': '20.08.2024 18:40:32'}, {'id': 4, 'latitude': -3.861845, 'longitude': -46.452716, 'datetime': '20.08.2024 18:39:32'}, {'id': 5, 'latitude': -47.261218, 'longitude': 7.480152, 'datetime': '20.08.2024 18:38:32'}, {'id': 6, 'latitude': 40.33253, 'longitude': -78.673527, 'datetime': '20.08.2024 18:37:32'}, {'id': 7, 'latitude': -25.592615, 'longitude': 107.626256, 'datetime': '20.08.2024 18:36:32'}, {'id': 8, 'latitude': 30.571154, 'longitude': 88.358953, 'datetime': '20.08.2024 18:35:32'}, {'id': 9, 'latitude': 16.119348, 'longitude': 5.084667, 'datetime': '20.08.2024 18:34:32'}, {'id': 10, 'latitude': 35.375989, 'longitude': 173.171525, 'datetime': '20.08.2024 18:33:32'}, {'id': 11, 'latitude': 15.087112, 'longitude': 158.48689, 'datetime': '20.08.2024 18:32:32'}, {'id': 12, 'latitude': -86.479121, 'longitude': -78.30122, 'datetime': '20.08.2024 18:31:32'},
...
]
```

Example usage 2:

``` bash
python manage.py show_last_12_h 1 0 0
```

This example fetches and displays location data for person ID 1 within the last 24 hours without verbose output. Example output:

``` bash
[{'id': 1, 'latitude': -21.133479, 'longitude': -120.73569, 'datetime': '20.08.2024 18:42:32'}, {'id': 2, 'latitude': 48.852559, 'longitude': -53.964061, 'datetime': '20.08.2024 18:41:32'}, {'id': 3, 'latitude': 30.245824, 'longitude': 54.379938, 'datetime': '20.08.2024 18:40:32'}, {'id': 4, 'latitude': -3.861845, 'longitude': -46.452716, 'datetime': '20.08.2024 18:39:32'}, {'id': 5, 'latitude': -47.261218, 'longitude': 7.480152, 'datetime': '20.08.2024 18:38:32'}, {'id': 6, 'latitude': 40.33253, 'longitude': -78.673527, 'datetime': '20.08.2024 18:37:32'}, {'id': 7, 'latitude': -25.592615, 'longitude': 107.626256, 'datetime': '20.08.2024 18:36:32'}, {'id': 8, 'latitude': 30.571154, 'longitude': 88.358953, 'datetime': '20.08.2024 18:35:32'}, {'id': 9, 'latitude': 16.119348, 'longitude': 5.084667, 'datetime': '20.08.2024 18:34:32'}, {'id': 10, 'latitude': 35.375989, 'longitude': 173.171525, 'datetime': '20.08.2024 18:33:32'}, {'id': 11, 'latitude': 15.087112, 'longitude': 158.48689, 'datetime': '20.08.2024 18:32:32'}, {'id': 12, 'latitude': -86.479121, 'longitude': -78.30122, 'datetime': '20.08.2024 18:31:32'},
...
]
```

Example usage 3:

``` bash
python manage.py show_last_12_h 1 1 1
```

This example fetches and displays location data for person ID 1 before 1 day from now and within the last 12 hours with verbose output. Example output:

``` bash
Fetching location data for person ID 1...
Start time: 2024-08-19 19:42:47.996242+00:00, End time: 2024-08-19 07:42:47.996242+00:00 | Difference: 12:00:00
Finished fetching location data for person ID 1 in 1.600183 seconds.
Time between first and last record is 11:59:00
First record: 19.08.2024 19:42:32
Last record: 19.08.2024 07:43:32

All records:
[{'id': 1381, 'latitude': -47.812305, 'longitude': -86.581901, 'datetime': '19.08.2024 19:42:32'}, {'id': 1382, 'latitude': 1.693451, 'longitude': 81.015675, 'datetime': '19.08.2024 19:41:32'}, {'id': 1383, 'latitude': -7.697453, 'longitude': 11.710903, 'datetime': '19.08.2024 19:40:32'}, {'id': 1384, 'latitude': -88.584574, 'longitude': -125.489823, 'datetime': '19.08.2024 19:39:32'}, {'id': 1385, 'latitude': 38.835698, 'longitude': -146.199363, 'datetime': '19.08.2024 19:38:32'}, {'id': 1386, 'latitude': 37.610161, 'longitude': 19.516383, 'datetime': '19.08.2024 19:37:32'}, {'id': 1387, 'latitude': -68.934014, 'longitude': -138.857716, 'datetime': '19.08.2024 19:36:32'}, {'id': 1388, 'latitude': 72.050015, 'longitude': 102.207276, 'datetime': '19.08.2024 19:35:32'}, {'id': 1389, 'latitude': -16.805728, 'longitude': -72.883979, 'datetime': '19.08.2024 19:34:32'}, {'id': 1390, 'latitude': -81.343103, 'longitude': -167.303346, 'datetime': '19.08.2024 19:33:32'}, {'id': 1391, 'latitude': 79.401281, 'longitude': 165.364395, 'datetime': '19.08.2024 19:32:32'}, {'id': 1392, 'latitude': 19.706413, 'longitude': 66.382234, 'datetime': '19.08.2024 19:31:32'}, {'id': 1393, 'latitude': -10.566591, 'longitude': -151.278152, 'datetime': '19.08.2024 19:30:32'}, {'id': 1394, 'latitude': -30.035518, 'longitude': 176.809375, 'datetime': '19.08.2024 19:29:32'}, {'id': 1395, 'latitude': -70.795508, 'longitude': 174.597195, 'datetime': '19.08.2024 19:28:32'}, {'id': 1396, 'latitude': 44.508933, 'longitude': -144.445756, 'datetime': '19.08.2024 19:27:32'}, {'id': 1397, 'latitude': 87.853028, 'longitude': -93.460985, 'datetime': '19.08.2024 19:26:32'}, {'id': 1398, 'latitude': -89.471681, 'longitude': 127.83289, 'datetime': '19.08.2024 19:25:32'}, {'id': 1399, 'latitude': -85.184696, 'longitude': 124.910665, 'datetime': '19.08.2024 19:24:32'}, {'id': 1400, 'latitude': 4.141821, 'longitude': -86.331232, 'datetime': '19.08.2024 19:23:32'}, {'id': 1401, 'latitude': -55.062669, 'longitude': -45.347324, 'datetime': '19.08.2024 19:22:32'}, {'id': 1402, 'latitude': -16.594744, 'longitude': 92.427547, 'datetime': '19.08.2024 19:21:32'},
...
]
```

## Suggestions to Optimize the "Show Last 12 Hours Data" Query

The current implementation of the show_last_12_h command is not efficient because it queries the database for each person. To improve the performance, we can use the following method:

### 1. Creating a new table to store the last location data of each person

Creating a new table called "LastLocationRecord" to store the last location data of each person. This table will be updated every time a new location data is added to the LocationRecord table. This way, we can query the LastLocationRecord table to get the last location data of each person without querying the LocationRecord table.

The table will have following fields:

- id PK
- person_id FK
- location_id FK

Disadvantages of this method is that it requires additional storage space and it increases the complexity of the system.

### 2. Using distributed caching mechanism such as Redis or Memcached (Recommended)

Using Redis as a caching mechanism to store the last location data of each person. When a new location data is added to the LocationRecord table, we can update the Redis cache with the new data. This way, we can query the Redis cache to get the last location data of each person without querying the LocationRecord table.

This method is efficient because Redis is an in-memory data store and it provides faster read and write operations. However, it requires additional setup and maintenance of the Redis server.

### 3. Using Django's cache framework

Using Django's cache framework to store the last location data of each person. When a new location data is added to the LocationRecord table, we can update the cache with the new data. This way, we can query the cache to get the last location data of each person without querying the LocationRecord table.

This method is efficient because Django's cache framework provides a simple and efficient way to store and retrieve data. However, it requires additional memory usage.

### 4. Using a separate table to store the last 12 hours location data of each person

Creating a new table called "LastLocationRecord" to store the last location data of each person. This table will be updated every time a new location data is added to the LocationRecord table. This way, we can query the LastLocationRecord table to get the last location data of each person without querying the LocationRecord table.

This method is efficient because it reduces the number of queries to the LocationRecord table. However, it requires additional storage space and it increases the complexity of the system.

This can be done using triggers, procedures, or functions in the database.

### 5. Using distributed database such as Amazon Aurora or Google Cloud Spanner (Recommended but requires experience)

Using a distributed database such as Amazon Aurora or Google Cloud Spanner to store the last location data of each person. This way, we can query the distributed database to get the last location data of each person without querying the LocationRecord table.

This method is efficient because distributed databases provide faster read and write operations. However, it requires additional setup and maintenance of the distributed database.

### 6. Indexing the LocationRecord table (Recommended)

Creating indexes on the LocationRecord table to improve the performance of the queries. This way, we can query the LocationRecord table more efficiently.

This method is efficient because indexing improves the performance of the queries. However, it requires additional storage space and it increases the complexity of the system.

### 9. Database Views and Materialized Views (Recommended)

Creating database views and materialized views to store the last location data of each person. This way, we can query the views to get the last location data of each person without querying the LocationRecord table.

This method is efficient because views and materialized views provide a way to store and retrieve data without querying the LocationRecord table. However, it requires additional setup and maintenance of the views.

### 10. Using a NoSQL database such as MongoDB or Cassandra (Recommended)

Using a NoSQL database such as MongoDB or Cassandra to store the last location data of each person.

This method is efficient because NoSQL databases provide faster read and write operations. However, it requires additional setup and maintenance of the NoSQL database. Also, it changes the data structure and query language.

### 11. Changing the DB Structure to the Thread-based Structure (Recommended but requires experience)

Changing the database structure to a thread-based structure to store the last location data of each person. This way, we can query the thread-based structure with multiple threads to get the last location data of each person without blocking the system.

This method is efficient because it uses multiple threads to query the thread-based structure. However, it requires additional setup and maintenance of the thread-based structure. Also, it depends on the experience of the developer.

#### Managing a Non-Thread-Safe Database

To safely use a non-thread-safe database, you can employ various strategies:

- Single-Threaded Applications: Restrict the application to a single-threaded model where the database is accessed sequentially.

- Application-Level Locking: Implement locking mechanisms at the application level to control database access. This can involve mutexes, semaphores, or other synchronization techniques to ensure that only one thread interacts with the database at a time.

- Queueing Requests: Use a queuing system where database requests are serialized, processed one at a time, thereby avoiding direct concurrent access.

- Proxy or Middleware: Employ a middleware layer that can manage access to the database, ensuring that calls are handled in a thread-safe manner even if the database itself is not thread-safe.

#### Risks and Considerations

- Data Integrity: Without proper handling, using a non-thread-safe database can lead to data corruption, loss, or duplication, especially under concurrent access scenarios.

- Scalability: As application load increases, a non-thread-safe database might become a bottleneck, unable to efficiently handle increased traffic or parallel processing requirements.

- Complexity in Management: While the database itself may be simpler, managing access to it can introduce additional complexity into the application architecture, possibly negating the benefits of using a simpler database system.

### 12. Changing the System Architecture to Use WebSockets (Recommended)

Changing the system architecture as whenever a new location data is added to the LocationRecord table, we can send new data to the connected clients via WebSockets. This way, we can update the connected clients with the new data in real-time.

This method is efficient because it uses WebSockets to update the connected clients with the new data in real-time.
