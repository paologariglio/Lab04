import csv
class Espositori:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
    @property
    def codice(self):
        return self.__codice
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome
    def __str__(self):
        return f"{self.__codice}, {self.nome}, {self.cognome}"

class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo

    @property
    def codice(self):
        return self.__codice
    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo(self):
        return self.__prezzo
    @prezzo.setter
    def prezzo(self,prezzo):
        self.__prezzo = prezzo

    def __str__(self):
        return f"{self.__codice}, {self.superficie}, {self.padiglione}, {self.prezzo}"

class Premium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese, posizione):
        super().__init__(codice,superficie, padiglione, prezzo)
        self.__prese = prese
        self.__posizione = posizione
    @property
    def prese(self):
        return self.__prese
    @property
    def posizione(self):
        return self.__posizione

    def __str__(self):
        return f"{super().__str__()}, {self.__prese}, {self.__posizione}"

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.espositori = { }
        self.stand = { }
@property
def nome(self):
    return self.__nome
@nome.setter
def nome(self,nome):
    self.__nome = nome
    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            with open(file_path) as infile:
                reader = csv.reader(infile)
                for line in reader:
                    if line[0].startswith('E'):
                        codice = line[0]
                        nome = line[1]
                        cognome = line[2]
                        espositore = Espositori(codice, nome, cognome)
                        self.espositori[codice] = espositore
                    if line[0].startswith('S') and len(line)<5:
                        codice = line[0]
                        superficie = line[1]
                        padiglione = line[2]
                        prezzo = line[3]
                        stand = Stand(codice, superficie, padiglione, valore)
                    if line[0].startswith('S') and len(line)==5:
                        codice = line[0]
                        superficie = line[1]
                        padiglione = line[2]
                        prezzo = line[3]
                        valore = line[4]
                        if valore.isdigit():
                            prese = int(valore)
                            posizione = None
                            premium = Premium(codice, superficie, padiglione, prezzo, prese, posizione)
                            self.stand[codice] = premium
                        else:
                            prese = None
                            posizione = valore





    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
