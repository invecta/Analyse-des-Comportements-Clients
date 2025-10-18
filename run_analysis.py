#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exécuter le notebook d'analyse des comportements clients
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import random
import warnings
warnings.filterwarnings('ignore')

def main():
    """Fonction principale pour exécuter l'analyse"""
    
    print("=" * 60)
    print("ANALYSE DES COMPORTEMENTS CLIENTS - SUISSE")
    print("=" * 60)
    
    # Configuration des styles
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Configuration des options d'affichage
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    
    print("Configuration terminee!")
    
    # Générer les données
    print("\nGenerer les donnees d'exemple...")
    df = get_donnees_echantillon(1000)
    print(f"Dataset genere: {df.shape[0]} clients, {df.shape[1]} variables")
    
    # Valider les données
    print("\nValidation des donnees...")
    validation_resultats = validate_donnees_client(df)
    print("Validation terminee!")
    
    # Afficher les informations du dataset
    print("\n" + "=" * 60)
    print("APERÇU DU DATASET")
    print("=" * 60)
    print(f"Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\nINFORMATIONS DES COLONNES:")
    print("-" * 40)
    print(df.info())
    
    # Afficher les premières lignes
    print("\nPREMIERES LIGNES:")
    print("-" * 40)
    print(df.head())
    
    # Statistiques descriptives
    print("\nSTATISTIQUES DESCRIPTIVES:")
    print("-" * 40)
    print(df.describe())
    
    # Analyse de qualité des données
    print("\n" + "=" * 60)
    print("ANALYSE DE LA QUALITÉ DES DONNÉES")
    print("=" * 60)
    
    # Vérifier les valeurs manquantes
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    
    quality_summary = pd.DataFrame({
        'Valeurs_Manquantes': missing_data,
        'Pourcentage': missing_percent,
        'Type': df.dtypes
    })
    
    print("RÉSUMÉ DE LA QUALITÉ:")
    print("-" * 40)
    print(quality_summary)
    
    # Vérifier les doublons
    duplicates = df.duplicated().sum()
    print(f"\nDoublons detectes: {duplicates}")
    
    # Vérifier les valeurs uniques
    print("\nVALEURS UNIQUES PAR COLONNE:")
    print("-" * 40)
    for col in df.columns:
        unique_count = df[col].nunique()
        print(f"{col}: {unique_count} valeurs uniques")
    
    print("\nAnalyse de qualite terminee!")
    
    # Sauvegarder le résumé
    resume_data = {
        'Metrique': ['Clients_Totaux', 'Revenus_Totaux_CHF', 'CLV_Moyen_CHF', 'Taux_Churn_Pourcent', 'Satisfaction_Moyenne'],
        'Valeur': [
            len(df),
            df['total_depense'].sum(),
            df['total_depense'].mean(),
            (len(df[df['derniere_activite'] < datetime(2023, 12, 1)]) / len(df)) * 100,
            df['score_satisfaction'].mean()
        ]
    }
    
    resume_df = pd.DataFrame(resume_data)
    resume_df.to_csv('resume_analyse_clients.csv', index=False)
    print("\nResume sauvegarde dans 'resume_analyse_clients.csv'")
    
    print("\n" + "=" * 60)
    print("ANALYSE TERMINEE AVEC SUCCÈS!")
    print("=" * 60)

def get_donnees_echantillon(n_clients: int = 1000) -> pd.DataFrame:
    """Générer des données d'exemple de comportement client pour l'analyse."""
    np.random.seed(42)  # Pour des résultats reproductibles
    random.seed(42)

    # Générer les IDs clients
    ids_clients = [f"CUST_{i:04d}" for i in range(1, n_clients + 1)]

    # Générer les données démographiques
    ages = np.random.normal(45, 15, n_clients).astype(int)
    ages = np.clip(ages, 18, 80)  # Assurer une plage d'âge raisonnable

    genres = np.random.choice(['M', 'F', 'Autre'], n_clients, p=[0.4, 0.5, 0.1])
    
    villes = np.random.choice([
        'Zurich', 'Geneva', 'Basel', 'Bern', 'Lausanne', 'Lucerne'
    ], n_clients)
    
    # Générer les dates d'inscription (réparties sur 2023)
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = (end_date - start_date).days

    dates_inscription = [
        start_date + timedelta(days=random.randint(0, date_range))
        for _ in range(n_clients)
    ]
    
    # Générer les données comportementales avec des corrélations réalistes
    age_factor = (ages - ages.mean()) / ages.std()
    
    # Générer le nombre total d'achats (1-20, avec une corrélation à l'âge)
    total_achats = np.random.poisson(5, n_clients) + np.random.poisson(2, n_clients) * (1 + 0.1 * age_factor)
    total_achats = np.clip(total_achats, 1, 20).astype(int)
    
    # Générer le montant total dépensé (corrélé avec les achats et l'âge)
    base_depenses = 50 + 30 * total_achats + 2 * ages + np.random.normal(0, 50, n_clients)
    total_depense = np.maximum(base_depenses, 0.5)  # Minimum 0.50CHF
    
    # Générer les données de session
    duree_moyenne_session = np.random.exponential(10, n_clients) + 5
    duree_moyenne_session = np.clip(duree_moyenne_session, 0.5, 35)
    
    vues_page_par_session = np.random.poisson(8, n_clients) + np.random.poisson(3, n_clients)
    vues_page_par_session = np.clip(vues_page_par_session, 2, 25).astype(int)
    
    # Taux de rebond (relation inverse avec la durée de session)
    taux_rebond = np.random.beta(2, 5, n_clients) * (1 - 0.3 * (duree_moyenne_session / duree_moyenne_session.max()))
    taux_rebond = np.clip(taux_rebond, 0.01, 0.8)
    
    # Générer les dates de dernière activité
    dates_derniere_activite = []
    for inscription_date in dates_inscription:
        jours_after_inscription = random.randint(0, (end_date - inscription_date).days)
        dates_derniere_activite.append(inscription_date + timedelta(days=jours_after_inscription))
    
    # Générer les types d'abonnement (corrélés avec les dépenses)
    q25 = np.percentile(total_depense, 25)
    q50 = np.percentile(total_depense, 50)
    q75 = np.percentile(total_depense, 75)

    types_abonnement = []
    for depenses in total_depense:
        if depenses <= q25:
            types_abonnement.append('Basique')
        elif depenses <= q50:
            types_abonnement.append(np.random.choice(['Basique', 'Premium'], p=[0.4, 0.6]))
        elif depenses <= q75:
            types_abonnement.append(np.random.choice(['Premium', 'Entreprise'], p=[0.7, 0.3]))
        else:  # Top 25%
            types_abonnement.append(np.random.choice(['Premium', 'Entreprise'], p=[0.3, 0.7]))
    
    # Générer les types d'appareils
    types_appareil = np.random.choice(['Mobile', 'Bureau', 'Tablette'], n_clients, p=[0.6, 0.3, 0.1])
    
    # Générer les scores de satisfaction
    score_satisfactions = []
    for i in range(n_clients):
        if random.random() < 0.05:  # 5% de valeurs manquantes
            score_satisfactions.append(np.nan)
        else:
            base_satisfaction = 5 + 0.5 * (total_depense[i] / total_depense.max()) + np.random.normal(0, 1.5)
            score_satisfactions.append(np.clip(base_satisfaction, 1, 10))
    
    # Générer les tickets de support
    tickets_support = []
    for i in range(n_clients):
        base_tickets = np.random.poisson(1)
        if not np.isnan(score_satisfactions[i]):
            satisfaction_factor = max(0, 6 - score_satisfactions[i]) / 5
        else:
            satisfaction_factor = 0.5
        tickets = base_tickets + int(total_achats[i] * 0.1) + int(satisfaction_factor * 2)
        tickets_support.append(max(0, min(tickets, 8)))
    
    # Générer les sources de référence
    sources_reference = np.random.choice([
        'Organique', 'Social Media', 'Email', 'Paye Ads', 'Reference'
    ], n_clients, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    
    # Créer le DataFrame
    df = pd.DataFrame({
        'id_client': ids_clients,
        'age': ages,
        'genre': genres,
        'ville': villes,
        'date_inscription': dates_inscription,
        'total_achats': total_achats,
        'total_depense': total_depense,
        'duree_moyenne_session': duree_moyenne_session,
        'vues_page_par_session': vues_page_par_session,
        'taux_rebond': taux_rebond,
        'derniere_activite': dates_derniere_activite,
        'type_abonnement': types_abonnement,
        'type_appareil': types_appareil,
        'score_satisfaction': score_satisfactions,
        'tickets_support': tickets_support,
        'source_reference': sources_reference
    })
    
    return df

def validate_donnees_client(df: pd.DataFrame) -> dict:
    """Valider la qualité des données client."""
    validation_results = {
        'completeness': {},
        'consistency': {},
        'accuracy': {},
        'timeliness': {}
    }
    
    # Vérifier la complétude
    for col in df.columns:
        missing_count = df[col].isnull().sum()
        missing_percent = (missing_count / len(df)) * 100
        validation_results['completeness'][col] = {
            'missing_count': missing_count,
            'missing_percent': missing_percent,
            'is_complete': missing_percent < 5
        }
    
    # Vérifier la cohérence
    validation_results['consistency']['age_range'] = {
        'min': df['age'].min(),
        'max': df['age'].max(),
        'valid': 18 <= df['age'].min() and df['age'].max() <= 80
    }
    
    validation_results['consistency']['spending_positive'] = {
        'min': df['total_depense'].min(),
        'valid': df['total_depense'].min() >= 0
    }
    
    # Vérifier l'exactitude
    validation_results['accuracy']['satisfaction_range'] = {
        'min': df['score_satisfaction'].min(),
        'max': df['score_satisfaction'].max(),
        'valid': df['score_satisfaction'].min() >= 1 and df['score_satisfaction'].max() <= 10
    }
    
    return validation_results

if __name__ == "__main__":
    main()
