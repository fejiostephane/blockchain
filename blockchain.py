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