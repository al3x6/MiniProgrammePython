import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class Ingredient:
    def __init__(self, nom, cout):
        self.nom = nom
        self.cout = cout

class Plat:
    def __init__(self, nom, prix, ingredients):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients

class Client:
    def __init__(self):
        self.affluence = random.randint(1, 10)  # Nombre de clients
        self.satisfaction = random.uniform(0, 1)  # Satisfaction de 0 à 1
        self.critique = self.generer_critique()

    def generer_critique(self):
        critiques = [
            "Excellent repas !",
            "Service un peu lent.",
            "Pas assez d'options végétariennes.",
            "Délicieux ! Je reviendrai.",
            "Médiocre, j'espérais mieux."
        ]
        return random.choice(critiques)

class Restaurant:
    def __init__(self, nom):
        self.nom = nom
        self.budget = 1000
        self.menu = []
        self.stock = {}
        self.clients = 0
        self.satisfaction_moyenne = 0
        self.ameliorations = []

    def ajouter_plat(self, plat):
        self.menu.append(plat)
        for ingredient in plat.ingredients:
            if ingredient.nom in self.stock:
                self.stock[ingredient.nom] += 1
            else:
                self.stock[ingredient.nom] = 1

    def afficher_menu(self):
        return [f"{plat.nom} - Prix: {plat.prix}€" for plat in self.menu]

    def afficher_stock(self):
        return [f"{nom}: {quantite}" for nom, quantite in self.stock.items()]

    def recevoir_clients(self):
        client = Client()
        self.clients += client.affluence
        self.satisfaction_moyenne = (self.satisfaction_moyenne + client.satisfaction) / 2
        print(f"{client.affluence} clients sont arrivés avec une satisfaction de {client.satisfaction:.2f}.")

        # Affichage de la critique
        print("Critique:", client.critique)

    def servir_clients(self):
        if self.clients > 0:
            if not self.menu:  # Vérification si le menu est vide
                print("Le menu est vide. Vous ne pouvez pas servir de clients.")
                return
            
            plat_choisi = random.choice(self.menu)
            cout_total = plat_choisi.prix * self.clients
            
            if self.verifier_ingredients(plat_choisi):
                self.budget += cout_total
                self.debiter_ingredients(plat_choisi)
                print(f"Servi {plat_choisi.nom} à {self.clients} clients. Budget actuel: {self.budget}€")
            else:
                print("Pas assez d'ingrédients pour servir les clients.")
            self.clients = 0
            self.evenement_aleatoire()  # Déclenche un événement aléatoire
        else:
            print("Pas de clients à servir.")

    def verifier_ingredients(self, plat):
        for ingredient in plat.ingredients:
            if self.stock.get(ingredient.nom, 0) < 1:
                return False
        return True

    def debiter_ingredients(self, plat):
        for ingredient in plat.ingredients:
            self.stock[ingredient.nom] -= 1

    def acheter_ingredients(self, ingredient, quantite):
        cout_total = ingredient.cout * quantite
        if self.budget >= cout_total:
            self.budget -= cout_total
            if ingredient.nom in self.stock:
                self.stock[ingredient.nom] += quantite
            else:
                self.stock[ingredient.nom] = quantite
            print(f"Acheté {quantite} de {ingredient.nom}. Budget actuel: {self.budget}€")
        else:
            print("Budget insuffisant pour cet achat.")

    def evenement_aleatoire(self):
        if random.random() < 0.2:  # 20% de chance d'événement
            print("Un critique gastronomique est arrivé !")
            bonus = random.randint(50, 200)
            self.budget += bonus
            print(f"Vous avez reçu une critique positive. Budget bonus: {bonus}€. Budget total: {self.budget}€")

    def ameliorer_restaurant(self):
        cout_amelioration = 200
        if self.budget >= cout_amelioration:
            self.budget -= cout_amelioration
            self.ameliorations.append("Amélioration de la salle.")
            print("Amélioration du restaurant réalisée.")
        else:
            print("Budget insuffisant pour une amélioration.")

# Interface Utilisateur avec Tkinter
class RestaurantApp:
    def __init__(self, master):
        self.restaurant = Restaurant("Le Gourmet")
        self.master = master
        master.title("Restaurant Tycoon")

        # Ajout d'un plat initial
        ingredient1 = Ingredient("Pâtes", 2)
        ingredient2 = Ingredient("Tomate", 1)
        plat1 = Plat("Pâtes à la tomate", 12, [ingredient1, ingredient2])
        self.restaurant.ajouter_plat(plat1)

        self.menu_text = tk.StringVar()
        self.menu_label = tk.Label(master, textvariable=self.menu_text)
        self.menu_label.pack()

        self.stock_text = tk.StringVar()
        self.stock_label = tk.Label(master, textvariable=self.stock_text)
        self.stock_label.pack()

        self.ameliorations_text = tk.StringVar()
        self.ameliorations_label = tk.Label(master, textvariable=self.ameliorations_text)
        self.ameliorations_label.pack()

        self.recevoir_button = tk.Button(master, text="Recevoir Clients", command=self.recevoir_clients)
        self.recevoir_button.pack()

        self.servir_button = tk.Button(master, text="Servir Clients", command=self.servir_clients)
        self.servir_button.pack()

        self.acheter_button = tk.Button(master, text="Acheter Ingrédients", command=self.acheter_ingredients)
        self.acheter_button.pack()

        self.ameliorer_button = tk.Button(master, text="Améliorer le Restaurant", command=self.ameliorer_restaurant)
        self.ameliorer_button.pack()

        self.update_menu()
        self.update_stock()
        self.update_ameliorations()

    def update_menu(self):
        menu = self.restaurant.afficher_menu()
        self.menu_text.set("\n".join(menu) if menu else "Menu vide")

    def update_stock(self):
        stock = self.restaurant.afficher_stock()
        self.stock_text.set("\n".join(stock) if stock else "Pas d'ingrédients en stock")

    def update_ameliorations(self):
        ameliorations = self.restaurant.ameliorations
        self.ameliorations_text.set("\n".join(ameliorations) if ameliorations else "Aucune amélioration.")

    def recevoir_clients(self):
        self.restaurant.recevoir_clients()
        self.update_menu()

    def servir_clients(self):
        self.restaurant.servir_clients()
        self.update_menu()

    def acheter_ingredients(self):
        nom_ingredient = simpledialog.askstring("Nom de l'ingrédient", "Nom de l'ingrédient:")
        if nom_ingredient:  # Vérifie que l'utilisateur a saisi un nom
            cout_ingredient = simpledialog.askinteger("Coût de l'ingrédient", "Coût de l'ingrédient:")
            if cout_ingredient is not None:  # Vérifie que l'utilisateur a saisi un coût
                quantite = simpledialog.askinteger("Quantité", "Quantité à acheter:")
                if quantite is not None:  # Vérifie que l'utilisateur a saisi une quantité
                    ingredient = Ingredient(nom_ingredient, cout_ingredient)
                    self.restaurant.acheter_ingredients(ingredient, quantite)  # Correctement appelée
                    self.update_menu()
                    self.update_stock()  # Mettre à jour le stock après l'achat
                else:
                    messagebox.showwarning("Alerte", "Quantité non saisie.")
            else:
                messagebox.showwarning("Alerte", "Coût non saisi.")
        else:
            messagebox.showwarning("Alerte", "Nom de l'ingrédient non saisi.")

    def ameliorer_restaurant(self):
        self.restaurant.ameliorer_restaurant()
        self.update_menu()
        self.update_ameliorations()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
