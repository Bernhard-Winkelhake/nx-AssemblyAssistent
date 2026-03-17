import NXOpen

theSession = NXOpen.Session.GetSession()

def color_all_parts_gray():
    """Färbt alle Bauteile der Baugruppe grau"""
    displayPart = theSession.Parts.Display
    root = displayPart.ComponentAssembly.RootComponent

    def recurse(comp):
        for child in comp.GetChildren():
            try:
                part = child.Prototype.OwningPart
                for body in part.Bodies:
                    body.Color = 8  # Grau
            except:
                pass
            recurse(child)

    recurse(root)
