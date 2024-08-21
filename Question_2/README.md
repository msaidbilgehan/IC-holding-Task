# Q2 - Architecture Optimization and Improvement

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

## Given Design

![Entity-Relationship Diagram](./1_model_first_implementation/er_diagram.png)

As we can see, given design has a one-to-one (1-1) relationship between `Person` and `Task` models. We need to store the frequency and last completion time of tasks by person. To achieve this, we need to create a new model named `TaskAssignment` that has a many-to-many relationship with `Person` and `Task` models. This new model will store the information of number of task-person pairs. Therefore we can calculate the frequency of tasks by person.

## Solution

### Many-to-Many

![Entity-Relationship Diagram](./2_requirements/er_diagram.png)

#### `TaskAssignment` Table

- **Purpose**: Manages the linkage between tasks and persons, indicating which tasks are assigned to which persons.
- **Fields and Keys**:
  - `task_id` and `person_id`: These foreign keys link the `TaskAssignment` directly to the specific `Task` and `Person`, establishing a many-to-many relationship through this associative table.
  - **Indexing**: The composite index on (`task_id`, `person_id`) enhances the efficiency of queries involving both task and person lookups, which is crucial for operations that need to retrieve task assignments quickly.
- **Functionality**: This table is critical for tracking which tasks are currently assigned, laying the groundwork for logging their completions.

#### `TaskCompletionLog` Table

- **Purpose**: Logs each instance when a task is started and completed, focusing on the specifics of each assignment's execution.
- **Fields and Keys**:
  - `task_assignment_id`: A foreign key that connects each entry in this log to a specific task assignment, thereby providing a direct link to both the task and the person involved through the `TaskAssignment` table.
  - `time_start` and `time_completed`: These timestamps are vital for tracking the duration and completion times of tasks.
  - **Indexing**: The index on `task_assignment_id` ensures that all logs related to a specific task assignment can be retrieved efficiently, which is vital for performance in scenarios with frequent access patterns.
- **Functionality**: This table is crucial for recording detailed completion data, enabling the analysis of task execution and frequency calculations.

### References

- Foreign keys establish relational integrity between entities:
  - `Person.id` < `TaskAssignment.person_id`
  - `Task.id` < `TaskAssignment.task_id`
  - `Person.id` < `TaskCompletionLog.person_id`
  - `Task.id` < `TaskCompletionLog.task_id`
- **Rationale**: These references ensure that tasks and persons associated with assignments and completions are valid and exist in their respective tables. It safeguards the database against orphan records and maintains data consistency across the schema.

This design effectively separates concerns by distinguishing between ongoing task assignments and historical completions, optimizing both operational needs (like viewing current assignments) and analytical requirements (like reviewing task completion histories).

### Frequency Calculation Compatibility

The structure supports calculating the frequency of task completions by utilizing the `TaskCompletionLog`. The linkage via `task_assignment_id` allows to aggregate completion data directly back to both the specific task and person involved without ambiguity.

```sql
SELECT
    TA.person_id,
    TA.task_id,
    COUNT(TCL.id) AS completion_count,
    AVG(TIMESTAMPDIFF(MONTH, TCL.time_start, TCL.time_completed)) AS average_completion_time
FROM
    TaskAssignment TA
JOIN
    TaskCompletionLog TCL ON TA.id = TCL.task_assignment_id
WHERE
    TCL.time_completed BETWEEN DATE_SUB(NOW(), INTERVAL 1 MONTH) AND NOW()
GROUP BY
    TA.person_id, TA.task_id;
```
