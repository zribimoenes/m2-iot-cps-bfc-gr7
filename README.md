# Projet de Sécurité des Véhicules à la Porte du Bateau

Bienvenue dans le dépôt du projet de sécurité des véhicules à la porte du bateau. Ce projet utilise l'ESP32, le Raspberry Pi, l'Arduino, et des codes QR pour garantir la sécurité. Les composants principaux et leurs rôles sont décrits ci-dessous.

## Contenu du Projet

1. **Code ESP32**

   Assure la sécurité à la porte du bateau en maintenant la communication avec le Raspberry Pi via MQTT. La barrière reste fermée et les données des capteurs sont transmises à l'interface.

2. **Code Raspberry Pi**

   Communique avec l'ESP32 via MQTT pour maintenir la barrière fermée et collecte les données des capteurs. Envoie des requêtes HTTP pour récupérer les données des voyageurs de la base de données. En cas de défaillance, peut être commandé par le serveur web via MQTT.

3. **Code Arduino**

   Contribue au fonctionnement global du système, bien que sa fonction spécifique ne soit pas détaillée ici.

4. **Code QR Code**

   Partie intégrante du système pour l'identification et le suivi des voyageurs.

## Fonctionnement du Système

- **Communication MQTT :** L'ESP32 communique avec le Raspberry Pi via MQTT pour maintenir la barrière fermée et partager les données des capteurs.

- **Requêtes HTTP :** Le Raspberry Pi envoie des requêtes HTTP pour récupérer les données des voyageurs stockées dans la base de données et interagit avec le serveur web pour l'enregistrement d'états système.

- **Serveur Web :** Collecte les données du Raspberry Pi via MQTT et interagit avec la base de données. Peut commander le Raspberry Pi en cas de défaillance.

## Configuration du Projet

Suivez les instructions d'installation pour chaque composant du projet. Pour plus de détails, référez-vous aux fichiers de code dans ce dépôt.

## Licence

Ce projet est sous licence [insérer la licence appropriée ici, par exemple, MIT License]. Consultez le fichier `LICENSE` pour plus de détails.

Nous vous remercions de votre intérêt pour notre projet. Pour des questions ou des commentaires, n'hésitez pas à nous contacter.
