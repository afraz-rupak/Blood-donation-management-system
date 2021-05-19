-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2021 at 09:10 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `b_d_m_s`
--

-- --------------------------------------------------------

--
-- Table structure for table `d_info`
--

CREATE TABLE `d_info` (
  `id` int(11) NOT NULL,
  `fname` text DEFAULT NULL,
  `lname` text DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` text DEFAULT NULL,
  `b_grp` text DEFAULT NULL,
  `address` text DEFAULT NULL,
  `mobile` text DEFAULT NULL,
  `job` text DEFAULT NULL,
  `month` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `d_info`
--

INSERT INTO `d_info` (`id`, `fname`, `lname`, `age`, `gender`, `b_grp`, `address`, `mobile`, `job`, `month`) VALUES
(10, 'Afraz', 'Rupak', 21, 'male', 'O+', 'Chandpur', '02626', 'Student', 'may'),
(12, 'Aunek', 'Ahammed', 21, 'male', 'B+', 'Dhanmondi', '0162', 'student', 'june'),
(13, 'Subrina', 'Sirajee', 21, 'Female', 'o+', 'Chitta', '0182', 'student', 'july');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `d_info`
--
ALTER TABLE `d_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `d_info`
--
ALTER TABLE `d_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
