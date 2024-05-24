# blockchain
Projet Blockchain en Python
Ce projet implémente une blockchain simple en Python. Chaque bloc contient un index, un horodatage, des données, le hachage du bloc précédent et son propre hachage. La blockchain prend en charge l'ajout de nouveaux blocs, la vérification de l'intégrité de la chaîne et la récupération de blocs spécifiques au format JSON.

Prérequis
Python 3.x
Installation
Clonez le dépôt (ou téléchargez les fichiers) et assurez-vous que vous avez Python 3 installé sur votre machine.

Utilisation
Initialisation et ajout de blocs :

python
# Créer une instance de la blockchain
blockchain = Blockchain()

# Ajout de blocs avec des données d'extrait de naissance (exemple de données)
blockchain.add_block({
    "Nom": "Dupont",
    "Prénom": "Jean",
    "Date de naissance": "01/01/1990",
    "Lieu de naissance": "Paris",
    "Nom des parents": "Dupont Pierre et Dupont Marie"
})

blockchain.add_block({
    "Nom": "Martin",
    "Prénom": "Alice",
    "Date de naissance": "02/02/1992",
    "Lieu de naissance": "Lyon",
    "Nom des parents": "Martin Jacques et Martin Sophie"
})

blockchain.add_block({
    "Nom": "Bernard",
    "Prénom": "Luc",
    "Date de naissance": "03/03/1993",
    "Lieu de naissance": "Marseille",
    "Nom des parents": "Bernard André et Bernard Claire"
})
Affichage de la blockchain au format JSON :

python
print("Affichage de tous les blocs dans la blockchain (format JSON):")
print(blockchain.to_json())
Vérification de la validité de la blockchain :

python
print("Blockchain valid:", blockchain.is_chain_valid())
Récupération et affichage de blocs spécifiques :

python
print("Bloc à l'index 0 (format JSON):")
print(json.dumps(blockchain.get_block(0).__dict__, sort_keys=True, indent=4))

print("Bloc à l'index 1 (format JSON):")
print(json.dumps(blockchain.get_block(1).__dict__, sort_keys=True, indent=4))

print("Bloc à l'index 2 (format JSON):")
print(json.dumps(blockchain.get_block(2).__dict__, sort_keys=True, indent=4))
Structure du Code
Block : Cette classe représente un bloc dans la blockchain.

__init__(self, index, timestamp, data, previous_hash): Initialise un bloc.
calculate_hash(self): Calcule le hachage du bloc.
to_json(self): Retourne une représentation JSON du bloc.
__repr__(self): Fournit une représentation textuelle du bloc.
Blockchain : Cette classe gère la chaîne de blocs.

__init__(self): Initialise la blockchain avec le bloc genesis.
create_genesis_block(self): Crée le bloc genesis.
get_latest_block(self): Retourne le dernier bloc de la chaîne.
add_block(self, data): Ajoute un nouveau bloc à la chaîne.
is_chain_valid(self): Vérifie l'intégrité de la blockchain.
get_block(self, index): Retourne un bloc par son index.
to_json(self): Retourne une représentation JSON de la blockchain.
Exécution
Pour exécuter le code, ouvrez votre terminal ou ligne de commande, naviguez jusqu'au répertoire contenant les fichiers, et lancez le fichier principal :

python blockchain.py
Exemple de Sortie
Voici un exemple de sortie lors de l'exécution du code :

Blockchain valid: True
Bloc à l'index 0 (format JSON):
{
    "index": 0,
    "timestamp": 1652444570.0978088,
    "data": "Genesis Block",
    "previous_hash": "0",
    "hash": "b0e72e5edcf26a8c0ae93ff8bc255e9ed0c8424e3d841bde6ff3b9dbfbdd9fa8"
}
Bloc à l'index 1 (format JSON):
{
    "index": 1,
    "timestamp": 1652444571.2000000,
    "data": {
        "Nom": "Dupont",
        "Prénom": "Jean",
        "Date de naissance": "01/01/1990",
        "Lieu de naissance": "Paris",
        "Nom des parents": "Dupont Pierre et Dupont Marie"
    },
    "previous_hash": "b0e72e5edcf26a8c0ae93ff8bc255e9ed0c8424e3d841bde6ff3b9dbfbdd9fa8",
    "hash": "c1e32a6f7b89e1f4d2e21c9c1d0c4f4bb3c2f7d8e1f0b6c3e8d0a3e1d5b6a8c4"
}
Bloc à l'index 2 (format JSON):
{
    "index": 2,
    "timestamp": 1652444572.3000000,
    "data": {
        "Nom": "Martin",
        "Prénom": "Alice",
        "Date de naissance": "02/02/1992",
        "Lieu de naissance": "Lyon",
        "Nom des parents": "Martin Jacques et Martin Sophie"
    },
    "previous_hash": "c1e32a6f7b89e1f4d2e21c9c1d0c4f4bb3c2f7d8e1f0b6c3e8d0a3e1d5b6a8c4",
    "hash": "d2e43b7c8c9d2e32a7f8b1e0f3b7d8e1d0c5f6b8c7d9a1c4e9e0b3f4e8c7d1a2"
}
Bloc à l'index 3 (format JSON):
Bloc à l'index 3 n'existe pas
Auteur
Stephane, issa, MAriam







