# Analyse des Comportements Clients

Un projet d'analyse exploratoire de donnees (EDA) complet axe sur la comprehension des modeles de comportement des clients, des habitudes de depenses et des metriques d'engagement pour orienter les decisions commerciales basees sur les donnees.

## Apercu du Projet

Ce projet effectue une analyse approfondie des donnees de comportement des clients, incluant l'analyse demographique, les modeles de depenses, les metriques d'engagement et la segmentation des clients. L'analyse fournit des insights actionables pour la croissance commerciale et l'optimisation de l'experience client.

## Fonctionnalites Cles

- **Exploration Complete des Donnees** : Workflow EDA complet du chargement des donnees a la generation d'insights
- **Evaluation de la Qualite des Donnees** : Validation approfondie incluant les valeurs manquantes, les valeurs aberrantes et les verifications de coherence
- **Segmentation des Clients** : Analyse par niveaux de depenses, groupes d'age et modeles comportementaux
- **Visualisations Interactives** : Plusieurs types de graphiques incluant histogrammes, graphiques de dispersion et cartes de correlation
- **Intelligence Commerciale** : Recommandations strategiques basees sur les insights des donnees
- **Analyse Temporelle** : Analyse de la duree de vie des clients et des tendances d'inscription

## Insights Cles

### Demographie des Clients
- **1 000 clients** analyses avec un age moyen de 44,9 ans
- **Repartition par genre** : 52,5% Femmes, 38,3% Hommes, 9,2% Autres
- **Repartition geographique** : Clients dans 6 villes suisses (Lausanne, Bale, Zurich en tete)

### Performance Financiere
- **Chiffre d'Affaires Total** : 336 309 $
- **Chiffre d'Affaires Moyen par Client** : 336,31 $
- **Achats Moyens par Client** : 6,6
- L'abonnement **Enterprise** montre le plus fort potentiel de depenses

### Modeles Comportementaux
- **Forte correlation** entre le nombre total d'achats et les depenses (0,839)
- **Dominance mobile** : 61,8% des clients utilisent des appareils mobiles
- **Duree moyenne de session** : 14,4 minutes
- **Taux de rebond** : 24,6%

## Stack Technique

- **Python 3.x**
- **Pandas** : Manipulation et analyse de donnees
- **NumPy** : Calculs numeriques
- **Matplotlib & Seaborn** : Visualisation de donnees
- **Plotly** : Visualisations interactives
- **Jupyter Notebook** : Environnement de developpement interactif

## Prerequis

Voir `requirements.txt` pour les dependances detaillees des packages.

## Demarrage Rapide

1. **Cloner le repository** :
   ```bash
   git clone https://github.com/invecta/customer-behavior-analysis-.git
   cd customer-behavior-analysis-
   ```

2. **Installer les dependances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Executer l'analyse** :
   ```bash
   jupyter notebook 01_data_exploration.ipynb
   ```

## Structure du Projet

```
customer-behavior-analysis/
????????? 01_data_exploration.ipynb    # Notebook principal d'analyse
????????? README.md                     # Documentation du projet (anglais)
????????? README_FR.md                  # Documentation du projet (francais)
????????? requirements.txt              # Dependances Python
????????? .gitignore                   # Regles Git ignore
```

## Composants de l'Analyse

### 1. Evaluation de la Qualite des Donnees
- Analyse des valeurs manquantes (4,1% manquantes dans les scores de satisfaction)
- Detection des doublons (0 doublons trouves)
- Validation des types de donnees et verification des plages
- Detection des valeurs aberrantes utilisant la methode IQR
- Score global de qualite des donnees : **99,92%**

### 2. Visualisations Exploratoires
- Analyse de distribution pour les variables numeriques
- Analyse des variables categoriques
- Matrice de correlation et cartes de chaleur
- Visualisations de segmentation des clients
- Analyse des tendances temporelles

### 3. Intelligence Commerciale
- Identification des clients a haute valeur (top 10%)
- Recommandations d'optimisation des revenus
- Insights sur la strategie d'abonnement
- Opportunites d'expansion geographique
- Ameliorations de l'experience client

## Recommandations Strategiques

### Optimisation des Revenus
1. Se concentrer sur les abonnes **Enterprise** et les utilisateurs **mobiles**
2. Implementer des programmes VIP pour les 100 meilleurs clients
3. Cibler les clients avec le plus fort potentiel de depenses

### Strategie d'Abonnement
1. Promouvoir l'abonnement **Enterprise** (depenses moyennes les plus elevees)
2. Creer des incitations a la mise a niveau pour les clients Basic ??? Premium
3. Developper des fonctionnalites Enterprise basees sur les besoins des clients a haute valeur

### Expansion Geographique
1. Etendre les efforts marketing a **Lausanne** (depenses moyennes les plus elevees)
2. Repliquer les strategies reussies des villes les plus performantes
3. Considerer des partenariats locaux dans les marches a haute valeur

### Experience Client
1. Adresser le taux de rebond eleve (4,8% des clients)
2. Ameliorer la duree de session pour un meilleur engagement
3. Implementer des enquetes de satisfaction pour les clients notes ???4

## Metriques de Succes

Suivre ces indicateurs de performance cles :
- **Valeur Vie Client (CLV)**
- **Revenus Recurrents Mensuels (MRR)**
- **Cout d'Acquisition Client (CAC)**
- **Taux de Desabonnement par segment**
- **Score Net Promoter (NPS)**
- **Revenus Moyens par Utilisateur (ARPU)**

## Contribution

1. Fork le repository
2. Creer une branche de fonctionnalite (`git checkout -b feature/fonctionnalite-incroyable`)
3. Commiter vos changements (`git commit -m 'Ajouter une fonctionnalite incroyable'`)
4. Pousser vers la branche (`git push origin feature/fonctionnalite-incroyable`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de details.

## Contact

Pour des questions ou suggestions, veuillez ouvrir une issue ou contacter les mainteneurs du projet.

---

**Note** : Cette analyse utilise des donnees synthetiques a des fins de demonstration. Dans un scenario reel, remplacer les fonctions de generation de donnees par des mecanismes de chargement de donnees clients reelles.
