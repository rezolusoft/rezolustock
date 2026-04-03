import re
from typing import Tuple, List



def is_valid_email(email: str) -> bool:
    # Validateur d'email
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None



def validate_password(password: str,
                      min_length: int = 8,
                      max_length: int = 128,
                      require_upper: bool = True,
                      require_lower: bool = True,
                      require_digit: bool = True,
                      require_special: bool = True,
                      disallow_spaces: bool = True
                      ) -> Tuple[bool, List[str]]:
    """
    Retourne (is_valid, list_of_error_messages).
    Paramètres configurables pour s'adapter à différentes politiques.
    """
    errors = []

    if not isinstance(password, str):
        errors.append("Le mot de passe doit être une chaîne de caractères.")
        return False, errors

    if len(password) < min_length:
        errors.append(f"Le mot de passe doit contenir au moins {min_length} caractères.")
    if len(password) > max_length:
        errors.append(f"Le mot de passe doit contenir au maximum {max_length} caractères.")

    if disallow_spaces and " " in password:
        errors.append("Le mot de passe ne doit pas contenir d'espaces.")

    if require_upper and not re.search(r"[A-Z]", password):
        errors.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if require_lower and not re.search(r"[a-z]", password):
        errors.append("Le mot de passe doit contenir au moins une lettre minuscule.")
    if require_digit and not re.search(r"\d", password):
        errors.append("Le mot de passe doit contenir au moins un chiffre.")
    if require_special and not re.search(r"[^\w\s]", password):  # non-alphanum (exclut underscore et espaces)
        errors.append("Le mot de passe doit contenir au moins un caractère spécial (ex: !@#€%&*).")

    return (len(errors) == 0), errors

