CREATE TABLE `students` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  `project` int DEFAULT NULL,
  `l_1` int DEFAULT NULL,
  `l_2` int DEFAULT NULL,
  `l_3` int DEFAULT NULL
) 

INSERT INTO `students` (`id`, `name`, `surname`, `email`, `status`, `project`, `l_1`, `l_2`, `l_3`) VALUES
(1, 'Jan', 'Kowalski', 'jk@pjwstk.edu.pl', 'None', 6, 1, 3, 4),
(3, 'Adam', 'Malysz', 'am@pjwstk.edu.pl', 'None', 5, 2, 3, 4);

ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);