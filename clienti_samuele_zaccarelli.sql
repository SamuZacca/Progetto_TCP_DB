-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 14, 2023 alle 20:47
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `5atepsit`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `clienti_samuele_zaccarelli`
--

CREATE TABLE `clienti_samuele_zaccarelli` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `cognome` varchar(30) NOT NULL,
  `data_nascita` date NOT NULL,
  `luogo_nascita` varchar(30) NOT NULL,
  `posizione_lavorativa` varchar(30) NOT NULL,
  `data_assunzione` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `clienti_samuele_zaccarelli`
--

INSERT INTO `clienti_samuele_zaccarelli` (`id`, `nome`, `cognome`, `data_nascita`, `luogo_nascita`, `posizione_lavorativa`, `data_assunzione`) VALUES
(1, 'Samuele', 'Zaccarelli', '2005-04-28', 'Carpi', 'Programmatore', '2023-05-29'),
(3, 'Iacopo', 'Ferrari', '1990-10-10', 'Correggio', 'Professore', '2020-09-15');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `clienti_samuele_zaccarelli`
--
ALTER TABLE `clienti_samuele_zaccarelli`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `clienti_samuele_zaccarelli`
--
ALTER TABLE `clienti_samuele_zaccarelli`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
