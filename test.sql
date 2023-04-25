-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3308
-- Время создания: Апр 25 2023 г., 17:09
-- Версия сервера: 5.7.24
-- Версия PHP: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `test`
--

-- --------------------------------------------------------

--
-- Структура таблицы `blog`
--

CREATE TABLE `blog` (
  `primaryKey` int(11) NOT NULL,
  `name` varchar(25) NOT NULL,
  `tegs` varchar(100) NOT NULL,
  `data` varchar(500) NOT NULL,
  `nameImage` varchar(1000) DEFAULT NULL,
  `nameAdmin` int(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `blog`
--

INSERT INTO `blog` (`primaryKey`, `name`, `tegs`, `data`, `nameImage`, `nameAdmin`) VALUES
(238, 'qwewqeq', 'qwewqe', 'qwewqe', 'Screenshot 2023-04-24 110000.png', 0),
(239, 'qwewqeqw11', 'qwewqe', 'qwewqe', 'OpenEye.png', 0),
(243, 'test', 'dog,help', 'test', 'Screenshot 2023-04-24 110000.png', 0);

-- --------------------------------------------------------

--
-- Структура таблицы `logindata`
--

CREATE TABLE `logindata` (
  `primaryKey` int(11) NOT NULL,
  `login` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `firstName` varchar(15) NOT NULL,
  `lastName` varchar(15) NOT NULL,
  `id_checkAdmin` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `logindata`
--

INSERT INTO `logindata` (`primaryKey`, `login`, `password`, `firstName`, `lastName`, `id_checkAdmin`) VALUES
(0, 'root', 'root', 'TestName', 'TestlastName', 1),
(1, 'user', 'user', '2Name', '2LastName', 0),
(3, 'root2', 'root2', 'TestName2', 'TestName2', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id_roles` int(11) NOT NULL,
  `name_Roles` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id_roles`, `name_Roles`) VALUES
(1, 'admin');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`primaryKey`),
  ADD UNIQUE KEY `name` (`name`),
  ADD KEY `nameAdmin` (`nameAdmin`);

--
-- Индексы таблицы `logindata`
--
ALTER TABLE `logindata`
  ADD PRIMARY KEY (`primaryKey`,`login`),
  ADD KEY `id_checkAdmin` (`id_checkAdmin`),
  ADD KEY `primaryKey` (`primaryKey`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_roles`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `blog`
--
ALTER TABLE `blog`
  MODIFY `primaryKey` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=244;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id_roles` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `blog`
--
ALTER TABLE `blog`
  ADD CONSTRAINT `blog_ibfk_1` FOREIGN KEY (`nameAdmin`) REFERENCES `logindata` (`primaryKey`);

--
-- Ограничения внешнего ключа таблицы `roles`
--
ALTER TABLE `roles`
  ADD CONSTRAINT `roles_ibfk_1` FOREIGN KEY (`id_roles`) REFERENCES `logindata` (`id_checkAdmin`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
