
import pathlib

CORE_REP = pathlib.Path(__file__).parent

NOTES_REP = f"{CORE_REP}/data/notes"
ELEVES_REP = f"{CORE_REP}/data/eleves"
#PAYEMENT_REP = f"{CORE_REP}/data/payements"
BULLETIN_REP = f"{CORE_REP}/data/bulletins"

PAYEMENT_REP = NOTES_REP

MATIERE = { 7 : ["Mathematique", "Français", 
           "Physique", "Chimie", "Redaction",
           "Biologie", "Histoire-geograohie",
           "Anglais", "ECM", "EPS"]
}


MATIERE[8], MATIERE[9] = MATIERE[7], MATIERE[7]

MATIERE[1], MATIERE[2], MATIERE[3] = None, None, None

MATIERE[4], MATIERE[5], MATIERE[6] = None, None, None

USER_INFORMATION = {
            "prenom": None,
            "nom": None,
            "date de naissance": None,
            "prenom du père": None,
            "nom de la mère": None,
            "prenom de la mère": None,
            "matricule": None,
            "contact": None,
            "addresse": None,
            "classe": [i + 1 for i in range(10)],
        }

MOIS = ["octobre", "novembre", "decembre",
        "janvier", "fevrier", "mars", "avril",
        "mais", "juin"]