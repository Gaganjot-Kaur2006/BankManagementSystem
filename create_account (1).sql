-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2026 at 03:28 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbbank`
--

-- --------------------------------------------------------

--
-- Table structure for table `create_account`
--

CREATE TABLE `create_account` (
  `account_no` int(255) NOT NULL,
  `name` varchar(500) NOT NULL,
  `phn_no` varchar(500) NOT NULL,
  `account_type` varchar(500) NOT NULL,
  `pwd` varchar(500) NOT NULL,
  `opening_balance` int(255) NOT NULL,
  `available_balance` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `create_account`
--

INSERT INTO `create_account` (`account_no`, `name`, `phn_no`, `account_type`, `pwd`, `opening_balance`, `available_balance`) VALUES
(1001, 'Gaganjot Kaur', '7901800768\r\n', 'savings\r\n', 'gk@2006', 2000, '76000'),
(1002, 'Rahul Kumar', '7824593170', 'current', 'rk247', 1000, '1000'),
(1003, 'Karanveer Singh', '9885231476', 'savings', 'ks@2005', 2000, '52000'),
(1004, 'Harvin Kaur', '7845123690', 'savings\r\n', 'hkd@2004', 1500, '6547'),
(1006, 'Jasneev Kaur Brar', '7884556487', 'savings', '2026', 1500, '6500');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create_account`
--
ALTER TABLE `create_account`
  ADD PRIMARY KEY (`account_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `create_account`
--
ALTER TABLE `create_account`
  MODIFY `account_no` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1007;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
