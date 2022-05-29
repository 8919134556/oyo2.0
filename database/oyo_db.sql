-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 24, 2022 at 02:09 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oyo_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add hotel model', 7, 'add_hotelmodel'),
(26, 'Can change hotel model', 7, 'change_hotelmodel'),
(27, 'Can delete hotel model', 7, 'delete_hotelmodel'),
(28, 'Can view hotel model', 7, 'view_hotelmodel'),
(29, 'Can add travel model', 8, 'add_travelmodel'),
(30, 'Can change travel model', 8, 'change_travelmodel'),
(31, 'Can delete travel model', 8, 'delete_travelmodel'),
(32, 'Can view travel model', 8, 'view_travelmodel'),
(33, 'Can add user model', 9, 'add_usermodel'),
(34, 'Can change user model', 9, 'change_usermodel'),
(35, 'Can delete user model', 9, 'delete_usermodel'),
(36, 'Can view user model', 9, 'view_usermodel'),
(37, 'Can add hoteldashboard model', 10, 'add_hoteldashboardmodel'),
(38, 'Can change hoteldashboard model', 10, 'change_hoteldashboardmodel'),
(39, 'Can delete hoteldashboard model', 10, 'delete_hoteldashboardmodel'),
(40, 'Can view hoteldashboard model', 10, 'view_hoteldashboardmodel'),
(41, 'Can add cardashboard model', 11, 'add_cardashboardmodel'),
(42, 'Can change cardashboard model', 11, 'change_cardashboardmodel'),
(43, 'Can delete cardashboard model', 11, 'delete_cardashboardmodel'),
(44, 'Can view cardashboard model', 11, 'view_cardashboardmodel'),
(45, 'Can add cruisesdashboard model', 12, 'add_cruisesdashboardmodel'),
(46, 'Can change cruisesdashboard model', 12, 'change_cruisesdashboardmodel'),
(47, 'Can delete cruisesdashboard model', 12, 'delete_cruisesdashboardmodel'),
(48, 'Can view cruisesdashboard model', 12, 'view_cruisesdashboardmodel'),
(49, 'Can add flightdashboard model', 13, 'add_flightdashboardmodel'),
(50, 'Can change flightdashboard model', 13, 'change_flightdashboardmodel'),
(51, 'Can delete flightdashboard model', 13, 'delete_flightdashboardmodel'),
(52, 'Can view flightdashboard model', 13, 'view_flightdashboardmodel'),
(53, 'Can add user hotel booking', 14, 'add_userhotelbooking'),
(54, 'Can change user hotel booking', 14, 'change_userhotelbooking'),
(55, 'Can delete user hotel booking', 14, 'delete_userhotelbooking'),
(56, 'Can view user hotel booking', 14, 'view_userhotelbooking'),
(57, 'Can add room booking', 15, 'add_roombooking'),
(58, 'Can change room booking', 15, 'change_roombooking'),
(59, 'Can delete room booking', 15, 'delete_roombooking'),
(60, 'Can view room booking', 15, 'view_roombooking'),
(61, 'Can add car booking', 16, 'add_carbooking'),
(62, 'Can change car booking', 16, 'change_carbooking'),
(63, 'Can delete car booking', 16, 'delete_carbooking'),
(64, 'Can view car booking', 16, 'view_carbooking'),
(65, 'Can add cruises booking', 17, 'add_cruisesbooking'),
(66, 'Can change cruises booking', 17, 'change_cruisesbooking'),
(67, 'Can delete cruises booking', 17, 'delete_cruisesbooking'),
(68, 'Can view cruises booking', 17, 'view_cruisesbooking'),
(69, 'Can add flight booking', 18, 'add_flightbooking'),
(70, 'Can change flight booking', 18, 'change_flightbooking'),
(71, 'Can delete flight booking', 18, 'delete_flightbooking'),
(72, 'Can view flight booking', 18, 'view_flightbooking'),
(73, 'Can add feedback', 19, 'add_feedback'),
(74, 'Can change feedback', 19, 'change_feedback'),
(75, 'Can delete feedback', 19, 'delete_feedback'),
(76, 'Can view feedback', 19, 'view_feedback'),
(77, 'Can add user feedback', 20, 'add_userfeedback'),
(78, 'Can change user feedback', 20, 'change_userfeedback'),
(79, 'Can delete user feedback', 20, 'delete_userfeedback'),
(80, 'Can view user feedback', 20, 'view_userfeedback'),
(81, 'Can add user fb', 21, 'add_userfb'),
(82, 'Can change user fb', 21, 'change_userfb'),
(83, 'Can delete user fb', 21, 'delete_userfb'),
(84, 'Can view user fb', 21, 'view_userfb'),
(85, 'Can add user feedback', 22, 'add_userfeedback'),
(86, 'Can change user feedback', 22, 'change_userfeedback'),
(87, 'Can delete user feedback', 22, 'delete_userfeedback'),
(88, 'Can view user feedback', 22, 'view_userfeedback');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `booking_car_details`
--

CREATE TABLE `booking_car_details` (
  `car_booking_id` int(11) NOT NULL,
  `car_from` varchar(50) NOT NULL,
  `to` varchar(50) NOT NULL,
  `journey_date` date NOT NULL,
  `return_date` date NOT NULL,
  `pick_up` varchar(50) NOT NULL,
  `drop_off` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_car_details`
--

INSERT INTO `booking_car_details` (`car_booking_id`, `car_from`, `to`, `journey_date`, `return_date`, `pick_up`, `drop_off`, `email`, `phone`, `agency_id`) VALUES
(1, 'hyderabad', 'vijayawada', '2022-03-11', '2022-03-12', 'ammerpeta', 'bander', 'surya123@gmail.com', '8919134556', NULL),
(2, 'hyderabad', 'vijayawada', '2022-03-13', '2022-03-14', 'ammerpeta', 'bander', 'surya123@gmail.com', '8919134556', NULL),
(3, 'hyderabad', 'vijayawada', '2022-03-11', '2022-03-11', 'ammerpeta', 'bander', 'anand1234@gmail.com', '8919134556', NULL),
(4, 'hyderabad', 'vijayawada', '2022-03-10', '2022-03-10', 'ammerpeta', 'bander', 'surya123anand@gmail.com', '8919134556', NULL),
(5, 'hyderabad', 'vijayawada', '2022-03-11', '2022-03-10', 'ammerpeta', 'bander', 'surya123@gmail.com', '8919134556', NULL),
(6, 'hyderabad', 'vijayawada', '2022-03-11', '2022-03-11', 'ammerpeta', 'bander', 'surya123@gmail.com', '8919134556', NULL),
(7, 'hyderabad', 'ongole', '2022-03-04', '2022-03-05', 'uppal', 'ongole', 'srimannarayanabiruduraju96010@gmail.com', '6300537678', NULL),
(10, 'guntur', 'hyderabad', '2022-03-23', '2022-03-24', 'bharathapeta', 'ameerpeta', 'suryaanand456@gmail.com', '8919134556', NULL),
(11, 'guntur', 'hyderabad', '2022-03-23', '2022-03-23', 'bharathapeta', 'ameerpeta', 'suryaanand456@gmail.com', '8919134556', 10),
(12, 'guntur', 'hyderabad', '2022-03-23', '2022-03-24', 'bharathapeta', 'ameerpeta', 'suryaanand456@gmail.com', '8919134556', 10),
(13, 'hyderabad', 'guntur', '2022-03-23', '2022-03-24', 'ammerpeta', 'guntur', 'surya123@gmail.com', '8919134556', 10),
(14, 'hyderabad', 'guntur', '2022-03-23', '2022-03-23', 'ammerpeta', 'guntur', 'surya123@gmail.com', '8919134556', 10),
(15, 'surya', 'surya', '2022-03-09', '2022-03-01', 'surya', 'surya', 'surya123@gmail.com', '8919134556', 12);

-- --------------------------------------------------------

--
-- Table structure for table `booking_cruises_details`
--

CREATE TABLE `booking_cruises_details` (
  `cruises_booking_id` int(11) NOT NULL,
  `addres` varchar(50) NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `passport` varchar(50) NOT NULL,
  `select_class` varchar(50) NOT NULL,
  `no_adults` varchar(50) NOT NULL,
  `no_children` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_cruises_details`
--

INSERT INTO `booking_cruises_details` (`cruises_booking_id`, `addres`, `check_in`, `check_out`, `passport`, `select_class`, `no_adults`, `no_children`, `email`, `phone`, `agency_id`) VALUES
(1, 'hyderabad', '2022-03-12', '2022-03-12', '456gyuhjfygbhjn', 'econamy', '1', '0', 'example@123gmail.com', '9989228601', NULL),
(2, 'hyderabad', '2022-03-11', '2022-03-12', 'dwertyi', 'ordinary', '1', '0', 'example@123gmail.com', '8919134556', NULL),
(3, 'hyderabad', '2022-03-03', '2022-03-02', 'chfyvngu59', 'ordinary', '1', '0', 'suryaanand456@gmail.com', '8919134556', NULL),
(4, 'hyderabad', '2022-03-04', '2022-03-04', 'fgyudxhga698', 'business', '1', '0', 'srimannarayanabiruduraju96010@gmail.com', '6300537678', NULL),
(10, '4-16-55 bharapeta', '2022-03-23', '2022-03-23', 'as424', 'ordinary', '1', '0', 'suryaanand456@gmail.com', '8919134556', NULL),
(11, 'surya', '2022-03-30', '2022-03-02', 'agfbjygn', 'ordinary', '1', '0', 'surya123@gmail.com', '8919134556', 10);

-- --------------------------------------------------------

--
-- Table structure for table `booking_flight_details`
--

CREATE TABLE `booking_flight_details` (
  `flight_booking_id` int(11) NOT NULL,
  `addres` varchar(50) NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `passport` varchar(50) NOT NULL,
  `select_class` varchar(50) NOT NULL,
  `no_adults` varchar(50) NOT NULL,
  `no_children` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_flight_details`
--

INSERT INTO `booking_flight_details` (`flight_booking_id`, `addres`, `check_in`, `check_out`, `passport`, `select_class`, `no_adults`, `no_children`, `email`, `phone`, `agency_id`) VALUES
(1, 'hyderabad', '2022-03-11', '2022-03-12', 'ao41563gvhbj', 'ordinary', '1', '0', 'example@123gmail.com', '8919134556', NULL),
(2, 'hyderabad', '2022-03-04', '2022-03-02', 'xcbyvnugyhu6', 'ordinary', '1', '0', 'suryaanand456@gmail.com', '8919134556', NULL),
(3, 'hyderabad', '2022-03-04', '2022-03-02', 'xcbyvnugyhu6', 'ordinary', '1', '0', 'suryaanand456@gmail.com', '8919134556', NULL),
(4, 'hyderabad', '2022-03-04', '2022-03-04', '25754gujy', 'business', '1', '0', 'srimannarayanabiruduraju96010@gmail.com', '6300537678', NULL),
(10, '4-16-55 bharapeta', '2022-03-23', '2022-03-23', 'As56824', 'ordinary', '1', '0', 'suryaanand456@gmail.com', '8919134566', NULL),
(11, 'hyderabad', '2022-03-10', '2022-03-08', 'As56824', 'ordinary', '1', '0', 'surya123@gmail.com', '8919134556', 10),
(12, 'hyderabad', '2022-03-25', '2022-03-26', 'asdf82829', 'econamy', '1', '0', 'anand123@gmail.com', '8919134556', 10);

-- --------------------------------------------------------

--
-- Table structure for table `booking_room_details`
--

CREATE TABLE `booking_room_details` (
  `booking_id` int(11) NOT NULL,
  `room_Addres` varchar(50) NOT NULL,
  `room_check_in` date NOT NULL,
  `room_check_out` date NOT NULL,
  `no_rooms` varchar(50) NOT NULL,
  `no_adults` varchar(50) NOT NULL,
  `no_children` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `room_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_room_details`
--

INSERT INTO `booking_room_details` (`booking_id`, `room_Addres`, `room_check_in`, `room_check_out`, `no_rooms`, `no_adults`, `no_children`, `email`, `phone`, `room_id`) VALUES
(59, 'madhapur', '2022-03-23', '2022-03-23', '1', '1', '0', 'suryaanand456@gmail.com', '8919134556', 35),
(60, 'panjagutta', '2022-03-23', '2022-03-24', '1', '1', '0', 'suryaanand456@gmail.com', '8919134556', 38),
(61, 'guntur', '2022-03-07', '2022-03-17', '1', '1', '0', 'anand123@gmail.com', '8919134556', 35);

-- --------------------------------------------------------

--
-- Table structure for table `car_dashboard`
--

CREATE TABLE `car_dashboard` (
  `car_id` int(11) NOT NULL,
  `car_type` varchar(50) NOT NULL,
  `car_model` varchar(50) NOT NULL,
  `car_no` varchar(50) NOT NULL,
  `select_car` varchar(50) NOT NULL,
  `price` varchar(100) DEFAULT NULL,
  `car_photo` varchar(100) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `car_dashboard`
--

INSERT INTO `car_dashboard` (`car_id`, `car_type`, `car_model`, `car_no`, `select_car`, `price`, `car_photo`, `agency_id`) VALUES
(4, 'Hatchback', '6 setting', 'TS45S8551', 'Non-A/C Car', '500.00', 'car/images/tesla-model-s.png', NULL),
(5, 'Sedan', '6 sitting', 'TS446S8545', 'Non-A/C Car', '3000.00', 'car/images/cars.jpg', NULL),
(6, 'MUV/SUV', '2 sitting', 'TS45S8551', 'A/C Car', '5000.00', 'car/images/tesla-model-s_VCveu66.png', NULL),
(7, 'Coupe', '5 sitting', 'TS45S8551', 'A/C Car', '4000.00', 'car/images/tesla-model-s_FD8yKJB.png', NULL),
(8, 'Wagon', '4-sitting', 'TS45S8551', 'Non-A/C Car', '5000.00', 'car/images/cars1.jpg', NULL),
(9, 'Sedan', '4 sitting', 'TS45S8551', 'Non-A/C Car', '5000', 'car/images/cars_IQjGoBA.jpg', 10),
(10, 'Hatchback', '6 setting', 'TS446S8545', 'Non-A/C Car', '5000', 'car/images/cars1_iVpLUe5.jpg', 10),
(11, 'Wagon', '4 sitting', 'TS45S8551', 'A/C Car', '5000', 'car/images/cars1_vDGlf2W.jpg', 12),
(12, 'Hatchback', '4-sitting', 'TS446S8545', 'Non-A/C Car', '500', 'car/images/visa.png', 14);

-- --------------------------------------------------------

--
-- Table structure for table `cruises_dashboard`
--

CREATE TABLE `cruises_dashboard` (
  `cruises_id` int(11) NOT NULL,
  `cruises_name` longtext NOT NULL,
  `cruises_no` varchar(50) NOT NULL,
  `select_class` varchar(50) NOT NULL,
  `from` varchar(50) NOT NULL,
  `to` varchar(50) NOT NULL,
  `via` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `check_in` time(6) NOT NULL,
  `check_out` time(6) NOT NULL,
  `price` varchar(100) DEFAULT NULL,
  `cruises_photo` varchar(100) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cruises_dashboard`
--

INSERT INTO `cruises_dashboard` (`cruises_id`, `cruises_name`, `cruises_no`, `select_class`, `from`, `to`, `via`, `date`, `check_in`, `check_out`, `price`, `cruises_photo`, `agency_id`) VALUES
(1, 'lilala', '4152', 'Economic Class', 'mumbai', 'nagoal', 'goa', '2022-06-12', '15:30:00.000000', '15:45:00.000000', '7000.00', 'cruises/images/ships_0jah6CH.jpg', NULL),
(3, 'majunu', '456456', 'Business Class', 'hyderabad', 'goa', 'vijayawada', '2020-06-12', '15:00:00.000000', '15:00:00.000000', '400.00', 'cruises/images/ships1.jpg', NULL),
(4, 'jinda', '456', 'Economic Class', 'goa', 'gujarath', 'mumbai', '2020-06-12', '00:00:00.000000', '12:00:00.000000', '3000.00', 'cruises/images/ships1_PIlstdb.jpg', NULL),
(5, 'lilala', '456456', 'Economic Class', 'goa', 'mumbai', 'kolkotha', '2022-03-23', '03:00:00.000000', '15:00:00.000000', '500', 'cruises/images/ships1_qf6EZbo.jpg', 10);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'hotelapp', 'hoteldashboardmodel'),
(7, 'hotelapp', 'hotelmodel'),
(22, 'mainapp', 'userfeedback'),
(6, 'sessions', 'session'),
(11, 'travelapp', 'cardashboardmodel'),
(12, 'travelapp', 'cruisesdashboardmodel'),
(13, 'travelapp', 'flightdashboardmodel'),
(8, 'travelapp', 'travelmodel'),
(16, 'userapp', 'carbooking'),
(17, 'userapp', 'cruisesbooking'),
(19, 'userapp', 'feedback'),
(18, 'userapp', 'flightbooking'),
(15, 'userapp', 'roombooking'),
(21, 'userapp', 'userfb'),
(20, 'userapp', 'userfeedback'),
(14, 'userapp', 'userhotelbooking'),
(9, 'userapp', 'usermodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-03-04 12:08:57.503981'),
(2, 'auth', '0001_initial', '2022-03-04 12:08:58.975045'),
(3, 'admin', '0001_initial', '2022-03-04 12:08:59.298181'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-03-04 12:08:59.318170'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-03-04 12:08:59.342063'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-03-04 12:08:59.552506'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-03-04 12:08:59.736006'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-03-04 12:08:59.775901'),
(9, 'auth', '0004_alter_user_username_opts', '2022-03-04 12:08:59.795881'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-03-04 12:08:59.912535'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-03-04 12:08:59.919516'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-03-04 12:08:59.939465'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-03-04 12:08:59.980357'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-03-04 12:09:00.013266'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-03-04 12:09:00.057149'),
(16, 'auth', '0011_update_proxy_permissions', '2022-03-04 12:09:00.079091'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-03-04 12:09:00.114994'),
(18, 'sessions', '0001_initial', '2022-03-04 12:09:00.204755'),
(19, 'hotelapp', '0001_initial', '2022-03-04 12:09:58.814461'),
(20, 'hotelapp', '0002_auto_20220304_2042', '2022-03-04 15:12:48.974153'),
(21, 'hotelapp', '0003_auto_20220304_2046', '2022-03-04 15:16:54.304860'),
(22, 'hotelapp', '0004_auto_20220304_2147', '2022-03-04 16:17:47.040138'),
(23, 'hotelapp', '0005_auto_20220304_2205', '2022-03-04 16:38:00.616342'),
(24, 'hotelapp', '0006_auto_20220304_2218', '2022-03-04 16:49:07.137608'),
(25, 'hotelapp', '0007_auto_20220304_2244', '2022-03-04 17:14:45.052062'),
(26, 'hotelapp', '0008_auto_20220304_2245', '2022-03-04 17:16:07.158500'),
(27, 'travelapp', '0001_initial', '2022-03-05 06:25:54.761234'),
(28, 'userapp', '0001_initial', '2022-03-05 07:44:05.143566'),
(29, 'hotelapp', '0009_auto_20220309_1204', '2022-03-09 06:35:02.086141'),
(30, 'hotelapp', '0010_auto_20220309_1411', '2022-03-09 08:41:15.217869'),
(31, 'travelapp', '0002_cardashboardmodel', '2022-03-10 05:55:02.036984'),
(32, 'travelapp', '0003_cruisesdashboardmodel_flightdashboardmodel', '2022-03-10 06:05:22.927666'),
(33, 'travelapp', '0004_alter_cardashboardmodel_car_photo', '2022-03-10 08:52:38.573434'),
(34, 'travelapp', '0005_alter_flightdashboardmodel_flight_photo', '2022-03-10 11:38:52.959535'),
(35, 'travelapp', '0006_alter_cruisesdashboardmodel_cruises_photo', '2022-03-10 12:36:49.348597'),
(36, 'userapp', '0002_userhotelbooking', '2022-03-12 05:16:05.665335'),
(37, 'userapp', '0003_auto_20220312_1047', '2022-03-12 06:01:44.815295'),
(38, 'userapp', '0004_auto_20220312_1051', '2022-03-12 06:01:44.824270'),
(39, 'userapp', '0005_auto_20220312_1100', '2022-03-12 06:01:44.832288'),
(40, 'userapp', '0006_auto_20220312_1102', '2022-03-12 06:01:44.841303'),
(41, 'userapp', '0007_delete_userroombooking', '2022-03-12 06:01:44.849279'),
(42, 'userapp', '0008_userroombooking', '2022-03-12 06:01:44.857223'),
(43, 'userapp', '0009_delete_userroombooking', '2022-03-12 06:01:44.872184'),
(44, 'userapp', '0010_roombooking', '2022-03-12 06:01:44.888140'),
(45, 'userapp', '0011_delete_roombooking', '2022-03-12 06:04:53.213032'),
(46, 'userapp', '0012_roombooking', '2022-03-12 06:06:17.184529'),
(47, 'userapp', '0013_carbooking', '2022-03-12 07:01:08.226758'),
(48, 'userapp', '0014_cruisesbooking_flightbooking', '2022-03-12 07:44:47.214853'),
(49, 'userapp', '0015_auto_20220315_1531', '2022-03-15 10:01:43.309750'),
(50, 'userapp', '0016_auto_20220315_1540', '2022-03-15 10:10:51.954700'),
(51, 'travelapp', '0007_auto_20220315_1552', '2022-03-15 10:22:24.302389'),
(52, 'hotelapp', '0011_auto_20220315_1620', '2022-03-15 10:50:39.948506'),
(53, 'travelapp', '0008_auto_20220318_1441', '2022-03-18 09:12:07.864350'),
(54, 'hotelapp', '0012_hotelmodel_status', '2022-03-18 10:13:15.216281'),
(55, 'userapp', '0017_auto_20220319_1857', '2022-03-19 13:27:33.357601'),
(56, 'userapp', '0018_feedback', '2022-03-21 04:51:58.070793'),
(57, 'userapp', '0019_auto_20220321_1035', '2022-03-21 05:05:48.357213'),
(58, 'hotelapp', '0013_hoteldashboardmodel_hotel_id', '2022-03-21 09:50:27.899525'),
(59, 'userapp', '0020_roombooking_room_id', '2022-03-21 10:25:29.405622'),
(60, 'travelapp', '0009_auto_20220322_1223', '2022-03-22 06:53:09.408102'),
(61, 'userapp', '0002_auto_20220322_1225', '2022-03-22 06:55:48.044452'),
(62, 'userapp', '0003_feedback_servies', '2022-03-22 17:29:21.770821'),
(63, 'userapp', '0002_alter_feedback_table', '2022-03-24 06:08:46.702814'),
(64, 'mainapp', '0001_initial', '2022-03-24 06:42:49.723575'),
(65, 'mainapp', '0002_alter_userfeedback_agency_id', '2022-03-24 06:56:46.662979'),
(66, 'mainapp', '0003_userfeedback_email', '2022-03-24 07:22:26.912633');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ds490mhvw8cskiq7njqw6a8q6yi5x3k9', '.eJyrViotTi2Kz0xRslIqLsrMTczLSyxKrEzMS0zKLCpNKi1KzCq1NDMwNHBIz03MzNFLzs9V0oHoSQUJgLSVFlUmAjXkpZiYmiEpqwUAGNAhDQ:1nUp6t:pjBKNVJrg9iQVcwilpGadFHN3R5873D_3F8G7Ds7Ko4', '2022-03-31 12:20:07.452387'),
('rq5zghxok6d1dtcpebucomzniap00yd8', '.eJyFjs0KwjAQhN9lz4uY_gTpyTcpa7rEYJOFxAhFfPfGWKF48TYz8M3ME3LiOLInN8MAKceFKFCYul6f7Ts9GPGAEEX86CYYGo1wEbm5YKvXCuEqd56ra08I_8vIcjBLBdQRoTx4OE4FMTG7VBR-bu16-y36QTf7naxrqml3a68VFq1MZw:1nXLV4:bFINXl5D6uTqqbwlm09og6mlGV2kvMr_untiO41lzgc', '2022-04-07 11:19:30.715815'),
('wi661cidj2k9mx91hs2tlmz2057acgd0', '.eJxVjcEOQDAQRP9lz41oqYOTP5FFU422mxQHEf-u1oXjZOa9OWFfTerdBC1gxDhJVXU2oPPFSAEEzLQZz32lBaA1cTw4ylK8rHnWGV_3dCA7at38HL9Flx--ZSIKLFRKwEC0uGg56_q6AU2FNDM:1nWGAM:ShovEU2XpANAI5J0U_-cfv7b89sCLTrRDPDFMfnhs6A', '2022-04-04 11:25:38.276613');

-- --------------------------------------------------------

--
-- Table structure for table `flight_dashboard`
--

CREATE TABLE `flight_dashboard` (
  `flight_id` int(11) NOT NULL,
  `flight_name` varchar(50) NOT NULL,
  `flight_no` varchar(50) NOT NULL,
  `select_class` varchar(50) NOT NULL,
  `trom` varchar(50) NOT NULL,
  `to` varchar(50) NOT NULL,
  `via` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `check_in` time(6) NOT NULL,
  `check_out` time(6) NOT NULL,
  `price` varchar(100) DEFAULT NULL,
  `flight_photo` varchar(100) NOT NULL,
  `agency_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flight_dashboard`
--

INSERT INTO `flight_dashboard` (`flight_id`, `flight_name`, `flight_no`, `select_class`, `trom`, `to`, `via`, `date`, `check_in`, `check_out`, `price`, `flight_photo`, `agency_id`) VALUES
(3, 'indigo', '458252', 'Economic Class', 'benguluru', 'vijayawada', 'hyderabad', '2021-06-12', '12:00:00.000000', '12:30:00.000000', '3000.00', 'room/images/flights45.jpg', NULL),
(4, 'kingfisher', '123456', 'Business Class', 'hyderabad', 'benguluru', 'vijayawada', '2021-03-04', '15:15:00.000000', '15:30:00.000000', '6000.00', 'room/images/travel3_7DoKv1L.png', NULL),
(5, 'air india', '4582', 'Ordinary Class', 'hyderabad', 'jai pur', 'gujarath', '2022-06-20', '01:30:00.000000', '02:45:00.000000', '4000.00', 'flight/images/flight.jfif', NULL),
(6, 'air india', '154669', 'Ordinary Class', 'hyderabad', 'gujarath', 'vijayawada', '2020-01-12', '13:00:00.000000', '13:30:00.000000', '5000.00', 'flight/images/flights45.jpg', NULL),
(7, 'airindia', '154669', 'Ordinary Class', 'ameerpet', 'panjagutta', 'lb nagar', '2022-03-08', '03:00:00.000000', '15:00:00.000000', '400', 'flight/images/flight_GWNIoW4.jfif', 10);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_dashboard`
--

CREATE TABLE `hotel_dashboard` (
  `room_id` int(11) NOT NULL,
  `room_type` varchar(50) NOT NULL,
  `room_size` varchar(50) NOT NULL,
  `check_in` time(6) NOT NULL,
  `check_out` time(6) NOT NULL,
  `price` varchar(100) DEFAULT NULL,
  `description` varchar(100) NOT NULL,
  `hotel_policies` varchar(100) NOT NULL,
  `room_photo` varchar(100) NOT NULL,
  `hotel_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_dashboard`
--

INSERT INTO `hotel_dashboard` (`room_id`, `room_type`, `room_size`, `check_in`, `check_out`, `price`, `description`, `hotel_policies`, `room_photo`, `hotel_id`) VALUES
(20, 'Delux', '45sqft', '15:00:00.000000', '03:00:00.000000', '9850.00', 'good', 'besst room', 'room/images/bg-smart-home-2_uxQvuT1.jpg', 35),
(22, 'Ordinary', '89898sqft', '03:00:00.000000', '15:00:00.000000', '5', 'bada', 'bada', 'room/images/cars_DrjujBU.jpg', 35),
(23, 'Delux', '89 sqft', '15:00:00.000000', '03:00:00.000000', '8595', 'best rooms in world', 'world', 'room/images/bg-smart-home-2_S2RtGvT.jpg', 35),
(26, 'Delux', '45sqft', '03:00:00.000000', '15:00:00.000000', '500', 'best', 'hotel', 'room/images/visa.png', 38);

-- --------------------------------------------------------

--
-- Table structure for table `hotel_details`
--

CREATE TABLE `hotel_details` (
  `hotel_id` int(11) NOT NULL,
  `hotel_name` varchar(50) NOT NULL,
  `hotel_pan_number` varchar(50) NOT NULL,
  `hotel_Addres` varchar(50) NOT NULL,
  `hotel_phone` bigint(20) NOT NULL,
  `hotel_email` varchar(100) DEFAULT NULL,
  `hotel_pwd` varchar(100) NOT NULL,
  `hotel_photo` varchar(100) NOT NULL,
  `hotel_certificate` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_details`
--

INSERT INTO `hotel_details` (`hotel_id`, `hotel_name`, `hotel_pan_number`, `hotel_Addres`, `hotel_phone`, `hotel_email`, `hotel_pwd`, `hotel_photo`, `hotel_certificate`, `status`) VALUES
(35, 'kkr', 'ASDF4562A', 'hyderabad', 8919134556, 'surya@123gmail.com', 'qwer', 'hotel/images/hotel4.jpg', 'hotel/certificate/bg-smart-home-2.jpg', 'Accepted'),
(38, 'suryaanand', 'ASDF4567Q', 'hyderabad', 8998, 'suryaanand456@gmail.com', 'Anand@123', 'hotel/images/bg-smart-home-2.jpg', 'hotel/certificate/bg-smart-home-2_r34gZfd.jpg', 'Accepted'),
(39, 'surya', 'ASDF4567Q', 'hyderabad', 8919134556, 'surya123@gmail.com', 'Anand@123', 'hotel/images/bg-smart-home-2_dkaESSE.jpg', 'hotel/certificate/bg-smart-home-2_XT332WU.jpg', 'Accepted'),
(40, 'suryaanand', 'ASDF4567Q', 'hyderabad', 755, 'suryaanand@gmail.com', 'Aanad@123', 'hotel/images/bg-smart-home-2_hfRBx2a.jpg', 'hotel/certificate/bg-smart-home-2_OAUia69.jpg', 'Accepted'),
(41, 'surya', 'ASDF4567Q', 'hyderabad', 8929, 'anand52986@gmail.com', 'Anand@123', 'hotel/images/cars.jpg', 'hotel/certificate/bg-smart-home-2_KzDygsF.jpg', 'Accepted'),
(42, 'surya', 'ASDF4567Q', '65898', 8919134556, 'surya5256@gmail.com', 'Anand@123', 'hotel/images/cars_wtmbED6.jpg', 'hotel/certificate/bg-smart-home-2_hBY3DZ9.jpg', 'Accepted'),
(43, '52688652', 'ASDF4567Q', 'hyderabad', 8919134556, 'sgnkyuhm428@gmail.com', 'Anand@123', 'hotel/images/bg-smart-home-2_jC2vWz5.jpg', 'hotel/certificate/cars.jpg', 'Rejected'),
(45, 'surya', 'ASDF4567Q', 'hyderabad', 8919134556, 'surya123@yahoo.com', 'Anand@123', 'hotel/images/bg-smart-home-2_A0bwKJA.jpg', 'hotel/certificate/bg-smart-home-2_KZyYCLL.jpg', 'pending'),
(46, 'suryaanand', 'BGFD7458Q', 'hyderabad', 9393055901, 'suryanand895@yahoo.com', 'Anand@123', 'hotel/images/bg-smart-home-2_GW4Y8WL.jpg', 'hotel/certificate/bg-smart-home-2_G6BMdto.jpg', 'Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `travel_details`
--

CREATE TABLE `travel_details` (
  `agency_id` int(11) NOT NULL,
  `agency_name` longtext NOT NULL,
  `agency_pan_number` varchar(50) NOT NULL,
  `agency_Addres` varchar(50) NOT NULL,
  `agency_phone` bigint(20) NOT NULL,
  `agency_email` varchar(100) DEFAULT NULL,
  `agency_pwd` varchar(100) NOT NULL,
  `agency_photo` varchar(100) NOT NULL,
  `iata_certificate` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `travel_details`
--

INSERT INTO `travel_details` (`agency_id`, `agency_name`, `agency_pan_number`, `agency_Addres`, `agency_phone`, `agency_email`, `agency_pwd`, `agency_photo`, `iata_certificate`, `status`) VALUES
(10, 'anand agency', 'ASDF4567Q', 'hyderabad', 8919134556, 'surya123anand@gmail.com', 'Anand@123', 'travel/images/cars_N0swP9S.jpg', 'travel/certificate/cars1.jpg', 'Accepted'),
(11, 'surya', 'vtfbygunh\'p.[', 'hyderabad', 8919134556, 'suryaanand975@gmail.com', 'Anand@123', 'travel/images/bruce-mars.jpg', 'travel/certificate/bruce-mars.jpg', 'Rejected'),
(12, 'anand', 'SURYA4565Q', 'hyderabad', 8919134556, 'surya123@gmail.com', 'Surya@123', 'travel/images/bruce-mars_ZAv6ZWh.jpg', 'travel/certificate/drake.jpg', 'Accepted'),
(13, 'surya', 'WERTY8520A', 'hyderabad', 8919134556, 'suryaanand654@gmail.com', 'Anand@123', 'travel/images/tesla-model-s.png', 'travel/certificate/travel.jpg', 'pending'),
(14, 'anand', 'ASDF4567Q', 'hyderabad', 8919134556, 'suryaanand456@gmail.com', 'anand@123', 'travel/images/bg-smart-home-2.jpg', 'travel/certificate/bg-smart-home-2.jpg', 'Accepted'),
(15, 'sriman', 'ASSD6454A', 'prakasam', 6300537678, 'srimannarayanabiruraju96010@gmail.com', 'sriman4787', 'travel/images/home-decor-2.jpg', 'travel/certificate/home-decor-1.jpg', 'Rejected'),
(16, 'sriman', 'ASDF1234H', 'prakasam', 6300537678, 'srimannarayanabiruduraju96010@gmail.com', 'sriman4787', 'travel/images/ivancik.jpg', 'travel/certificate/product-12.jpg', 'Accepted'),
(17, 'saddam', 'ASDE0987Q', 'hyderabad', 9573970379, 'saddamoddin18@gmail.com', 'Saddam@18', 'travel/images/cars1_SOqWd09.jpg', 'travel/certificate/team-2.jpg', 'Accepted'),
(18, 'surya', 'ASDF4567Q', 'hyderabad', 8919134556, 'suryaanand975@yahoo.com', 'Anand@123', 'travel/images/cars_feyJFOt.jpg', 'travel/certificate/bg-smart-home-2_eVy2ITJ.jpg', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `user_id` int(11) NOT NULL,
  `user_name` longtext NOT NULL,
  `user_lastname` longtext NOT NULL,
  `user_phone` bigint(20) NOT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_pwd` varchar(100) NOT NULL,
  `user_photo` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `user_lastname`, `user_phone`, `user_email`, `user_pwd`, `user_photo`) VALUES
(1, 'suryaanand', 'nadendla', 8919134556, 'suryaanand456@gmail.com', 'Anand@123', 'user/images/team-4.jpg'),
(33, 'anand', 'Nadendla', 9989228601, 'suryaanand975@gmail.com', '', 'user/images/bruce-mars.jpg'),
(34, 'suryaanandN', 'Nadendla', 855645852, 'anand123@gmail.com', 'Anand@123', 'user/images/bruce-mars.jpg'),
(35, 'sri', 'raju', 6300537678, 'srimannarayanabiruburaju96010@gmail.com', 'Sriman4787', 'user/images/bruce-mars.jpg'),
(36, 'surya', 'anand', 8919134556, 'surya123@gmail.com', 'Anand@123', 'user/images/bruce-mars.jpg'),
(62, 'surya', 'Nadendla', 8919134556, 'anand456@gmail.com', 'Anand@123', 'user/images/bruce-mars.jpg'),
(63, 'surya', 'nadendla', 9393055901, 'srivani@gmail.com', 'Anand@123', 'user/images/drake.jpg'),
(64, 'sri', 'nadendlka', 6305598758, 'sri@123gmail.com', 'Anand@123', 'user/images/ivana-squares.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user_feedback`
--

CREATE TABLE `user_feedback` (
  `fb_id` int(11) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `hotel_id` varchar(50) DEFAULT NULL,
  `comments` longtext NOT NULL,
  `agency_id` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_feedback`
--

INSERT INTO `user_feedback` (`fb_id`, `rating`, `hotel_id`, `comments`, `agency_id`, `email`) VALUES
(1, 'average', '35', 'emmo', '', NULL),
(2, 'bad', NULL, 'emoo', '10', NULL),
(3, 'very Good', '38', 'very nice', NULL, NULL),
(4, 'good', '35', 'surya', NULL, 'suryaanand456@gmail.com'),
(5, 'good', '35', 'surya', NULL, 'suryaanand456@gmail.com'),
(6, 'good', '35', 'demo', NULL, 'suryaanand456@gmail.com'),
(7, 'good', '35', 'demo', NULL, 'suryaanand456@gmail.com'),
(8, 'very Good', '35', 'good', NULL, 'suryaanand456@gmail.com'),
(9, 'good', NULL, 'guntur', '10', 'suryaanand456@gmail.com'),
(10, 'very Good', NULL, 'hyderabad', '10', 'suryaanand456@gmail.com'),
(11, 'very Good', '35', 'surya surya surya', NULL, 'anand123@gmail.com'),
(12, 'good', '35', 'demoooooooo', NULL, 'anand123@gmail.com'),
(13, 'good', NULL, 'surya demooo', '10', 'anand123@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `booking_car_details`
--
ALTER TABLE `booking_car_details`
  ADD PRIMARY KEY (`car_booking_id`);

--
-- Indexes for table `booking_cruises_details`
--
ALTER TABLE `booking_cruises_details`
  ADD PRIMARY KEY (`cruises_booking_id`);

--
-- Indexes for table `booking_flight_details`
--
ALTER TABLE `booking_flight_details`
  ADD PRIMARY KEY (`flight_booking_id`);

--
-- Indexes for table `booking_room_details`
--
ALTER TABLE `booking_room_details`
  ADD PRIMARY KEY (`booking_id`);

--
-- Indexes for table `car_dashboard`
--
ALTER TABLE `car_dashboard`
  ADD PRIMARY KEY (`car_id`);

--
-- Indexes for table `cruises_dashboard`
--
ALTER TABLE `cruises_dashboard`
  ADD PRIMARY KEY (`cruises_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `flight_dashboard`
--
ALTER TABLE `flight_dashboard`
  ADD PRIMARY KEY (`flight_id`);

--
-- Indexes for table `hotel_dashboard`
--
ALTER TABLE `hotel_dashboard`
  ADD PRIMARY KEY (`room_id`);

--
-- Indexes for table `hotel_details`
--
ALTER TABLE `hotel_details`
  ADD PRIMARY KEY (`hotel_id`);

--
-- Indexes for table `travel_details`
--
ALTER TABLE `travel_details`
  ADD PRIMARY KEY (`agency_id`);

--
-- Indexes for table `user_details`
--
ALTER TABLE `user_details`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_feedback`
--
ALTER TABLE `user_feedback`
  ADD PRIMARY KEY (`fb_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking_car_details`
--
ALTER TABLE `booking_car_details`
  MODIFY `car_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `booking_cruises_details`
--
ALTER TABLE `booking_cruises_details`
  MODIFY `cruises_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `booking_flight_details`
--
ALTER TABLE `booking_flight_details`
  MODIFY `flight_booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `booking_room_details`
--
ALTER TABLE `booking_room_details`
  MODIFY `booking_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `car_dashboard`
--
ALTER TABLE `car_dashboard`
  MODIFY `car_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `cruises_dashboard`
--
ALTER TABLE `cruises_dashboard`
  MODIFY `cruises_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `flight_dashboard`
--
ALTER TABLE `flight_dashboard`
  MODIFY `flight_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `hotel_dashboard`
--
ALTER TABLE `hotel_dashboard`
  MODIFY `room_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `hotel_details`
--
ALTER TABLE `hotel_details`
  MODIFY `hotel_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `travel_details`
--
ALTER TABLE `travel_details`
  MODIFY `agency_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `user_details`
--
ALTER TABLE `user_details`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `user_feedback`
--
ALTER TABLE `user_feedback`
  MODIFY `fb_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
