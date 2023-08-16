# OC P4 : Développer un programme logiciel en utilisant Python

## Gestion de tournoi d'échecs

<!-- TOC -->
* [OC P4 : Développer un programme logiciel en utilisant Python](#oc-p4--dvelopper-un-programme-logiciel-en-utilisant-python)
  * [Gestion de tournoi d'échecs](#gestion-de-tournoi-dchecs)
    * [Installation](#installation)
    * [Démarrer le projet](#d%C3%A9marrer-le-projet)
    * [Utilisation](#utilisation)
      * [Créer un joueur](#crer-un-joueur)
      * [Créer un nouveau tournoi](#crer-un-nouveau-tournoi)
      * [Démarrer un tournoi](#dmarrer-un-tournoi)
    * [Rapport](#rapport)
      * [Liste de tous les joueurs par ordre alphabétique](#liste-de-tous-les-joueurs-par-ordre-alphabtique)
      * [Liste de tous les tournois](#liste-de-tous-les-tournois)
      * [Nom et dates d'un tournoi](#nom-et-dates-dun-tournoi)
      * [Liste des joueurs du tournoi](#liste-des-joueurs-du-tournoi)
      * [Liste des tours et liste des matchs d'un tour](#liste-des-tours-et-liste-des-matchs-dun-tour)
    * [Rapport flake8](#rapport-flake8)
<!-- TOC -->

### Installation 
Pour lancer le projet, veuillez suivre les étapes suivantes : 
* Cloner le répertoire, naviguer dedans et créer le venv : 
```shell
git clone https://github.com/Masuchotabe/OC_Projet4.git
cd OC_Projet4/src
python -m venv venv
```
* Activer le venv selon votre OS : 
Linux
```shell
source venv/bin/activate
```
Windows 
```shell
.\venv\Scripts\Activate
```
* Installer les requirements 
```shell
python -m pip install -r requirements.txt
```

### Démarrer le projet 
Après l'installation, vous pouvez démarrer le projet 
avec la commande : 
```shell
python main.py
```

### Utilisation
#### Créer un joueur
Pour créer un nouveau joueur, il faut aller dans la gestion des joueurs puis "Créer un joueur"
Si des erreurs apparaissent dans les données renseignées, le joueur ne sera pas créer. Il faudra recommencer. 

#### Créer un nouveau tournoi 
Pour créer un nouveau tournoi, il faut aller dans la gestion des tournois puis "Créer un tournoi".
Si des erreurs apparaissent dans les données renseignées, le tournoi ne sera pas créer. Il faudra recommencer. 

#### Démarrer un tournoi
Pour démarrer un tournoi, il faut lui ajouter des joueurs. Pour cela, aller dans "Gérer un tournoi", 
sélectionnez le tournoi souhaité. Ensuite, vous pouvez ajouter des joueurs via son Identifiant national d'échecs. 
Par défaut, le premier joueur de la liste est sélectionné.

Après avoir ajouté les joueurs, vous pouvez démarrer le tournoi. Le premier tour est généré automatiquement et affiché. 

Vous pouvez ensuite renseigner les résultats du tour en cours, match par match. 

Lorsque tous les matchs ont été renseignés, vous pouvez générer le tour suivant, jusqu'à la fin du tournoi. 

### Rapport 
#### Liste de tous les joueurs par ordre alphabétique
"Gestion des joueurs" --> "Afficher tous les joueurs"

#### Liste de tous les tournois
"Gestion des tournois" --> "Afficher tous les tournois"

#### Nom et dates d'un tournoi
"Gestion des tournois" --> "Afficher tous les tournois". 
Les dates de début de fin sont affichées dans la liste. 

#### Liste des joueurs du tournoi
"Gestion des tournois" --> "Gérer un tournoi"
Choisissez le tournoi souhaité puis sélectionnez "Voir la liste des joueurs"

#### Liste des tours et liste des matchs d'un tour
"Gestion des tournois" --> "Gérer un tournoi"
Choisissez le tournoi souhaité (en cours ou terminé) puis sélectionnez "Voir la liste des tours"
pour avoir la liste des tours. 
Pour les matchs, il suffit de sélectionner "Voir les matchs d'un tour" et de choisir le tour. 

### Rapport flake8 
Un rapport flake8 est présent dans le répertoire src/flake8_rapport. 
Vous pouvez en générer un nouveau avec la commande suivante depuis le répertoire src : 
```shell
flake8
```
La configuration est présente dans le fichier .flake8. 
