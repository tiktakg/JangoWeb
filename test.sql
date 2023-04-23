-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3308
-- Время создания: Апр 23 2023 г., 04:28
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
  `nameAdmin` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `blog`
--

INSERT INTO `blog` (`primaryKey`, `name`, `tegs`, `data`, `nameImage`, `nameAdmin`) VALUES
(238, 'qwewqeqw', 'qwewqe', 'qwewqe', 'CloseEye.png', ''),
(239, 'qwewqeqw11', 'qwewqe', 'qwewqe', 'OpenEye.png', '');

-- --------------------------------------------------------

--
-- Структура таблицы `checkadmin`
--

CREATE TABLE `checkadmin` (
  `nameAdmin` int(15) NOT NULL,
  `isAdmin` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `checkadmin`
--

INSERT INTO `checkadmin` (`nameAdmin`, `isAdmin`) VALUES
(0, 1),
(0, 1),
(1, 0),
(1, 0),
(3, 1),
(3, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `logindata`
--

CREATE TABLE `logindata` (
  `primaryKey` int(11) NOT NULL,
  `login` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  `firstName` varchar(15) NOT NULL,
  `lastName` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `logindata`
--

INSERT INTO `logindata` (`primaryKey`, `login`, `password`, `firstName`, `lastName`) VALUES
(0, 'root', 'root', 'TestName', 'TestlastName'),
(1, 'user', 'user', '2Name', '2LastName'),
(3, 'root2', 'root2', 'TestName2', 'TestName2');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`primaryKey`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `checkadmin`
--
ALTER TABLE `checkadmin`
  ADD KEY `isAdmin` (`isAdmin`),
  ADD KEY `nameAdmin` (`nameAdmin`);

--
-- Индексы таблицы `logindata`
--
ALTER TABLE `logindata`
  ADD PRIMARY KEY (`primaryKey`,`login`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `blog`
--
ALTER TABLE `blog`
  MODIFY `primaryKey` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=241;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `checkadmin`
--
ALTER TABLE `checkadmin`
  ADD CONSTRAINT `checkadmin_ibfk_1` FOREIGN KEY (`nameAdmin`) REFERENCES `logindata` (`primaryKey`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
