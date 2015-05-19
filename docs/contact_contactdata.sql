-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Czas wygenerowania: 19 Maj 2015, 21:14
-- Wersja serwera: 5.5.41-0ubuntu0.14.04.1
-- Wersja PHP: 5.5.9-1ubuntu4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Baza danych: `django`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `contact_contactdata`
--

CREATE TABLE IF NOT EXISTS `contact_contactdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) COLLATE utf8_polish_ci NOT NULL,
  `value` varchar(70) COLLATE utf8_polish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci AUTO_INCREMENT=6 ;

--
-- Zrzut danych tabeli `contact_contactdata`
--

INSERT INTO `contact_contactdata` (`id`, `name`, `value`) VALUES
(1, 'email', 'tbajorek3@gmail.com'),
(2, 'address_name', 'Wypożyczalnia książek'),
(3, 'address_street', 'ul. Reymonta 17/263B'),
(4, 'address_city', '30-059 Kraków'),
(5, 'bank_number', '12524598741485479874587432');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
