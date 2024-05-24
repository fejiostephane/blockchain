# je fais un import sur haslib pur hasher, time pour le HD, et JSOn pour affiher mes blocs en bon format, c-a-d JSON
import hashlib
import time
import json
 # Constructeur de la classe Block, 
 #######################
  #Initialise index, timestamp,data,Previous_hash qui sont les attributs du bloc, et le constructeur calul le haschage en appelant calculate_hash

class Block:
    def _init_(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Crée le hachage SHA-256 du bloc, j(utilise f-string (chaîne formatée) pour concaténer les attributs en une seule chaîne de caractère
        #.encode() convertit cette chaîne de caractères en bytes
        #hashlib.sha256(block_string) crée un objet SHA-256 et .hexdigest convertit le resultat du hachage en chaine hexadecimale
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def to_json(self):
        # je fais un return de json.dumps pour une représentation JSON du bloc et met indent = 4 pour ajouter des indentations de 4
        return json.dumps(self._dict_, sort_keys=True, indent=4)

    # la methode _repr_ pour fournir une représentation textuelle du bloc
    def _repr_(self):
        return f"Block(index={self.index}, timestamp={self.timestamp}, data={self.data}, previous_hash={self.previous_hash}, hash={self.hash})"
    
     #creer un constructeur de la classe Blockchain. Initialiser la chaîne avec le bloc genesis((bloc 0) en appelant create_genesis_block().

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Crée le bloc genesis(bloc 0), date actuelle, index 0
        return Block(0, time.time(), "Genesis Block", "0")

    #jaccede au bloc, et retourne le dernier element avec le [-1]
    def get_latest_block(self):
        return self.chain[-1]

    #add_block : Ajoute un nouveau bloc à la chaîne avec les données fournies.
    def add_block(self, data):
        # Ajoute un nouveau bloc à la chaîne
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

    #verification de l'integrité
    #or i in range(1, len(self.chain)): parcourt tous les blocs de la chaîne à partir du second bloc (indice 1) jusqu'au dernier bloc.
    #current_block = self.chain[i] récupère le bloc actuel dans la boucle.
    #previous_block = self.chain[i - 1] récupère le bloc précédent.
    #if current_block.hash != current_block.calculate_hash(): compare le hachage stocké dans le bloc courant avec un hachage recalculé du bloc courant
    # is_chain_valid : Vérifie l'intégrité de la blockchain.
    def is_chain_valid(self):
        # Vérifie l'intégrité de la blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    #get_block : Retourne un bloc par son index, ou None si l'index est invalide.
    def get_block(self, index):
        # Récupère un bloc par son index
        if 0 <= index < len(self.chain):
            return self.chain[index]
        return None

    def to_json(self):
        # Retourne une représentation JSON de la blockchain, qui sera peu necessaire
        return json.dumps([block.__dict__ for block in self.chain], sort_keys=True, indent=4)

#creer une instance
blockchain = Blockchain()

# Ajout de blocs avec des données d'extrait de naissance(exple de donner)
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