import re
from datetime import datetime


def validate_date_from_str(string_to_validate):
    """
    Valide que la chaine de carctère est au format attendu pour une date JJ/MM/AAAA
    :param string_to_validate: Chaine à valider
    :return: True si la chaine est au format JJ/MM/AAAA
    """
    pattern = r"[0-3]?\d/[0-1]?\d/\d{4}"
    if re.match(pattern, string_to_validate):
        try:
            datetime.strptime(string_to_validate, '%d/%m/%Y')
            return True
        except ValueError:
            pass

    return False


def validate_national_chess_identifier(string_to_validate):
    """
    Valide l'identifiant national d'échec selon la norme AAXXXXX avec A un lettre et X un chiffre
    :param string_to_validate: chaine à valider
    :return: True si la chaine est au format AAXXXXX
    """
    pattern = r"[a-zA-Z]{2}\d{5}"
    return re.match(pattern, string_to_validate)
