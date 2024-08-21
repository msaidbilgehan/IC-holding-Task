CREATE TABLE `Person` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL
);

CREATE TABLE `Task` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` text
);

CREATE TABLE `TaskAssignment` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `task_id` int NOT NULL,
  `person_id` int NOT NULL
);

CREATE TABLE `TaskCompletionLog` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `task_assignment_id` int NOT NULL,
  `time_start` timestamp NOT NULL,
  `time_completed` timestamp
);

CREATE INDEX `index_task_person_assignment` ON `TaskAssignment` (`task_id`, `person_id`);

CREATE UNIQUE INDEX `TaskAssignment_index_1` ON `TaskAssignment` (`id`);

CREATE INDEX `index_task_person_completion_log` ON `TaskCompletionLog` (`task_assignment_id`);

CREATE UNIQUE INDEX `TaskCompletionLog_index_3` ON `TaskCompletionLog` (`id`);

ALTER TABLE `TaskAssignment` ADD FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`);

ALTER TABLE `TaskAssignment` ADD FOREIGN KEY (`task_id`) REFERENCES `Task` (`id`);

ALTER TABLE `TaskCompletionLog` ADD FOREIGN KEY (`task_assignment_id`) REFERENCES `TaskAssignment` (`id`);
