--

-- Database: clement_ruf_info1c_vrai
-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS clement_ruf_info1c_vrai;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS clement_ruf_info1c_vrai;

-- Utilisation de cette base de donnée
-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mer 11 Mai 2022 à 11:54
-- Version du serveur :  5.7.11
-- Version de PHP :  5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `164_clement_ruf_info1c`
--

-- --------------------------------------------------------

--
-- Structure de la table `t_acheter_marchandise`
--

CREATE TABLE `t_acheter_marchandise` (
  `id_acheter_marchandise` int(11) NOT NULL,
  `fk_objet` int(11) NOT NULL,
  `fk_fournisseur` int(11) NOT NULL,
  `prix` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_adresse`
--

CREATE TABLE `t_adresse` (
  `id_adresse` int(11) NOT NULL,
  `ville` varchar(78) NOT NULL,
  `batiment` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_adresse`
--

INSERT INTO `t_adresse` (`id_adresse`, `ville`, `batiment`) VALUES
(1, 'Morges', 'Avenue du bus 23'),
(2, 'Morges', 'Avenue du léopard 5'),
(3, 'Morges', 'Avenue du tala 7'),
(4, 'Morges', 'Avenue du fils 4'),
(5, 'Morges', 'Avenue du francois 5'),
(6, 'Morges', 'Avenue du bili 8'),
(7, 'Konoha', 'Avenue du pors 2'),
(8, 'Konoha', 'Avenue du cri 30'),
(9, 'Konoha', 'Avenue du rat 1'),
(10, 'Konoha', 'Avenue du rat 2'),
(11, 'Konoha', 'Avenue du gang 67'),
(12, 'Crissier', 'Avenue du singe 5'),
(13, 'Crissier', 'Avenue du poulet 8'),
(14, 'Crissier', 'Avenue du dindon 2'),
(15, 'Crissier', 'Avenue du ricard 7'),
(16, 'Logiville', 'Avenue du logitec 11'),
(17, 'Digiville', 'Avenue du digitec 12');

-- --------------------------------------------------------

--
-- Structure de la table `t_avoir`
--

CREATE TABLE `t_avoir` (
  `id_avoir` int(11) NOT NULL,
  `fk_mail` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_fournisseur`
--

CREATE TABLE `t_fournisseur` (
  `id_fournisseur` int(11) NOT NULL,
  `nom` varchar(78) NOT NULL,
  `objet` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_fournisseur`
--

INSERT INTO `t_fournisseur` (`id_fournisseur`, `nom`, `objet`) VALUES
(1, 'Digitec', 'Mannette Xbox'),
(2, 'Logitec', 'Carte Cadeau PS4'),
(3, 'Digitec', 'Carte cadeau Xbox'),
(4, 'Digitec', 'Enceinte '),
(5, 'Digitec', 'Machine a café'),
(6, 'Digitec', 'Multiprise'),
(7, 'Digitec', 'Clé USB'),
(8, 'Digitec', 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC'),
(9, 'logitec', 'Iphone 12'),
(10, 'logitec', 'Souris Logitech B100 Optical USB Mouse'),
(11, 'logitec', 'Ecran LG 27" LED - UltraGear 27GP850-B'),
(12, 'logitec', 'PC Thinkpas-X1'),
(13, 'logitec', 'Chargeur USB-C'),
(14, 'logitec', 'Chargeur Iphone'),
(15, 'logitec', 'cable RJ-45');

-- --------------------------------------------------------

--
-- Structure de la table `t_habiter`
--

CREATE TABLE `t_habiter` (
  `id_habiter` int(11) NOT NULL,
  `fk_adresse` int(11) NOT NULL,
  `fk_fournisseur` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_mail`
--

CREATE TABLE `t_mail` (
  `id_mail` int(11) NOT NULL,
  `mail` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_mail`
--

INSERT INTO `t_mail` (`id_mail`, `mail`) VALUES
(1, 'logitec@gmail.com'),
(2, 'digitec@gmail.com'),
(3, 'lalilo@gmail.com'),
(4, 'asdasdasd@gmail.com'),
(5, 'sdgwertgewrg@gmail.com'),
(6, 'dsfgsdusdfz@gmail.com'),
(7, 'merci@gmail.com'),
(8, 'aurevoire@gmail.com'),
(9, 'poupipou@gmail.com'),
(10, 'grrrrrrra@gmail.com'),
(11, 'cortex@gmail.com'),
(12, 'squeezie@gmail.com'),
(13, 'gotaga@gmail.com'),
(14, 'mickalow@gmail.com'),
(15, 'kameto@gmail.com'),
(16, 'locklear@gmail.com'),
(17, 'aiushfsludhfisaufddsafs@gmail.com');

-- --------------------------------------------------------

--
-- Structure de la table `t_objet`
--

CREATE TABLE `t_objet` (
  `id_objet` int(11) NOT NULL,
  `nom` varchar(78) NOT NULL,
  `num_serie` varchar(78) NOT NULL,
  `nombre_objet` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_objet`
--

INSERT INTO `t_objet` (`id_objet`, `nom`, `num_serie`, `nombre_objet`) VALUES
(1, 'Mannette Xbox', '210bd3', '1'),
(2, 'Mannette Xbox', '210bsa6', '1'),
(3, 'Mannette Xbox', '210bsu', '1'),
(4, 'Mannette Xbox', '210bpo', '1'),
(5, 'Mannette Xbox', '210b76', '1'),
(6, 'Carte Cadeau PS4', 'jsjjsh3B', '1'),
(7, 'Carte Cadeau PS4', 'jsjjshae', '1'),
(8, 'Carte Cadeau PS4', 'jsjjshmb', '1'),
(9, 'Carte Cadeau PS4', 'jsjjshtg', '1'),
(10, 'Carte Cadeau PS4', 'jsjjshio', '1'),
(11, 'Carte cadeau Xbox', 'asjhdakhsdk6boa', '1'),
(12, 'Carte cadeau Xbox', 'asjhdakhsdkaiks', '1'),
(13, 'Carte cadeau Xbox', 'asjhdakhsdkdf', '1'),
(14, 'Carte cadeau Xbox', 'asjhdakhsdklp', '1'),
(15, 'Carte cadeau Xbox', 'asjhdakhsdk6b', '1'),
(16, 'Enceinte', 'asjhdkahsdkah23', '1'),
(17, 'Enceinte', 'asjhdkahsdkahop', '1'),
(18, 'Enceinte', 'asjhdkahsdkahlaks', '1'),
(19, 'Enceinte', 'asjhdkahsdkah23877', '1'),
(20, 'Enceinte', 'asjhdkahsdksda', '1'),
(21, 'Machine a café', 'lalalala', '1'),
(22, 'Machine a café', 'lalalztuz', '1'),
(23, 'Machine a café', 'lalalala29374', '1'),
(24, 'Machine a café', 'lalalalaj98j', '1'),
(25, 'Machine a café', 'lalalala002jjf', '1'),
(26, 'Machine a café', 'lalalalakquwhe7', '1'),
(27, 'Multiprise', 'akquwhasu', '1'),
(28, 'Multiprise', 'akquwhe7234', '1'),
(29, 'Multiprise', 'akquwhe7brg', '1'),
(30, 'Multiprise', 'akquwhe7sdfr5', '1'),
(31, 'Multiprise', 'e7sdfr5erw34', '1'),
(32, 'Clé USB', 'e7sdfr5345s', '1'),
(33, 'Clé USB', 'e7sdfr5fgh', '1'),
(34, 'Clé USB', 'e7sdfdsdf', '1'),
(35, 'Clé USB', 'e7sdfr5763hh3', '1'),
(36, 'Clé USB', 'r5763hh38efss', '1'),
(37, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r576qewqwe', '1'),
(38, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r576323o', '1'),
(39, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r5763hh3oiwerjh', '1'),
(40, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r5763hh3owhro', '1'),
(41, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'hh3ow34r', '1'),
(42, 'Iphone 12', 'hh3owhrowsdfh', '1'),
(43, 'Iphone 12', 'hh3owhro076', '1'),
(44, 'Iphone 12', 'hh3owhro3658', '1'),
(45, 'Iphone 12', 'hh3owhro02737', '1'),
(46, 'Souris Logitech B100 Optical USB Mouse', '123198723', '1'),
(47, 'Souris Logitech B100 Optical USB Mouse', '123198723iuh', '1'),
(48, 'Souris Logitech B100 Optical USB Mouse', '1231987230987', '1'),
(49, 'Souris Logitech B100 Optical USB Mouse', '123198723ikdsk', '1'),
(50, 'Souris Logitech B100 Optical USB Mouse', '123198723qas', '1'),
(51, 'Ecran LG 27" LED - UltraGear 27GP850-B', '123198723uh', '1'),
(52, 'Ecran LG 27" LED - UltraGear 27GP850-B', '123198723dtd', '1'),
(53, 'Ecran LG 27" LED - UltraGear 27GP850-B', '1231987230as9jd', '1'),
(54, 'Ecran LG 27" LED - UltraGear 27GP850-B', '87230as9jdoij', '1'),
(55, 'Ecran LG 27" LED - UltraGear 27GP850-B', '87230as9jdwsf', '1'),
(56, 'PC Thinkpas-X1', '87230as9jd980z', '1'),
(57, 'PC Thinkpas-X1', '87230as9jdedwsa', '1'),
(58, 'PC Thinkpas-X1', '87230as9jd8uza9sd', '1'),
(59, 'PC Thinkpas-X1', '87230as9jdasd', '1'),
(60, 'PC Thinkpas-X1', '87230as9jdgtgt', '1'),
(61, 'Chargeur USB-C', '87230as9jd9273z4', '1'),
(62, 'Chargeur USB-C', '87230as9jdbjbdska', '1'),
(63, 'Chargeur USB-C', 'jbdskaw98eh', '1'),
(64, 'Chargeur USB-C', 'jbdska08hwse', '1'),
(65, 'Chargeur Iphone', 'jbdskaweruh', '1'),
(66, 'Chargeur Iphone', 'jbdskaw4r', '1'),
(67, 'Chargeur Iphone', 'jbdskaw4thh', '1'),
(68, 'Chargeur Iphone', 'aw4thhjtzu', '1'),
(69, 'Chargeur Iphone', 'aw4thhjtr6uj', '1'),
(70, 'cable RJ-45', 'aw4thhsef', '1'),
(71, 'cable RJ-45', 'aw4thhk798i', '1'),
(72, 'cable RJ-45', 'aw4thhsssa', '1'),
(73, 'cable RJ-45', 'hhsssa3546', '1'),
(74, 'cable RJ-45', 'hhsssasdfr', '1'),
(75, 'cable RJ-45', 'hhsssau465', '1');

-- --------------------------------------------------------

--
-- Structure de la table `t_personne`
--

CREATE TABLE `t_personne` (
  `id_personne` int(78) NOT NULL,
  `nom` varchar(78) NOT NULL,
  `prenom` varchar(78) NOT NULL,
  `moral` varchar(78) NOT NULL,
  `physique` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_personne`
--

INSERT INTO `t_personne` (`id_personne`, `nom`, `prenom`, `moral`, `physique`) VALUES
(1, 'Ruf ', 'Clément', '', 'Patron'),
(2, 'Ruf', 'Arthur', '', 'Employer'),
(3, 'Kusner', 'Nolan', '', 'Employer'),
(4, 'Maccaud', 'Olivier', '', 'Employer'),
(5, 'Hussain', 'Corentin', '', 'Client'),
(6, 'Pinacolada', 'Pinacoco', 'Pepsi', ''),
(7, 'Quirit', 'Lavache', '', 'Client'),
(8, 'Smith', 'Will', '', 'Client'),
(9, 'Holland', 'Tom', '', 'Client'),
(10, 'Stark', 'Tony', '', 'Client'),
(11, 'Lebg', 'Thanos', '', 'Client'),
(12, 'Macron', 'Emmanuel', '', 'Client'),
(13, 'boitbeaucoup', 'bigard', 'heineken', ''),
(14, 'Uchiha', 'Madara', '', 'Client'),
(15, 'Némar', 'Jean', 'Migros', '');

-- --------------------------------------------------------

--
-- Structure de la table `t_tel`
--

CREATE TABLE `t_tel` (
  `id_tel` int(11) NOT NULL,
  `numero` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_tel`
--

INSERT INTO `t_tel` (`id_tel`, `numero`) VALUES
(1, '079 111 11 11'),
(2, '079 111 11 22'),
(3, '079 111 11 33'),
(4, '079 111 11 44'),
(5, '079 111 11 55'),
(6, '079 111 11 66'),
(7, '079 111 11 77'),
(8, '079 111 11 88'),
(9, '079 111 11 88'),
(10, '079 111 11 99'),
(11, '079 111 12 75'),
(12, '079 111 21 21'),
(13, '079 111 11 96'),
(14, '079 111 11 56'),
(15, '079 111 11 29');

-- --------------------------------------------------------

--
-- Structure de la table `t_telephoner`
--

CREATE TABLE `t_telephoner` (
  `id_telephoner` int(11) NOT NULL,
  `fk_tel` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `fk_fournisseur` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_vendre`
--

CREATE TABLE `t_vendre` (
  `id_vendre` int(11) NOT NULL,
  `fk_objet` int(11) NOT NULL,
  `fk_personne` int(11) NOT NULL,
  `prix` varchar(78) NOT NULL,
  `point_fidélité` varchar(78) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Index pour les tables exportées
--

--
-- Index pour la table `t_acheter_marchandise`
--
ALTER TABLE `t_acheter_marchandise`
  ADD PRIMARY KEY (`id_acheter_marchandise`),
  ADD KEY `fk_objet` (`fk_objet`),
  ADD KEY `fk_fournisseur` (`fk_fournisseur`);

--
-- Index pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  ADD PRIMARY KEY (`id_adresse`);

--
-- Index pour la table `t_avoir`
--
ALTER TABLE `t_avoir`
  ADD PRIMARY KEY (`id_avoir`),
  ADD KEY `fk_personne` (`fk_personne`),
  ADD KEY `fk_mail` (`fk_mail`);

--
-- Index pour la table `t_fournisseur`
--
ALTER TABLE `t_fournisseur`
  ADD PRIMARY KEY (`id_fournisseur`);

--
-- Index pour la table `t_habiter`
--
ALTER TABLE `t_habiter`
  ADD PRIMARY KEY (`id_habiter`),
  ADD KEY `fk_adresse` (`fk_adresse`),
  ADD KEY `fk_fournisseur` (`fk_fournisseur`),
  ADD KEY `fk_personne` (`fk_personne`);

--
-- Index pour la table `t_mail`
--
ALTER TABLE `t_mail`
  ADD PRIMARY KEY (`id_mail`);

--
-- Index pour la table `t_objet`
--
ALTER TABLE `t_objet`
  ADD PRIMARY KEY (`id_objet`);

--
-- Index pour la table `t_personne`
--
ALTER TABLE `t_personne`
  ADD PRIMARY KEY (`id_personne`);

--
-- Index pour la table `t_tel`
--
ALTER TABLE `t_tel`
  ADD PRIMARY KEY (`id_tel`);

--
-- Index pour la table `t_telephoner`
--
ALTER TABLE `t_telephoner`
  ADD PRIMARY KEY (`id_telephoner`);

--
-- Index pour la table `t_vendre`
--
ALTER TABLE `t_vendre`
  ADD PRIMARY KEY (`id_vendre`),
  ADD KEY `fk_objet` (`fk_objet`),
  ADD KEY `fk_personne` (`fk_personne`);

--
-- AUTO_INCREMENT pour les tables exportées
--

--
-- AUTO_INCREMENT pour la table `t_acheter_marchandise`
--
ALTER TABLE `t_acheter_marchandise`
  MODIFY `id_acheter_marchandise` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_adresse`
--
ALTER TABLE `t_adresse`
  MODIFY `id_adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT pour la table `t_avoir`
--
ALTER TABLE `t_avoir`
  MODIFY `id_avoir` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_fournisseur`
--
ALTER TABLE `t_fournisseur`
  MODIFY `id_fournisseur` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `t_habiter`
--
ALTER TABLE `t_habiter`
  MODIFY `id_habiter` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_mail`
--
ALTER TABLE `t_mail`
  MODIFY `id_mail` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT pour la table `t_objet`
--
ALTER TABLE `t_objet`
  MODIFY `id_objet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;
--
-- AUTO_INCREMENT pour la table `t_personne`
--
ALTER TABLE `t_personne`
  MODIFY `id_personne` int(78) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `t_tel`
--
ALTER TABLE `t_tel`
  MODIFY `id_tel` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
--
-- AUTO_INCREMENT pour la table `t_telephoner`
--
ALTER TABLE `t_telephoner`
  MODIFY `id_telephoner` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT pour la table `t_vendre`
--
ALTER TABLE `t_vendre`
  MODIFY `id_vendre` int(11) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
