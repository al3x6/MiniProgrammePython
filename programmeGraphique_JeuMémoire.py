import random
from processing import *


####### Les boutons
class Bouton:
    def __init__(self, texte, dx, fx, dy, fy, etat):
        self.texte = texte
        self.etat = etat
        self.dx = dx
        self.fx = fx
        self.dy = dy
        self.fy = fy

    def afficher(self):
        if self.texte == "RETOUR":
            tailleTexte = 20
        elif self.texte == "Valider" or self.texte == "EFFACER":
            tailleTexte = 25
        else:
            tailleTexte = 30
        fill(10, 10, 10)
        largeur = self.fx - self.dx
        hauteur = self.fy - self.dy
        rect(self.dx, self.dy, largeur, hauteur)
        fill(500, 0, 0)
        textAlign(CENTER)
        textSize(tailleTexte)
        text(self.texte, self.dx + largeur // 2, self.dy + 1.4 * hauteur // 2)


boutonStart = Bouton("DEMARRER", 250, 440, 400, 450, False)
boutonRetour = Bouton("RETOUR", 50, 150, 50, 80, False)
bouton_validation = Bouton("Valider", 250, 350, 700, 740, False)

jeu1Niveau1 = Bouton("1", 225, 275, 225, 275, False)
jeu1Niveau2 = Bouton("2", 325, 375, 225, 275, False)
jeu1Niveau3 = Bouton("3", 425, 475, 225, 275, False)

jeu2Niveau1 = Bouton("1", 225, 275, 325, 375, False)
jeu2Niveau2 = Bouton("2", 325, 375, 325, 375, False)
jeu2Niveau3 = Bouton("3", 425, 475, 325, 375, False)

jeu3Niveau1 = Bouton("1", 225, 275, 425, 475, False)
jeu3Niveau2 = Bouton("2", 325, 375, 425, 475, False)
jeu3Niveau3 = Bouton("3", 425, 475, 425, 475, False)

nombre_bt0 = Bouton("0", 275, 325, 625, 675, False)
nombre_bt1 = Bouton("1", 175, 225, 325, 375, False)
nombre_bt2 = Bouton("2", 275, 325, 325, 375, False)
nombre_bt3 = Bouton("3", 375, 425, 325, 375, False)
nombre_bt4 = Bouton("4", 175, 225, 425, 475, False)
nombre_bt5 = Bouton("5", 275, 325, 425, 475, False)
nombre_bt6 = Bouton("6", 375, 425, 425, 475, False)
nombre_bt7 = Bouton("7", 175, 225, 525, 575, False)
nombre_bt8 = Bouton("8", 275, 325, 525, 575, False)
nombre_bt9 = Bouton("9", 375, 425, 525, 575, False)
nombre_btmoins = Bouton("-", 375, 425, 625, 675, False)
nombre_btefface = Bouton("EFFACER", 120, 230, 700, 740, False)


########## Configuration de l'écran
def setup():
    global boutonStart
    background(250)
    size(800, 800)


########## Fonction pour tracer le tableau et afficher les boutons de jeu
def tracer_tableau():
    fill(254, 231, 240)
    rect(100, 100, 400, 400)
    strokeWeight(3)
    line(100, 200, 500, 200)
    line(100, 300, 500, 300)
    line(100, 400, 500, 400)
    line(200, 100, 200, 500)
    jeu1Niveau1.afficher()
    jeu1Niveau2.afficher()
    jeu1Niveau3.afficher()
    jeu2Niveau1.afficher()
    jeu2Niveau2.afficher()
    jeu2Niveau3.afficher()
    jeu3Niveau1.afficher()
    jeu3Niveau2.afficher()
    jeu3Niveau3.afficher()
    textAlign(CENTER)
    textSize(20)
    text("Jeu 1", 125, 225)
    text("Jeu 2", 125, 325)
    text("Jeu 3", 125, 425)
    text("niveau 1", 250, 150)
    text("niveau 2", 350, 150)
    text("niveau 3", 450, 150)


############ Parti jeu
# Variables to store random numbers
nombre1 = 0
nombre2 = 0
reponse_utilisateur = ""


## Fonction pour détecter les touches clavier
def keyPressed():
    global reponse_utilisateur
    if key.isdigit():
        reponse_utilisateur += key
    elif key == BACKSPACE:
        reponse_utilisateur = reponse_utilisateur[:-1]


## Fonction generer des nombres
def generer_nombres():
    global nombre1, nombre2
    nombre1 = random.randint(1, 10)
    nombre2 = random.randint(1, 10)


## Fonction les boutons des nombres
def tableau_nombre():
    fill(254, 231, 240)
    rect(100, 280, 400, 400)
    strokeWeight(3)
    nombre_bt1.afficher()
    nombre_bt2.afficher()
    nombre_bt3.afficher()
    nombre_bt4.afficher()
    nombre_bt5.afficher()
    nombre_bt6.afficher()
    nombre_bt7.afficher()
    nombre_bt8.afficher()
    nombre_bt9.afficher()
    nombre_bt0.afficher()
    nombre_btmoins.afficher()
    nombre_btefface.afficher()


###############################################

####### Fonction pour dessiner les pages
def draw():
    global boutonStart, bouton_validation, boutonRetour, input_box, jeu1Niveau1, jeu1Niveau2, jeu1Niveau3, jeu2Niveau2, jeu2Niveau3, jeu3Niveau1, jeu3Niveau2, jeu3Niveau3, nombre_bt1, nombre_bt2, nombre_bt3, nombre_bt4, nombre_bt5, nombre_bt6, nombre_bt7, nombre_bt8, nombre_bt9, nombre_bt0, reponse_utilisateur, nombre_btmoins, nombre_btefface

    ## Ecran d'accueil
    if boutonStart.etat == False:
        boutonStart.afficher()
        textSize(25)
        text("bienvenue dans notre jeu de calcul mental", 300, 300)

    ## Ecran de choix de jeu
    elif boutonStart.etat == True and jeu1Niveau1.etat == False and jeu1Niveau2.etat == False and jeu1Niveau3.etat == False and jeu2Niveau1.etat == False and jeu2Niveau2.etat == False and jeu2Niveau3.etat == False and jeu3Niveau1.etat == False and jeu3Niveau2.etat == False and jeu3Niveau3.etat == False:
        background(250)
        # textSize(50)
        # text("Tableau de jeu",400,100)
        tracer_tableau()  # Trace le tableau et Affiche tous les boutons dans le tableau

    ## Ecran de Jeu
    ################# Jeu 1 niveau 1
    elif boutonStart.etat == True and jeu1Niveau1.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 1 niveau 1", 300, 150)
        textSize(20)
        text("Operations à trous, trouvez le nombre qui manque.", 300, 200)

        ######" LE JEU
        # generer_nombres() # la il me boucle à l'infini
        # Générer les nombres aléatoires uniquement lorsque nécessaire et Evite de boucler à l'infini
        if nombre1 == 0 or nombre2 == 0:
            generer_nombres()

        # Construire l'équation
        equation_texte = "{} + {} = ?".format(nombre1, nombre2)

        # Afficher l'équation
        textSize(30)
        text(equation_texte, 300, 250)

        # Afficher la zone pour entrer le résultat
        textSize(20)
        fill(0)
        text("Réponse:", 300, 270)

        # Afficher la réponse de l'utilisateur en continu
        text(reponse_utilisateur, 370, 270)

        # Afficher le tableau des nombres
        tableau_nombre()

        # Afficher le bouton de validation
        bouton_validation.afficher()

    ###################################################
    ################# Jeu 1 niveau 2
    elif boutonStart.etat == True and jeu1Niveau2.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 1 de niveau 2", 300, 150)

        ######" LE JEU
        # generer_nombres() # la il me boucle à l'infini
        # Générer les nombres aléatoires uniquement lorsque nécessaire et Evite de boucler à l'infini
        if nombre1 == 0 or nombre2 == 0:
            generer_nombres()

        # Construire l'équation
        equation_texte = "{} + ? = {}".format(nombre1, nombre2)

        # Afficher l'équation
        textSize(30)
        text(equation_texte, 300, 250)

        # Afficher la zone pour entrer le résultat
        textSize(20)
        fill(0)
        text("Réponse:", 300, 270)

        # Afficher la réponse de l'utilisateur en continu
        text(reponse_utilisateur, 370, 270)

        # Afficher le tableau des nombres
        tableau_nombre()

        # Afficher le bouton de validation
        bouton_validation.afficher()

    ###################################################
    ################# Jeu 1 niveau 3
    elif boutonStart.etat == True and jeu1Niveau3.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 1 de niveau 3", 300, 150)

        ######" LE JEU
        # generer_nombres() # la il me boucle à l'infini
        # Générer les nombres aléatoires uniquement lorsque nécessaire et Evite de boucler à l'infini
        if nombre1 == 0 or nombre2 == 0:
            generer_nombres()

        # Construire l'équation
        equation_texte = "{} * {} = ?".format(nombre1, nombre2)

        # Afficher l'équation
        textSize(30)
        text(equation_texte, 300, 250)

        # Afficher la zone pour entrer le résultat
        textSize(20)
        fill(0)
        text("Réponse:", 300, 270)

        # Afficher la réponse de l'utilisateur en continu
        text(reponse_utilisateur, 370, 270)

        # Afficher le tableau des nombres
        tableau_nombre()

        # Afficher le bouton de validation
        bouton_validation.afficher()

    ###################################################
    elif boutonStart.etat == True and jeu2Niveau1.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 2", 300, 150)

    elif boutonStart.etat == True and jeu2Niveau2.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 2 de niveau 2", 300, 150)

    elif boutonStart.etat == True and jeu2Niveau3.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 2 de niveau 3", 300, 150)

    elif boutonStart.etat == True and jeu3Niveau1.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 3 de niveau 1", 300, 150)

    elif boutonStart.etat == True and jeu3Niveau2.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 3 de niveau 2", 300, 150)

    elif boutonStart.etat == True and jeu3Niveau3.etat == True:
        background(250)
        boutonRetour.afficher()
        textSize(40)
        text("mon super jeu 3 de niveau 3 ", 300, 150)

    # print(jeu1Niveau1.etat)
    #################### Clique souris change état
    if mouseX > boutonStart.dx and mouseX < boutonStart.fx and mouseY > boutonStart.dy and mouseY < boutonStart.fy and mousePressed:
        boutonStart.etat = True
    # Bouton jeu
    if mouseX > jeu1Niveau1.dx and mouseX < jeu1Niveau1.fx and mouseY > jeu1Niveau1.dy and mouseY < jeu1Niveau1.fy and mousePressed:
        jeu1Niveau1.etat = True
    if mouseX > jeu1Niveau2.dx and mouseX < jeu1Niveau2.fx and mouseY > jeu1Niveau2.dy and mouseY < jeu1Niveau2.fy and mousePressed:
        jeu1Niveau2.etat = True
    if mouseX > jeu1Niveau3.dx and mouseX < jeu1Niveau3.fx and mouseY > jeu1Niveau3.dy and mouseY < jeu1Niveau3.fy and mousePressed:
        jeu1Niveau3.etat = True
    if mouseX > jeu2Niveau1.dx and mouseX < jeu2Niveau1.fx and mouseY > jeu2Niveau1.dy and mouseY < jeu2Niveau1.fy and mousePressed:
        jeu2Niveau1.etat = True
    if mouseX > jeu2Niveau2.dx and mouseX < jeu2Niveau2.fx and mouseY > jeu2Niveau2.dy and mouseY < jeu2Niveau2.fy and mousePressed:
        jeu2Niveau2.etat = True
    if mouseX > jeu2Niveau3.dx and mouseX < jeu2Niveau3.fx and mouseY > jeu2Niveau3.dy and mouseY < jeu2Niveau3.fy and mousePressed:
        jeu2Niveau3.etat = True
    if mouseX > jeu3Niveau1.dx and mouseX < jeu3Niveau1.fx and mouseY > jeu3Niveau1.dy and mouseY < jeu3Niveau1.fy and mousePressed:
        jeu3Niveau1.etat = True
    if mouseX > jeu3Niveau2.dx and mouseX < jeu3Niveau2.fx and mouseY > jeu3Niveau2.dy and mouseY < jeu3Niveau2.fy and mousePressed:
        jeu3Niveau2.etat = True
    if mouseX > jeu3Niveau3.dx and mouseX < jeu3Niveau3.fx and mouseY > jeu3Niveau3.dy and mouseY < jeu3Niveau3.fy and mousePressed:
        jeu3Niveau3.etat = True
    # Clique sur le bouton "Retour"
    if mouseX > boutonRetour.dx and mouseX < boutonRetour.fx and mouseY > boutonRetour.dy and mouseY < boutonRetour.fy and mousePressed:
        boutonStart.etat = True
        jeu1Niveau1.etat = False
        jeu1Niveau2.etat = False
        jeu1Niveau3.etat = False
        jeu2Niveau1.etat = False
        jeu2Niveau2.etat = False
        jeu2Niveau3.etat = False
        jeu3Niveau1.etat = False
        jeu3Niveau2.etat = False
        jeu3Niveau3.etat = False
        generer_nombres()  # Quand je fais retour c'est pour qu'il me repropose des nouveaux nombres quand je reviens sur la page
        reponse_utilisateur = ""

    if mouseX > nombre_bt0.dx and mouseX < nombre_bt0.fx and mouseY > nombre_bt0.dy and mouseY < nombre_bt0.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "0"
        delay(200)  # Evite l'ajout multiple du nombre, qui boucle plusieurs fois, comme ci on clique plusieurs fois
    if mouseX > nombre_bt1.dx and mouseX < nombre_bt1.fx and mouseY > nombre_bt1.dy and mouseY < nombre_bt1.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "1"
        delay(200)
    if mouseX > nombre_bt2.dx and mouseX < nombre_bt2.fx and mouseY > nombre_bt2.dy and mouseY < nombre_bt2.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "2"
        delay(200)
    if mouseX > nombre_bt3.dx and mouseX < nombre_bt3.fx and mouseY > nombre_bt3.dy and mouseY < nombre_bt3.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "3"
        delay(200)
    if mouseX > nombre_bt4.dx and mouseX < nombre_bt4.fx and mouseY > nombre_bt4.dy and mouseY < nombre_bt4.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "4"
        delay(200)
    if mouseX > nombre_bt5.dx and mouseX < nombre_bt5.fx and mouseY > nombre_bt5.dy and mouseY < nombre_bt5.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "5"
        delay(200)
    if mouseX > nombre_bt6.dx and mouseX < nombre_bt6.fx and mouseY > nombre_bt6.dy and mouseY < nombre_bt6.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "6"
        delay(200)
    if mouseX > nombre_bt7.dx and mouseX < nombre_bt7.fx and mouseY > nombre_bt7.dy and mouseY < nombre_bt7.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "7"
        delay(200)
    if mouseX > nombre_bt8.dx and mouseX < nombre_bt8.fx and mouseY > nombre_bt8.dy and mouseY < nombre_bt8.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "8"
        delay(200)
    if mouseX > nombre_bt9.dx and mouseX < nombre_bt9.fx and mouseY > nombre_bt9.dy and mouseY < nombre_bt9.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "9"
        delay(200)
    if mouseX > nombre_btmoins.dx and mouseX < nombre_btmoins.fx and mouseY > nombre_btmoins.dy and mouseY < nombre_btmoins.fy and mousePressed:
        reponse_utilisateur = reponse_utilisateur + "-"
        delay(200)
    if mouseX > nombre_btefface.dx and mouseX < nombre_btefface.fx and mouseY > nombre_btefface.dy and mouseY < nombre_btefface.fy and mousePressed:
        reponse_utilisateur = ""
        delay(200)

    # Vérifier si le bouton de validation est cliqué
    if mouseX > bouton_validation.dx and mouseX < bouton_validation.fx and mouseY > bouton_validation.dy and mouseY < bouton_validation.fy and mousePressed:

        # Le calcul selon les niveaux
        if boutonStart.etat == True and jeu1Niveau1.etat == True:
            reponse_correcte = nombre1 + nombre2
        elif boutonStart.etat == True and jeu1Niveau2.etat == True:
            reponse_correcte = nombre2 - nombre1
        elif boutonStart.etat == True and jeu1Niveau3.etat == True:
            reponse_correcte = nombre2 * nombre1

        # Vérification console
        print(reponse_correcte)
        print(reponse_utilisateur)

        # Afficher le message de résultat
        textSize(25)
        # Comparer la réponse avec la réponse correcte
        if reponse_utilisateur == str(reponse_correcte):
            text("Bravo! la réponse est correct.", 200, 800)
        else:
            text("Dommage, la réponse est incorrecte.", 200, 800)