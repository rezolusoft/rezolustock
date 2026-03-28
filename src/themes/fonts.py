

def font_loader(page):

    # Cette fonction nous permettra de charger les police
    # personnaliser de l'application

    fonts = page.fonts = {
    "PoppinsThin" : "fonts/Poppins-Thin.ttf",
    "PoppinsLight" : "fonts/Poppins-Light.ttf",
    "PoppinsExtraLight" : "fonts/Poppins-ExtraLight.ttf",
    "Poppins" : "fonts/Poppins-Regular.ttf",
    "PoppinsMedium" : "fonts/Poppins-Medium.ttf",
    "PoppinsSemiBold" : "fonts/Poppins-SemiBold.ttf",
    "PoppinsBold" : "fonts/Poppins-Bold.ttf",
    "PoppinsExtraBold" : "fonts/Poppins-ExtraBold.ttf"}     

    return fonts
