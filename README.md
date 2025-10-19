# 📊 Analyse des Comportements Clients - Suisse

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-orange.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-purple.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.15+-red.svg)

**Intelligence Commerciale pour le Marché Suisse**

[![Demo](https://img.shields.io/badge/Demo-Live%20Analysis-brightgreen.svg)](https://github.com/invecta/Analyse-des-Comportements-Clients)
[![Report](https://img.shields.io/badge/Report-PDF%20Download-blue.svg)](Presentation_Analyse_Comportements_Clients.pdf)
[![Notebook](https://img.shields.io/badge/Notebook-Jupyter-orange.svg)](01_data_exploration.ipynb)

</div>

---

## 🎯 Aperçu du Projet

Ce projet effectue une **analyse approfondie des données de comportement des clients** sur le marché suisse, incluant l'analyse démographique, les modèles de dépenses, les métriques d'engagement et la segmentation des clients. L'analyse fournit des **insights actionables** pour la croissance commerciale et l'optimisation de l'expérience client.

### 🏆 Fonctionnalités Clés

- **📈 Exploration Complète des Données** : Workflow EDA complet du chargement des données à la génération d'insights
- **🔍 Évaluation de la Qualité des Données** : Validation approfondie incluant les valeurs manquantes, les valeurs aberrantes et les vérifications de cohérence
- **👥 Segmentation des Clients** : Analyse par niveaux de dépenses, groupes d'âge et modèles comportementaux
- **📊 Visualisations Interactives** : Plusieurs types de graphiques incluant histogrammes, graphiques de dispersion et cartes de corrélation
- **🧠 Intelligence Commerciale** : Recommandations stratégiques basées sur les insights des données
- **⏰ Analyse Temporelle** : Analyse de la durée de vie des clients et des tendances d'inscription

---

## 📊 Insights Clés

### Démographie des Clients
- **1,000 clients** analysés sur 6 villes suisses principales
- **Distribution équilibrée** : 52.5% Femmes, 38.3% Hommes, 9.2% Autre
- **Âge moyen** : 44.9 ans avec une concentration dans la tranche 36-50 ans (39.9%)

### Performance Financière
- **Revenus totaux** : 336,309 CHF
- **CLV moyen** : 336 CHF par client
- **Meilleure ville** : Lausanne avec 348.10 CHF de dépenses moyennes
- **Ville à optimiser** : Basel avec 322.60 CHF de dépenses moyennes

### Segmentation Stratégique
- **Segment Moyen** : 85.5% des clients (200-500 CHF) - Cœur de la base clientèle
- **Segment Élevé** : 6.1% des clients (500-1000 CHF) - Opportunité d'upselling
- **Segment VIP** : 0% des clients (>1000 CHF) - Potentiel inexploité

### Comportement Digital
- **Mobile-first** : 61.8% des clients utilisent principalement mobile
- **Taux de rebond** : 24.6% (acceptable pour le secteur)
- **Durée de vie client** : 92 jours en moyenne

### Alertes Critiques
- **Taux de churn élevé** : 68.7% nécessite une attention immédiate
- **Satisfaction modérée** : 5.3/10 avec seulement 3.6% de clients très satisfaits

---

## 🛠️ Technologies Utilisées

### Langages et Frameworks
- **Python 3.8+** - Langage principal d'analyse
- **Jupyter Notebook** - Environnement de développement interactif
- **Pandas** - Manipulation et analyse des données
- **NumPy** - Calculs numériques avancés

### Visualisation et Analyse
- **Matplotlib** - Graphiques statiques de base
- **Seaborn** - Visualisations statistiques avancées
- **Plotly** - Graphiques interactifs et dashboards
- **Chart.js** - Visualisations web dynamiques

### Outils de Développement
- **Git & GitHub** - Contrôle de version et collaboration
- **ReportLab** - Génération de rapports PDF professionnels
- **HTML5 & CSS3** - Interface web moderne et responsive

---

## 🚀 Installation et Utilisation

### Prérequis
```bash
Python 3.8 ou supérieur
pip (gestionnaire de paquets Python)
```

### Installation
1. **Cloner le repository**
   ```bash
git clone https://github.com/invecta/Analyse-des-Comportements-Clients.git
cd Analyse-des-Comportements-Clients
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'analyse**
   ```bash
# Option 1: Jupyter Notebook (recommandé)
   jupyter notebook 01_data_exploration.ipynb

# Option 2: Script Python direct
python -c "import pandas as pd; print('Environnement prêt!')"
```

### Structure du Projet
```
Analyse-des-Comportements-Clients/
├── 📊 01_data_exploration.ipynb          # Notebook principal d'analyse
├── 📄 Presentation_Analyse_Comportements_Clients.pdf  # Rapport académique complet
├── 🌐 index.html                         # Dashboard web interactif
├── 📋 requirements.txt                   # Dépendances Python
├── 📈 *.png                              # Graphiques générés
├── 📊 resume_analyse_clients.csv         # Résumé des métriques
├── 🐍 save_plots.py                     # Script de génération des graphiques
├── 📖 README.md                          # Documentation du projet
└── 🔧 create_academic_presentation.py   # Générateur de rapport PDF
```

---

## 📈 Résultats et Métriques

### Métriques de Performance Business
| Métrique | Valeur | Impact Business |
|----------|--------|-----------------|
| **CLV Moyen** | 336 CHF | Opportunité d'optimisation |
| **Taux de Churn** | 68.7% | ⚠️ Action immédiate requise |
| **Satisfaction** | 5.3/10 | Amélioration nécessaire |
| **Durée de Vie** | 92 jours | Potentiel de rétention |
| **Taux de Rebond** | 24.6% | Performance acceptable |

### Analyse Géographique
| Ville | Dépenses Moyennes | Clients | Potentiel |
|-------|-------------------|---------|-----------|
| **Lausanne** | 348.10 CHF | 180 | 🟢 Excellent |
| **Geneva** | 341.56 CHF | 153 | 🟢 Bon |
| **Zurich** | 338.17 CHF | 173 | 🟡 Moyen |
| **Basel** | 322.60 CHF | 173 | 🔴 À optimiser |

---

## 🎯 Recommandations Stratégiques

### 1. 🎯 Optimisation des Revenus
- **Focus sur Basel** : Développer des stratégies spécifiques pour augmenter les dépenses moyennes
- **Upselling Premium → Entreprise** : Les clients Entreprise dépensent 441 CHF vs 363 CHF pour Premium
- **Programme VIP** : Créer des offres premium pour atteindre le segment >1000 CHF

### 2. 📱 Stratégie Mobile-First
- **Optimisation mobile** : 61.8% des clients utilisent mobile en priorité
- **Fonctionnalités adaptées** : Développer des features spécifiques aux appareils mobiles
- **UX mobile** : Améliorer l'expérience utilisateur sur mobile

### 3. 🔄 Réduction du Churn
- **Programme de rétention** : Le taux de churn de 68.7% nécessite une action immédiate
- **Analyse des causes** : Identifier les raisons de départ des clients
- **Interventions ciblées** : Mettre en place des actions préventives

### 4. 📊 Amélioration de la Satisfaction
- **Focus sur les clients insatisfaits** : 19% des clients ont une satisfaction ≤4/10
- **Programme de feedback** : Mettre en place des enquêtes régulières
- **Amélioration continue** : Utiliser les retours pour optimiser l'expérience

---

## 📚 Documentation

### Rapports Disponibles
- **[📄 Rapport Académique](Presentation_Analyse_Comportements_Clients.pdf)** - Analyse complète pour présentation professionnelle
- **[🌐 Dashboard Web](index.html)** - Interface interactive avec graphiques dynamiques
- **[📊 Résumé CSV](resume_analyse_clients.csv)** - Métriques clés exportées

### Notebooks et Scripts
- **[📊 Notebook Principal](01_data_exploration.ipynb)** - Analyse complète en français
- **[🐍 Scripts Python](save_plots.py)** - Génération automatisée des graphiques
- **[📋 Dépendances](requirements.txt)** - Liste des packages Python requis

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer au projet :

1. **Fork** le repository
2. **Créez** une branche pour votre feature (`git checkout -b feature/nouvelle-analyse`)
3. **Commitez** vos changements (`git commit -m 'Ajout nouvelle analyse'`)
4. **Pushez** vers la branche (`git push origin feature/nouvelle-analyse`)
5. **Ouvrez** une Pull Request

---

## 📞 Contact et Support

- **📧 Email** : [Votre Email]
- **💼 LinkedIn** : [Votre Profil LinkedIn]
- **🐙 GitHub** : [@invecta](https://github.com/invecta)
- **📱 Twitter** : [@votre_twitter]

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<div align="center">

**Développé avec ❤️ pour l'analyse des comportements clients suisses**

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://python.org)
[![Powered by Data](https://img.shields.io/badge/Powered%20by-Data-green.svg)](https://pandas.pydata.org)
[![Built for Business](https://img.shields.io/badge/Built%20for-Business-purple.svg)](https://github.com/invecta/Analyse-des-Comportements-Clients)

</div>