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
-- Struttura della tabella `zona_lavoro_samuele_zaccarelli`
--

CREATE TABLE `zona_lavoro_samuele_zaccarelli` (
  `id` int(11) NOT NULL,
  `nome` varchar(30) NOT NULL,
  `numero_clienti` int(11) NOT NULL,
  `numero_dipendenti` int(11) NOT NULL,
  `id_dipendente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dump dei dati per la tabella `zona_lavoro_samuele_zaccarelli`
--

INSERT INTO `zona_lavoro_samuele_zaccarelli` (`id`, `nome`, `numero_clienti`, `numero_dipendenti`, `id_dipendente`) VALUES
(1, 'Ufficio DEV', 30, 20, 1),
(2, 'Scuola', 1000, 500, 3);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `zona_lavoro_samuele_zaccarelli`
--
ALTER TABLE `zona_lavoro_samuele_zaccarelli`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_dipendente` (`id_dipendente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `zona_lavoro_samuele_zaccarelli`
--
ALTER TABLE `zona_lavoro_samuele_zaccarelli`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `zona_lavoro_samuele_zaccarelli`
--
ALTER TABLE `zona_lavoro_samuele_zaccarelli`
  ADD CONSTRAINT `zona_lavoro_samuele_zaccarelli_ibfk_1` FOREIGN KEY (`id_dipendente`) REFERENCES `clienti_samuele_zaccarelli` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
