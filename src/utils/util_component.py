import NXOpen

theSession = NXOpen.Session.GetSession()

def get_all_components():
    """Gibt alle Komponenten der Baugruppe als Liste zurück"""
    displayPart = theSession.Parts.Display
    root = displayPart.ComponentAssembly.RootComponent

    components = []

    def recurse(comp):
        for child in comp.GetChildren():
            components.append(child)
            recurse(child)

    recurse(root)
    return components
