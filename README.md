# Unraid ME - Bot Discord

Unraid ME est un bot Discord simple conçu pour aider les administrateurs de serveur à nettoyer rapidement les salons textuels créés lors d'un "raid". Il fournit une commande pour supprimer tous les salons correspondant à un nom spécifique.

## Fonctionnalités

- **`!unraid`**: Parcourt tous les salons du serveur et supprime ceux dont le nom correspond à celui configuré dans le code. Un rapport détaillé est ensuite envoyé en message privé à l'utilisateur ayant exécuté la commande.
- **`!ping`**: Affiche la latence actuelle du bot.

## Prérequis

- Python 3.8 ou supérieur
- Un compte de bot Discord et son token.

## Installation

1.  **Clonez ce dépôt :**
    ```bash
    git clone https://github.com/votre-utilisateur/unraid-me.git
    cd unraid-me
    ```

2.  **Installez les dépendances :**
    Il est recommandé d'utiliser un environnement virtuel.
    ```bash
    # Créez un environnement virtuel (optionnel mais recommandé)
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate

    # Installez les paquets nécessaires
    pip install -r requirements.txt
    ```

3.  **Configuration :**

    a. **Le Token du Bot :**
    Remplacez la dans la variable dans le fichier main
    je vous conseille de supprimer le bot après son utilisation pour pas qu'il devienne lui-même un bot de raid ( rique de partage du token )

    b. **Nom du salon à supprimer :**
    Dans le fichier `main.py`, modifiez la ligne suivante dans la commande `!unraid` pour cibler le nom de salon désiré (insensible à la casse) :

    ```python
    if channel.name.lower() == 'nom-du-salon-a-supprimer':
    ```

4.  **Lancez le bot :**
    ```bash
    python main.py
    ```

## Permissions

### Permissions du Bot
Pour que le bot puisse supprimer des salons, il a besoin de la permission **"Gérer les salons"** sur votre serveur Discord. Invitez-le avec les permissions adéquates.

### Permissions de la Commande
Par défaut, la commande `!unraid` peut être utilisée par n'importe qui. Pour des raisons de sécurité, il est **fortement recommandé** de la restreindre aux administrateurs. Pour ce faire, décommentez la ligne suivante dans `main.py` :

```python
# @bot.command(...)
@commands.has_permissions(administrator=True) # <-- Décommentez cette ligne
# async def unraid(...):
```

## Avertissement

⚠️ La commande `!unraid` est destructive et supprime des salons de manière permanente. Utilisez-la avec prudence et assurez-vous d'avoir bien configuré le nom du salon à supprimer.