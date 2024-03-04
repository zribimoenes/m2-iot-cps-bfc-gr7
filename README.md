# Projet de Sécurité des Véhicules à la Porte du Bateau

Bienvenue dans le dépôt du projet de sécurité des véhicules à la porte du bateau. Ce projet utilise l'ESP32, le Raspberry Pi, l'Arduino, des codes QR, et Node-RED pour garantir la sécurité. Les composants principaux et leurs rôles sont décrits ci-dessous.

## Contenu du Projet

1. **Code ESP32**

   Assure la sécurité à la porte du bateau en maintenant la communication avec le Raspberry Pi via MQTT. La barrière reste fermée et les données des capteurs sont transmises à l'interface.

2. **Code Raspberry Pi**

   Communique avec l'ESP32 via MQTT pour maintenir la barrière fermée et collecte les données des capteurs. Envoie des requêtes HTTP pour récupérer les données des voyageurs de la base de données. En cas de défaillance, peut être commandé par le serveur web via MQTT.

3. **Code Arduino**

   Contribue au fonctionnement global du système, bien que sa fonction spécifique ne soit pas détaillée ici.

4. **Code QR Code**

   Partie intégrante du système pour l'identification et le suivi des voyageurs.

5. **Node-RED (Orchestration et Dashbording)**

   Node-RED est utilisé pour orchestrer le flux d'informations entre les composants du système. Il facilite également la création de tableaux de bord (dashboards) pour une surveillance visuelle.

## Fonctionnement du Système

- **Communication MQTT :** L'ESP32 communique avec le Raspberry Pi via MQTT pour maintenir la barrière fermée et partager les données des capteurs.

- **Requêtes HTTP :** Le Raspberry Pi envoie des requêtes HTTP pour récupérer les données des voyageurs stockées dans la base de données et interagit avec le serveur web pour l'enregistrement d'états système.

- **Node-RED (Orchestration) :** Node-RED orchestre le flux d'informations entre l'ESP32, le Raspberry Pi, et les autres composants pour assurer une communication fluide.

- **Node-RED (Dashboards) :** Utilisation de Node-RED pour créer des tableaux de bord visuels permettant une surveillance en temps réel du système.

## Configuration du Projet

Suivez les instructions d'installation pour chaque composant du projet. Pour plus de détails, référez-vous aux fichiers de code dans ce dépôt.


