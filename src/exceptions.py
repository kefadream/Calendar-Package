class HoraireError(Exception):
    """Exception de base pour les erreurs liées aux horaires."""
    pass

class IntervalleInvalideError(HoraireError):
    """Exception levée lorsque l'intervalle de temps est invalide."""
    pass

class SauvegardeError(HoraireError):
    """Exception levée lors d'une erreur de sauvegarde."""
    pass

class ChargementError(HoraireError):
    """Exception levée lors d'une erreur de chargement."""
    pass
