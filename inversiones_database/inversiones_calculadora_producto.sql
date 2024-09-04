-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: localhost    Database: inversiones
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `calculadora_producto`
--

DROP TABLE IF EXISTS `calculadora_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calculadora_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `dias_operativos_in` int NOT NULL,
  `dias_operativos_out` int NOT NULL,
  `dias_reinversion_in` int NOT NULL,
  `dias_reinversion_out` int NOT NULL,
  `hora_operativa` time(6) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calculadora_producto`
--

LOCK TABLES `calculadora_producto` WRITE;
/*!40000 ALTER TABLE `calculadora_producto` DISABLE KEYS */;
INSERT INTO `calculadora_producto` VALUES (1,'Plazo Fijo a 30 días',2,1,1,1,'09:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(2,'Certificado de Depósito 90 días',3,2,2,2,'10:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(3,'Fondo Mutuo Conservador',1,1,1,1,'14:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(4,'Letras del Tesoro a 180 días',3,3,0,0,'11:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(5,'Bono Corporativo a 1 año',5,5,0,0,'12:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(6,'Depósito a Plazo a 60 días',2,1,1,1,'09:30:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(7,'Fondo de Inversión Agresivo',1,2,2,2,'15:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(8,'Acciones Preferentes',3,3,0,0,'13:00:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(9,'Pagaré Bancario a 90 días',2,2,1,1,'10:30:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000'),(10,'Obligación Subordinada a 2 años',4,4,0,0,'11:30:00.000000','2024-09-01 08:58:21.000000','2024-09-01 08:58:21.000000');
/*!40000 ALTER TABLE `calculadora_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-01 14:09:56
