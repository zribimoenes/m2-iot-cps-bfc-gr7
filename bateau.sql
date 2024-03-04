-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2024 at 03:16 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bateau`
--

-- --------------------------------------------------------

--
-- Table structure for table `bateau`
--

CREATE TABLE `bateau` (
  `id` int(11) NOT NULL,
  `num_place` int(11) NOT NULL,
  `gate_num` int(11) NOT NULL,
  `capacity` float NOT NULL,
  `hauteur` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bateau`
--

INSERT INTO `bateau` (`id`, `num_place`, `gate_num`, `capacity`, `hauteur`) VALUES
(1, 50, 2, 20000, 300),
(2, 80, 2, 30000, 400),
(3, 100, 2, 700000, 300);

-- --------------------------------------------------------

--
-- Table structure for table `voyageur`
--

CREATE TABLE `voyageur` (
  `num_pass` varchar(20) NOT NULL,
  `Nom` varchar(100) NOT NULL,
  `voiture_immat` varchar(20) NOT NULL,
  `v_poid` float NOT NULL,
  `id_bateau` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `voyageur`
--

INSERT INTO `voyageur` (`num_pass`, `Nom`, `voiture_immat`, `v_poid`, `id_bateau`) VALUES
('g1234', 'hani', 'pl1234', 200, 1),
('g789', 'anne', 'pl1234', 2000, 1),
('j8567', 'mones', 'mz3001', 500, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bateau`
--
ALTER TABLE `bateau`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `voyageur`
--
ALTER TABLE `voyageur`
  ADD PRIMARY KEY (`num_pass`),
  ADD KEY `bateau_id` (`id_bateau`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bateau`
--
ALTER TABLE `bateau`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `voyageur`
--
ALTER TABLE `voyageur`
  ADD CONSTRAINT `voyageur_ibfk_1` FOREIGN KEY (`id_bateau`) REFERENCES `bateau` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
