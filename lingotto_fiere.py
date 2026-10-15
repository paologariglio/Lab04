import csv
class Espositori:
    def __init__(self, codice_espositore, nome, cognome):
        self.__codice_espositore = codice_espositore
        self.__nome = nome
        self.__cognome = cognome
    @property
    def codice_espositore(self):
        return self.__codice_espositore
    @property
    def nome(self):
        return self.__nome
    @property
    def cognome(self):
        return self.__cognome

    def __str__(self):
        return f"Codice {self.__codice_espositore}: {self.nome}, {self.cognome}"

    def __eq__(self,other):
        if isinstance(other, Espositori):
            return self.__codice_espositore == other.codice_espositore
        return False

class Stand:
    def __init__(self, codice_stand, superficie, padiglione, prezzo):
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__espositore = None
        self.__disponibile = True

    @property
    def codice_stand(self):
        return self.__codice_stand
    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo(self):
        return self.__prezzo
    @property
    def espositore(self):
        return self.__espositore
    @property
    def disponibile(self):
        return self.__disponibile
    @prezzo.setter
    def prezzo(self,prezzo):
        self.__prezzo = prezzo
    @espositore.setter
    def espositore(self,espositore):
        self.__espositore = espositore
    @disponibile.setter
    def disponibile(self,disponibile):
        self.__disponibile = disponibile

    def __str__(self):
        return f"{self.__codice_stand}, {self.superficie}, {self.padiglione}, {self.prezzo}"

class Premium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand,superficie, padiglione, prezzo)
        self.__posizione = posizione
    @property
    def posizione(self):
        return self.__posizione

    def __str__(self):
        return f"{super().__str__()}, {self.__posizione}"

class Prese(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__prese = prese
    @property
    def prese(self):
        return self.__prese

    def __str__(self):
        return f"{super().__str__()}, {self.__prese}"

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
        with open(file_path, "r", encoding="Utf-8") as infile:
            reader = csv.reader(infile)
            for line in reader:
                if line[0].startswith('E'):
                    codice_espositore = line[0]
                    nome = line[1]
                    cognome = line[2]
                    espositore = Espositori(codice_espositore, nome, cognome)
                    self.espositori[codice_espositore] = espositore
                if line[0].startswith('S') and len(line)<5:
                    codice_stand = line[0]
                    superficie = line[1]
                    padiglione = line[2]
                    prezzo = line[3]
                    stand = Stand(codice_stand, superficie, padiglione, prezzo)
                    self.stand[codice_stand] = stand
                if line[0].startswith('S') and len(line)==5:
                    codice_stand = line[0]
                    superficie = line[1]
                    padiglione = line[2]
                    prezzo = line[3]
                    valore = line[4]
                    if valore.isdigit():
                        prese = int(valore)
                        premium = Premium(codice_stand, superficie, padiglione, prezzo, prese)
                        self.stand[codice_stand] = premium
                    else:
                        posizione = valore
                        premium = Premium(codice_stand, superficie, padiglione, prezzo, posizione)
                        self.stand[codice_stand] = premium



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        if codice_stand not in self.stand:
            raise Exception(f"Stand: {codice_stand} non trovato")
        if codice_espositore not in self.espositori:
            raise Exception(f"Espositore: {codice_espositore} non trovato")

        stand = self.stand[codice_stand]
        espositore = self.espositori[codice_espositore]

        if stand.disponibile == False:
            raise Exception("Stand già assegnato")

        #controllo che l'espositore non sia già assegnato
        for s in self.stand.values():
            if s.espositore == espositore:
                raise Exception("L'espositore non è disponibile")

        #aggiornamento valori
        stand.espositore = espositore
        stand.disponibile = False

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for riga in self.espositori.values(): #riga è un oggetto Espositori
            stand_trovato = None

            for line in self.stand.values(): #line è un oggetto Stand
                if riga == line.espositore: #line.espositore è un oggetto Espositore grazie all'assegnazione fatta nella funzione prima
                    stand_trovato = line
                    break


            if stand_trovato is not None:
                print(f"{riga} - Stand: {stand_trovato.codice_stand}")
            else:
                print(f"{riga} - Nessuno stand associato")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
