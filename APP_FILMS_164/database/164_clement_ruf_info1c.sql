DROP DATABASE IF EXISTS 164_clement_ruf_info1c;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS 164_clement_ruf_info1c;

-- Utilisation de cette base de donnée

USE 164_clement_ruf_info1c;
-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Client :  localhost
-- Généré le :  Mar 31 Mai 2022 à 08:11
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
  `prix_marchandise` varchar(78) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `t_adresse`
--

CREATE TABLE `t_adresse` (
  `id_adresse` int(11) NOT NULL,
  `ville_adresse` varchar(78) DEFAULT NULL,
  `batiment_adresse` varchar(78) DEFAULT NULL,
  `personne_adresse` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_adresse`
--

INSERT INTO `t_adresse` (`id_adresse`, `ville_adresse`, `batiment_adresse`, `personne_adresse`) VALUES
(1, 'Morges', 'Avenue du bus 23', 'Clément Ruf'),
(2, 'Morges', 'Avenue du léopard 5', 'Arthur Ruf'),
(3, 'Morges', 'Avenue du tala 7', 'Nolan Kusner'),
(4, 'Morges', 'Avenue du fils 4', 'Olivier Maccaud'),
(5, 'Morges', 'Avenue du francois 5', 'Corentin Hussain'),
(6, 'Morges', 'Avenue du bili 8', 'Pinacoco Pinacolada'),
(7, 'Konoha', 'Avenue du pors 2', 'Lavache Quirit'),
(8, 'Konoha', 'Avenue du cri 30', 'Will Smith'),
(9, 'Konoha', 'Avenue du rat 1', 'Tom Holland'),
(10, 'Konoha', 'Avenue du rat 2', 'Tony Stark'),
(11, 'Konoha', 'Avenue du gang 67', 'Thanos leBG'),
(12, 'Crissier', 'Avenue du singe 5', 'Macron Emmanuel'),
(13, 'Crissier', 'Avenue du poulet 8', 'Bigard Boitbeaucoup'),
(14, 'Crissier', 'Avenue du dindon 2', 'Madara Uchiha'),
(15, 'Crissier', 'Avenue du ricard 7', 'Jean Némar'),
(16, 'Logiville', 'Avenue du logitec 11', 'Logitec'),
(17, 'Digiville', 'Avenue du digitec 12', 'Digitec'),
(18, 'test', NULL, NULL);

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
  `nom_fournisseur` varchar(78) DEFAULT NULL,
  `objet_fournisseur` varchar(78) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_fournisseur`
--

INSERT INTO `t_fournisseur` (`id_fournisseur`, `nom_fournisseur`, `objet_fournisseur`) VALUES
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
  `mail_mail` varchar(150) DEFAULT NULL,
  `personne_mail` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_mail`
--

INSERT INTO `t_mail` (`id_mail`, `mail_mail`, `personne_mail`) VALUES
(1, 'palalalalala@gmail.com', 'Clément Ruf'),
(2, 'floray@gmail.com', 'Arthur Ruf'),
(3, 'lalilo@gmail.com', 'Nolan Kusner'),
(4, 'asdasdasd@gmail.com', 'Olivier Maccaud'),
(5, 'sdgwertgewrg@gmail.com', 'Corentin Hussain'),
(6, 'dsfgsdusdfz@gmail.com', 'Pinacoco Pinacolada'),
(7, 'merci@gmail.com', 'Lavache Quirit'),
(8, 'aurevoire@gmail.com', 'Will Smith'),
(9, 'poupipou@gmail.com', 'Tom Holland'),
(10, 'grrrrrrra@gmail.com', 'Tony Stark'),
(11, 'cortex@gmail.com', 'Thanos leBG'),
(12, 'squeezie@gmail.com', 'Macron Emmanuel'),
(13, 'gotaga@gmail.com', 'Bigard Boitbeaucoup'),
(14, 'mickalow@gmail.com', 'Madara Uchiha'),
(15, 'kameto@gmail.com', 'Jean Némar'),
(16, 'locklear@gmail.com', 'Digitec'),
(17, 'aiushfsludhfisaufddsafs@gmail.com', 'Logitec');

-- --------------------------------------------------------

--
-- Structure de la table `t_objet`
--

CREATE TABLE `t_objet` (
  `id_objet` int(11) NOT NULL,
  `nom_objet` varchar(78) DEFAULT NULL,
  `num_serie_objet` varchar(78) DEFAULT NULL,
  `nombre_objet` varchar(1000) DEFAULT NULL,
  `description_objet` varchar(600) DEFAULT NULL,
  `creation_objet` varchar(600) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_objet`
--

INSERT INTO `t_objet` (`id_objet`, `nom_objet`, `num_serie_objet`, `nombre_objet`, `description_objet`, `creation_objet`) VALUES
(1, 'Mannette Xbox', '210bd3', '1', 'Mannette de couleur rouge pour jouer a tout vos jeux sur Xbox ', '10 juin 1969'),
(2, 'Mannette Xbox', '210bsa6', '1', 'Mannette de couleur rouge pour jouer a tout vos jeux sur Xbox ', '10 juin 1969'),
(3, 'Mannette Xbox', '210bsu', '1', 'Mannette de couleur bleu pour jouer a tout vos jeux sur Xbox ', '10 juin 1969'),
(4, 'Mannette Xbox', '210bpo', '1', 'Mannette de couleur bleu pour jouer a tout vos jeux sur Xbox ', '10 juin 1969'),
(5, 'Mannette Xbox', '210b76', '1', 'Mannette de couleur bleu pour jouer a tout vos jeux sur Xbox ', '10 juin 1969'),
(6, 'Carte Cadeau PS4', 'jsjjsh3B', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console PS4', '32 mai 2890'),
(7, 'Carte Cadeau PS4', 'jsjjshae', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console PS4', '32 mai 2890'),
(8, 'Carte Cadeau PS4', 'jsjjshmb', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console PS4', '32 mai 2890'),
(9, 'Carte Cadeau PS4', 'jsjjshtg', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console PS4', '32 mai 2890'),
(10, 'Carte Cadeau PS4', 'jsjjshio', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console PS4', '32 mai 2890'),
(11, 'Carte cadeau Xbox', 'asjhdakhsdk6boa', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console xbox', '32 mai 2890'),
(12, 'Carte cadeau Xbox', 'asjhdakhsdkaiks', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console xbox', '32 mai 2890'),
(13, 'Carte cadeau Xbox', 'asjhdakhsdkdf', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console xbox', '32 mai 2890'),
(14, 'Carte cadeau Xbox', 'asjhdakhsdklp', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console xbox', '12 mai 2890'),
(15, 'Carte cadeau Xbox', 'asjhdakhsdk6b', '1', 'Carte cadeau d\'une valeur de 50 CHF pour tout console xbox', '12 mai 2890'),
(16, 'Enceinte', 'asjhdkahsdkah23', '1', 'Toujours envies d\'écouter de la musique ?\r\nCette enceint est faite pour car elle a Plus de 10 H d\'autonomie et se recharge en seulement 2 minute. \r\nOui nous vous arnaquons mais bon c\'est juste une enceint normale', '10 juin 1969'),
(17, 'Enceinte', 'asjhdkahsdkahop', '1', 'Toujours envies d\'écouter de la musique ?\r\nCette enceint est faite pour car elle a Plus de 10 H d\'autonomie et se recharge en seulement 2 minute. \r\nOui nous vous arnaquons mais bon c\'est juste une enceint normale', '6 novembre 489'),
(18, 'Enceinte', 'asjhdkahsdkahlaks', '1', 'Toujours envies d\'écouter de la musique ?\r\nCette enceint est faite pour car elle a Plus de 10 H d\'autonomie et se recharge en seulement 2 minute. \r\nOui nous vous arnaquons mais bon c\'est juste une enceint normale', '6 novembre 489'),
(19, 'Enceinte', 'asjhdkahsdkah23877', '1', 'Toujours envies d\'écouter de la musique ?\r\nCette enceint est faite pour car elle a Plus de 10 H d\'autonomie et se recharge en seulement 2 minute. \r\nOui nous vous arnaquons mais bon c\'est juste une enceint normale', '6 novembre 489'),
(20, 'Enceinte', 'asjhdkahsdksda', '1', 'Toujours envies d\'écouter de la musique ?\r\nCette enceint est faite pour car elle a Plus de 10 H d\'autonomie et se recharge en seulement 2 minute. \r\nOui nous vous arnaquons mais bon c\'est juste une enceint normale', '10 juin 1969'),
(21, 'Machine a café', 'lalalala', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '12 mai 2890'),
(22, 'Machine a café', 'lalalztuz', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '12 mai 2890'),
(23, 'Machine a café', 'lalalala29374', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '12 mai 2890'),
(24, 'Machine a café', 'lalalalaj98j', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '12 mai 2890'),
(25, 'Machine a café', 'lalalala002jjf', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '32 mai 2890'),
(26, 'Machine a café', 'lalalalakquwhe7', '1', 'Machine a café qui fait du café pour plus de 50 personne en meme temps. (c\'est faux chakal)', '10 juin 1969'),
(27, 'Multiprise', 'akquwhasu', '1', 'C\'est une multiprise basique :)', '32 mai 2008'),
(28, 'Multiprise', 'akquwhe7234', '1', 'C\'est une multiprise basique :)', '32 mai 2008'),
(29, 'Multiprise', 'akquwhe7brg', '1', 'C\'est une multiprise basique :)', '32 mai 2008'),
(30, 'Multiprise', 'akquwhe7sdfr5', '1', 'C\'est une multiprise basique :)', '32 mai 2008'),
(31, 'Multiprise', 'e7sdfr5erw34', '1', 'C\'est une multiprise basique :)', '32 mai 2008'),
(32, 'Clé USB', 'e7sdfr5345s', '1', '800 T disponible sur cette clé USB pour stocker tout vos vidéo préféré ;)', '32 mai 2008'),
(33, 'Clé USB', 'e7sdfr5fgh', '1', '800 T disponible sur cette clé USB pour stocker tout vos vidéo préféré ;)', '32 mai 2008'),
(34, 'Clé USB', 'e7sdfdsdf', '1', '800 T disponible sur cette clé USB pour stocker tout vos vidéo préféré ;)', '32 mai 2008'),
(35, 'Clé USB', 'e7sdfr5763hh3', '1', '800 T disponible sur cette clé USB pour stocker tout vos vidéo préféré ;)', '32 mai 2008'),
(36, 'Clé USB', 'r5763hh38efss', '1', '800 T disponible sur cette clé USB pour stocker tout vos vidéo préféré ;)', '32 mai 2008'),
(37, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r576qewqwe', '1', 'C\'est pas une carte son mais une carte graphique bg.', '32 mai 2008'),
(38, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r576323o', '1', 'C\'est pas une carte son mais une carte graphique bg.', '32 mai 2008'),
(39, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r5763hh3oiwerjh', '1', 'C\'est pas une carte son mais une carte graphique bg.', '32 mai 2008'),
(40, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'r5763hh3owhro', '1', 'C\'est pas une carte son mais une carte graphique bg.', '32 mai 2008'),
(41, 'Carte Graphique MSI GeForce GT 1030 AERO ITX 2GD4 OC', 'hh3ow34r', '1', 'C\'est pas une carte son mais une carte graphique bg.', '32 mai 2008'),
(42, 'Iphone 12', 'hh3owhrowsdfh', '1', 'Nouvelle IPhone de plus en plus chère juste pour avoir un téléphone avec 1 T qui sert a rien. ', '10 juin 1969'),
(43, 'Iphone 12', 'hh3owhro076', '1', 'Nouvelle IPhone de plus en plus chère juste pour avoir un téléphone avec 1 T qui sert a rien. ', '10 juin 1969'),
(44, 'Iphone 12', 'hh3owhro3658', '1', 'Nouvelle IPhone de plus en plus chère juste pour avoir un téléphone avec 1 T qui sert a rien. ', '10 juin 1969'),
(45, 'Iphone 12', 'hh3owhro02737', '1', 'Nouvelle IPhone de plus en plus chère juste pour avoir un téléphone avec 1 T qui sert a rien. ', '10 juin 1969'),
(46, 'Souris Logitech B100 Optical USB Mouse', '123198723', '1', 'Souris pour ordinateur et c\'est pas une souris qui mange du fromage.', '10 juin 1969'),
(47, 'Souris Logitech B100 Optical USB Mouse', '123198723iuh', '1', 'Souris pour ordinateur et c\'est pas une souris qui mange du fromage.', '10 juin 1969'),
(48, 'Souris Logitech B100 Optical USB Mouse', '1231987230987', '1', 'Souris pour ordinateur et c\'est pas une souris qui mange du fromage.', '6 novembre 489'),
(49, 'Souris Logitech B100 Optical USB Mouse', '123198723ikdsk', '1', 'Souris pour ordinateur et c\'est pas une souris qui mange du fromage.', '6 novembre 489'),
(50, 'Souris Logitech B100 Optical USB Mouse', '123198723qas', '1', 'Souris pour ordinateur et c\'est pas une souris qui mange du fromage.', '6 novembre 489'),
(51, 'Ecran LG 27" LED - UltraGear 27GP850-B', '123198723uh', '1', 'Ecran absolument incroyable avec plus de 10 pixel. 10 Image par seconde. ACHETER MTN !!!', '12 mai 2890'),
(52, 'Ecran LG 27" LED - UltraGear 27GP850-B', '123198723dtd', '1', 'Ecran absolument incroyable avec plus de 10 pixel. 10 Image par seconde. ACHETER MTN !!!', '12 mai 2890'),
(53, 'Ecran LG 27" LED - UltraGear 27GP850-B', '1231987230as9jd', '1', 'Ecran absolument incroyable avec plus de 10 pixel. 10 Image par seconde. ACHETER MTN !!!', '12 mai 2890'),
(54, 'Ecran LG 27" LED - UltraGear 27GP850-B', '87230as9jdoij', '1', 'Ecran absolument incroyable avec plus de 10 pixel. 10 Image par seconde. ACHETER MTN !!!', '12 mai 2890'),
(55, 'Ecran LG 27" LED - UltraGear 27GP850-B', '87230as9jdwsf', '1', 'Ecran absolument incroyable avec plus de 10 pixel. 10 Image par seconde. ACHETER MTN !!!', '12 mai 2890'),
(56, 'PC Thinkpas-X1', '87230as9jd980z', '1', 'PC portable comme une fusée', '10 juin 1969'),
(57, 'PC Thinkpas-X1', '87230as9jdedwsa', '1', 'PC portable comme une fusée', '10 juin 1969'),
(58, 'PC Thinkpas-X1', '87230as9jd8uza9sd', '1', 'PC portable comme une fusée', '10 juin 1969'),
(59, 'PC Thinkpas-X1', '87230as9jdasd', '1', 'PC portable comme une fusée', '10 juin 1969'),
(60, 'PC Thinkpas-X1', '87230as9jdgtgt', '1', 'PC portable comme une fusée', '10 juin 1969'),
(61, 'Chargeur USB-C', '87230as9jd9273z4', '1', 'Chargeur de nationalité USB de type traditionnellement C', '12 mai 2890'),
(62, 'Chargeur USB-C', '87230as9jdbjbdska', '1', 'Chargeur de nationalité USB de type traditionnellement C', '12 mai 2890'),
(63, 'Chargeur USB-C', 'jbdskaw98eh', '1', 'Chargeur de nationalité USB de type traditionnellement C', '12 mai 2890'),
(64, 'Chargeur USB-C', 'jbdska08hwse', '1', 'Chargeur de nationalité USB de type traditionnellement C', '12 mai 2890'),
(65, 'Chargeur Iphone', 'jbdskaweruh', '1', 'Faite des chargeur USB-c', '12 mai 2890'),
(66, 'Chargeur Iphone', 'jbdskaw4r', '1', 'Faite des chargeur USB-c', '12 mai 2890'),
(67, 'Chargeur Iphone', 'jbdskaw4thh', '1', 'Faite des chargeur USB-c', '12 mai 2890'),
(68, 'Chargeur Iphone', 'aw4thhjtzu', '1', 'Faite des chargeur USB-c', '12 mai 2890'),
(69, 'Chargeur Iphone', 'aw4thhjtr6uj', '1', 'Faite des chargeur USB-c', '12 mai 2890'),
(70, 'cable RJ-45', 'aw4thhsef', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2008'),
(71, 'cable RJ-45', 'aw4thhk798i', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2890'),
(72, 'cable RJ-45', 'aw4thhsssa', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2890'),
(73, 'cable RJ-45', 'hhsssa3546', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2890'),
(74, 'cable RJ-45', 'hhsssasdfr', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2890'),
(75, 'cable RJ-45', 'hhsssau465', '1', 'Cable pour une connexion internet qui vous permutera d\'avoir le même niveau que Gotaga ', '32 mai 2890'),
(76, 'test01', '', '1', 'wow le test 01 fonctionne c\'est incroyable', '2029-06-22'),
(77, 'test02', 'asd', '4', 'sdasdadasdad', '2022-05-17'),
(78, 'test03', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `t_personne`
--

CREATE TABLE `t_personne` (
  `id_personne` int(78) NOT NULL,
  `nom_personne` varchar(78) DEFAULT NULL,
  `prenom_personne` varchar(78) DEFAULT NULL,
  `moral_personne` varchar(78) DEFAULT NULL,
  `physique_personne` varchar(78) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_personne`
--

INSERT INTO `t_personne` (`id_personne`, `nom_personne`, `prenom_personne`, `moral_personne`, `physique_personne`) VALUES
(1, 'Ruf ', 'Clément', '-', 'Patron'),
(2, 'Ruf', 'Arthur', '-', 'Employer'),
(3, 'Kusner', 'Nolan', '-', 'Employer'),
(4, 'Maccaud', 'Olivier', '-', 'Employer'),
(5, 'Hussain', 'Corentin', '-', 'Client'),
(6, 'Pinacolada', 'Pinacoco', 'Pepsi', '-'),
(7, 'Quirit', 'Lavache', '-', 'Client'),
(8, 'Smith', 'Will', '-', 'Client'),
(9, 'Holland', 'Tom', '-', 'Client'),
(10, 'Stark', 'Tony', '-', 'Client'),
(11, 'Lebg', 'Thanos', '-', 'Client'),
(12, 'Macron', 'Emmanuel', '-', 'Client'),
(13, 'boitbeaucoup', 'bigard', 'heineken', '-'),
(14, 'Uchiha', 'Madara', '-', 'Client'),
(15, 'Némar', 'Jean', 'Migros', '-');

-- --------------------------------------------------------

--
-- Structure de la table `t_tel`
--

CREATE TABLE `t_tel` (
  `id_tel` int(11) NOT NULL,
  `numero_tel` varchar(78) DEFAULT NULL,
  `prenom_tel` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `t_tel`
--

INSERT INTO `t_tel` (`id_tel`, `numero_tel`, `prenom_tel`) VALUES
(1, '079 111 11 11', 'Clément Ruf'),
(2, '079 111 11 22', 'Arthur Ruf'),
(3, '079 111 11 33', 'Nolan Kusner'),
(4, '079 111 11 44', 'Olivier Maccaud'),
(5, '079 111 11 55', 'Corentin Hussain'),
(6, '079 111 11 66', 'Pinacoco Pinacolada'),
(7, '079 111 11 77', 'Lavache Quirit'),
(8, '079 111 11 88', 'Will Smith'),
(9, '079 111 11 88', 'Tom Holland'),
(10, '079 111 11 99', 'Tony Stark'),
(11, '079 111 12 75', 'Thanos leBG'),
(12, '079 111 21 21', 'Macron Emmanuel'),
(13, '079 111 11 96', 'Bigard Boitbeaucoup'),
(14, '079 111 11 56', 'Madara Uchiha'),
(15, '079 111 11 29', 'Jean Némar');

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
  `prix_vendre` varchar(78) DEFAULT NULL,
  `point_fidélité_vendre` varchar(78) DEFAULT NULL
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
  MODIFY `id_adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
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
  MODIFY `id_objet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
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
