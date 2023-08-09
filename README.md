# OC P4 : Développer un programme logiciel en utilisant Python

## Gestion de tournoi d'échecs

<!-- TOC -->
* [Installation](#installation)
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
Gestion des joueurs --> Afficher tous les joueurs

#### liste de tous les tournois


### Rapport flake8 
Un rapport flake8 est présent dans le répertoire src/flake8_rapport
Vous pouvez en générer un nouveau avec la commande suivante depuis le répertoire src : 
```shell
flake8
```
La configuration est présente dans le fichier .flake8. 
