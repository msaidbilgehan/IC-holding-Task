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
  `person_id` int NOT NULL,
  `frequency` int NOT NULL,
  `last_completed` timestamp NOT NULL
);

ALTER TABLE `TaskAssignment` ADD FOREIGN KEY (`person_id`) REFERENCES `Person` (`id`);

ALTER TABLE `TaskAssignment` ADD FOREIGN KEY (`task_id`) REFERENCES `Task` (`id`);
