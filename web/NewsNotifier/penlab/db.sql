-- Adminer 4.6.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `sqlidb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `sqlidb`;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `user` text COLLATE utf8mb4_unicode_ci NOT NULL,
	  `pass` text COLLATE utf8mb4_unicode_ci NOT NULL,
	  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `user` (`id`, `user`, `pass`) VALUES
(1,	'admin',	'4dM1n'),
(2,	'user',	'p4s5w0rd');

-- 2019-01-18 12:11:15
