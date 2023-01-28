# JTasks
**************************Jtask************************** est une CLI app (Application en ligne de commande). 

Cet mini programme vous servira à gérer vos taches du quotidien plus rapidement et plus efficacement directement dans un terminal sous Windows, Linux, Mac etc…

**Fonctionnalités** 
Avec cet outil vous aurez:

- Un système de gestion de données avec le format **json**
- La possibilité d'ajouter une tache (en spécifiant la description, la priorité et une catégorie)
- La possibilité supprimer une tache
- La possibilité de modifier l'état d'une tâches (fait/à faire)
- Un système de priorité sur chaque tâche enregistré, matérialisée par un entier (1≤entier≤3). Un tâche peut donc avoir une priorité la plus élevé (1) ou le moins élevé (3) ou encore une priorité intermédiaire (2).
- Un sytème de catégorie sur les tâches.
- La possibilité de visionner la liste des tâches déjà enregistrée (avec un système de filtre)

**Installation** 

<aside>
💡 Notez que la méthode d’installation proposée est celle qui marche pour Windows. Alors n’hésitez pas à faire quelques recherches pour trouver l’équivalent si vous êtes sur un autre système.

</aside>

Pour récupérer le projet chez vous et l’utiliser, rien de plus simple.

- D’abord vous devez ouvrir un nouveau terminal
- Cloner le repo chez vous avec la syntaxe:
    
    ```bash
    git clone <lien du repo>
    ```
    
- Un nouveau dossier sera créé dans le répertoire courant (Jtask). Rendez-vous à l’intérieur avec la syntaxe:
    
    ```bash
    cd .\Jtask
    ```
    
- Créer un nouvel environnement virtuel python
    
    ```bash
    python -m venv env
    ```
    
- Activer l’environnement virtuel
    
    ```bash
    .\env\Script\activate
    ```
    
- Installer les dépendances
    
    ```bash
    pip install -r requirements.txt
    ```
    

A cette étape vous êtes en mesure d’utiliser l’app comme bon vous semble.

Pour exécuter l’app retenez la syntaxe 

```bash
python -m jtask <commande>
```

Visionner les possibilités d’utilisation qui s’offre à vous, notamment la liste des commandes et options disponible en accédant à l’interface d’aide 

```bash
python -m jtask --help
```

Avant tout manipulation assurez-vous d’exécuter la commande <init>

```bash
python -m jtask init 
```

Cette commande initialisera les paramètres par défaut de l’app et crée automatiquement  une mini base de donnée au format json.

**Exemple d’utilisation**

- initialisation
    
    ```bash
    python -m jtask init 
    ```
    
- Ajouter une tache (utilisez la commande add)
    
    ```bash
    python -m jtask add <description> 
    ```
    
- Voir la liste des taches déjà enregistrées (commande list)
    
    ```bash
    python -m jtask list
    ```
    

<aside>
💡 Notez qu’une commande pourrait avoir à lui des sous-commandes et sous-options. N’hésitez pas accéder à l’interface d’aide des commandes en mettant l’option « --help » devant.
</aside>

