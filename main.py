import tkinter as tk
from tkinter import ttk, messagebox

class BonDeCommandeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bon de Commande - Services de Formateur")

        self.frame_formateur = ttk.LabelFrame(self.root, text="Informations du Formateur")
        self.frame_formateur.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.label_nom = ttk.Label(self.frame_formateur, text="Nom:")
        self.label_nom.grid(row=0, column=0, sticky="w")
        self.entry_nom = ttk.Entry(self.frame_formateur)
        self.entry_nom.grid(row=0, column=1)

        self.label_prenom = ttk.Label(self.frame_formateur, text="Prénom:")
        self.label_prenom.grid(row=1, column=0, sticky="w")
        self.entry_prenom = ttk.Entry(self.frame_formateur)
        self.entry_prenom.grid(row=1, column=1)

        self.label_adresse = ttk.Label(self.frame_formateur, text="Adresse:")
        self.label_adresse.grid(row=2, column=0, sticky="w")
        self.entry_adresse = ttk.Entry(self.frame_formateur)
        self.entry_adresse.grid(row=2, column=1)

        self.label_telephone = ttk.Label(self.frame_formateur, text="Téléphone:")
        self.label_telephone.grid(row=3, column=0, sticky="w")
        self.entry_telephone = ttk.Entry(self.frame_formateur)
        self.entry_telephone.grid(row=3, column=1)

        self.label_siret = ttk.Label(self.frame_formateur, text="SIRET:")
        self.label_siret.grid(row=4, column=0, sticky="w")
        self.entry_siret = ttk.Entry(self.frame_formateur)
        self.entry_siret.grid(row=4, column=1)

        self.frame_formation = ttk.LabelFrame(self.root, text="Détails de la Formation")
        self.frame_formation.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.label_intitule = ttk.Label(self.frame_formation, text="Intitulé de la Formation:")
        self.label_intitule.grid(row=0, column=0, sticky="w")
        self.entry_intitule = ttk.Entry(self.frame_formation)
        self.entry_intitule.grid(row=0, column=1)

        self.label_quantite_jours = ttk.Label(self.frame_formation, text="Quantité de Jours:")
        self.label_quantite_jours.grid(row=1, column=0, sticky="w")
        self.entry_quantite_jours = ttk.Entry(self.frame_formation)
        self.entry_quantite_jours.grid(row=1, column=1)

        self.label_tarif_journalier = ttk.Label(self.frame_formation, text="Tarif Journalier:")
        self.label_tarif_journalier.grid(row=2, column=0, sticky="w")
        self.entry_tarif_journalier = ttk.Entry(self.frame_formation)
        self.entry_tarif_journalier.grid(row=2, column=1)

        self.button_calculer = ttk.Button(self.root, text="Calculer Total", command=self.calculer_total)
        self.button_calculer.grid(row=2, column=0, pady=10)

        self.frame_tableau = ttk.LabelFrame(self.root, text="Récapitulatif")
        self.frame_tableau.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(self.frame_tableau, columns=("Intitulé", "Quantité", "Tarif Journalier", "Total"))
        self.tree.heading("#0", text="Formateur")
        self.tree.heading("Intitulé", text="Intitulé de la Formation")
        self.tree.heading("Quantité", text="Quantité de Jours")
        self.tree.heading("Tarif Journalier", text="Tarif Journalier")
        self.tree.heading("Total", text="Total")
        self.tree.pack(fill="both", expand=True)

    def calculer_total(self):
        try:
            quantite_jours = int(self.entry_quantite_jours.get())
            tarif_journalier = float(self.entry_tarif_journalier.get())
            total = quantite_jours * tarif_journalier

            nom = self.entry_nom.get()
            prenom = self.entry_prenom.get()
            formateur = f"{nom} {prenom}"

            self.tree.insert("", "end", text=formateur, values=(self.entry_intitule.get(), quantite_jours, tarif_journalier, total))
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques pour la quantité de jours et le tarif journalier.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BonDeCommandeApp(root)
    root.mainloop()