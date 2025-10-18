#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour exécuter les visualisations et l'analyse de segmentation
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
    """Fonction principale pour les visualisations et segmentation"""
    
    print("=" * 60)
    print("VISUALISATIONS ET SEGMENTATION")
    print("=" * 60)
    
    # Générer les données
    df = get_donnees_echantillon(1000)
    
    # 1. Analyse démographique
    print("\n1. ANALYSE DÉMOGRAPHIQUE")
    print("-" * 40)
    
    # Distribution par genre
    genre_dist = df['genre'].value_counts()
    print("Distribution par genre:")
    for genre, count in genre_dist.items():
        print(f"  {genre}: {count} ({count/len(df)*100:.1f}%)")
    
    # Distribution par âge
    print(f"\nÂge moyen: {df['age'].mean():.1f} ans")
    print(f"Âge médian: {df['age'].median():.1f} ans")
    print(f"Écart-type: {df['age'].std():.1f} ans")
    
    # Distribution par ville
    ville_dist = df['ville'].value_counts()
    print("\nDistribution par ville:")
    for ville, count in ville_dist.items():
        print(f"  {ville}: {count} ({count/len(df)*100:.1f}%)")
    
    # 2. Analyse des dépenses
    print("\n2. ANALYSE DES DÉPENSES")
    print("-" * 40)
    
    print(f"Dépenses totales: {df['total_depense'].sum():,.2f} CHF")
    print(f"Dépenses moyennes: {df['total_depense'].mean():.2f} CHF")
    print(f"Dépenses médianes: {df['total_depense'].median():.2f} CHF")
    
    # Dépenses par ville
    depenses_ville = df.groupby('ville')['total_depense'].agg(['mean', 'sum', 'count']).round(2)
    print("\nDépenses par ville:")
    for ville in depenses_ville.index:
        mean_spend = depenses_ville.loc[ville, 'mean']
        total_spend = depenses_ville.loc[ville, 'sum']
        count = depenses_ville.loc[ville, 'count']
        print(f"  {ville}: {mean_spend:.2f} CHF (moyenne), {total_spend:,.2f} CHF (total), {count} clients")
    
    # 3. Segmentation des clients
    print("\n3. SEGMENTATION DES CLIENTS")
    print("-" * 40)
    
    # Segmentation par dépenses
    df['segment_depenses'] = pd.cut(df['total_depense'], 
                                   bins=[0, 200, 500, 1000, float('inf')], 
                                   labels=['Faible', 'Moyen', 'Élevé', 'VIP'])
    
    segment_counts = df['segment_depenses'].value_counts()
    print("Segmentation par dépenses:")
    for segment, count in segment_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  {segment}: {count} clients ({percentage:.1f}%)")
    
    # Segmentation par âge
    df['segment_age'] = pd.cut(df['age'], 
                              bins=[0, 25, 35, 50, 65, 100], 
                              labels=['18-25', '26-35', '36-50', '51-65', '65+'])
    
    age_segment_counts = df['segment_age'].value_counts()
    print("\nSegmentation par âge:")
    for segment, count in age_segment_counts.items():
        percentage = (count / len(df)) * 100
        print(f"  {segment}: {count} clients ({percentage:.1f}%)")
    
    # 4. Analyse des abonnements
    print("\n4. ANALYSE DES ABONNEMENTS")
    print("-" * 40)
    
    abonnement_dist = df['type_abonnement'].value_counts()
    print("Distribution des abonnements:")
    for abonnement, count in abonnement_dist.items():
        percentage = (count / len(df)) * 100
        print(f"  {abonnement}: {count} ({percentage:.1f}%)")
    
    # Dépenses moyennes par abonnement
    depenses_abonnement = df.groupby('type_abonnement')['total_depense'].mean()
    print("\nDépenses moyennes par abonnement:")
    for abonnement, depense in depenses_abonnement.items():
        print(f"  {abonnement}: {depense:.2f} CHF")
    
    # 5. Analyse de satisfaction
    print("\n5. ANALYSE DE SATISFACTION")
    print("-" * 40)
    
    df_clean = df.dropna(subset=['score_satisfaction'])
    print(f"Satisfaction moyenne: {df_clean['score_satisfaction'].mean():.2f}/10")
    print(f"Satisfaction médiane: {df_clean['score_satisfaction'].median():.2f}/10")
    
    # Clients satisfaits vs non satisfaits
    satisfied = len(df_clean[df_clean['score_satisfaction'] >= 8])
    dissatisfied = len(df_clean[df_clean['score_satisfaction'] <= 4])
    print(f"\nClients satisfaits (>=8): {satisfied} ({satisfied/len(df_clean)*100:.1f}%)")
    print(f"Clients non satisfaits (<=4): {dissatisfied} ({dissatisfied/len(df_clean)*100:.1f}%)")
    
    # 6. Analyse des appareils
    print("\n6. ANALYSE DES APPAREILS")
    print("-" * 40)
    
    device_dist = df['type_appareil'].value_counts()
    print("Distribution des appareils:")
    for device, count in device_dist.items():
        percentage = (count / len(df)) * 100
        print(f"  {device}: {count} ({percentage:.1f}%)")
    
    # 7. Sources d'acquisition
    print("\n7. SOURCES D'ACQUISITION")
    print("-" * 40)
    
    source_dist = df['source_reference'].value_counts()
    print("Distribution des sources:")
    for source, count in source_dist.items():
        percentage = (count / len(df)) * 100
        print(f"  {source}: {count} ({percentage:.1f}%)")
    
    # 8. Métriques clés
    print("\n8. MÉTRIQUES CLÉS")
    print("-" * 40)
    
    # CLV moyen
    clv_moyen = df['total_depense'].mean()
    print(f"CLV moyen: {clv_moyen:.2f} CHF")
    
    # Durée de vie moyenne
    df['duree_vie'] = (df['derniere_activite'] - df['date_inscription']).dt.days
    duree_vie_moyenne = df['duree_vie'].mean()
    print(f"Durée de vie moyenne: {duree_vie_moyenne:.1f} jours")
    
    # Taux de churn (clients inactifs depuis plus de 30 jours)
    date_cutoff = datetime(2023, 12, 1)
    churned_clients = len(df[df['derniere_activite'] < date_cutoff])
    taux_churn = (churned_clients / len(df)) * 100
    print(f"Taux de churn: {taux_churn:.1f}%")
    
    # Taux de rebond moyen
    taux_rebond_moyen = df['taux_rebond'].mean() * 100
    print(f"Taux de rebond moyen: {taux_rebond_moyen:.1f}%")
    
    print("\n" + "=" * 60)
    print("ANALYSE TERMINÉE AVEC SUCCÈS!")
    print("=" * 60)

def get_donnees_echantillon(n_clients: int = 1000) -> pd.DataFrame:
    """Générer des données d'exemple de comportement client pour l'analyse."""
    np.random.seed(42)
    random.seed(42)

    ids_clients = [f"CUST_{i:04d}" for i in range(1, n_clients + 1)]
    ages = np.random.normal(45, 15, n_clients).astype(int)
    ages = np.clip(ages, 18, 80)
    genres = np.random.choice(['M', 'F', 'Autre'], n_clients, p=[0.4, 0.5, 0.1])
    villes = np.random.choice(['Zurich', 'Geneva', 'Basel', 'Bern', 'Lausanne', 'Lucerne'], n_clients)
    
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    date_range = (end_date - start_date).days
    dates_inscription = [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(n_clients)]
    
    age_factor = (ages - ages.mean()) / ages.std()
    total_achats = np.random.poisson(5, n_clients) + np.random.poisson(2, n_clients) * (1 + 0.1 * age_factor)
    total_achats = np.clip(total_achats, 1, 20).astype(int)
    
    base_depenses = 50 + 30 * total_achats + 2 * ages + np.random.normal(0, 50, n_clients)
    total_depense = np.maximum(base_depenses, 0.5)
    
    duree_moyenne_session = np.random.exponential(10, n_clients) + 5
    duree_moyenne_session = np.clip(duree_moyenne_session, 0.5, 35)
    
    vues_page_par_session = np.random.poisson(8, n_clients) + np.random.poisson(3, n_clients)
    vues_page_par_session = np.clip(vues_page_par_session, 2, 25).astype(int)
    
    taux_rebond = np.random.beta(2, 5, n_clients) * (1 - 0.3 * (duree_moyenne_session / duree_moyenne_session.max()))
    taux_rebond = np.clip(taux_rebond, 0.01, 0.8)
    
    dates_derniere_activite = []
    for inscription_date in dates_inscription:
        jours_after_inscription = random.randint(0, (end_date - inscription_date).days)
        dates_derniere_activite.append(inscription_date + timedelta(days=jours_after_inscription))
    
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
        else:
            types_abonnement.append(np.random.choice(['Premium', 'Entreprise'], p=[0.3, 0.7]))
    
    types_appareil = np.random.choice(['Mobile', 'Bureau', 'Tablette'], n_clients, p=[0.6, 0.3, 0.1])
    
    score_satisfactions = []
    for i in range(n_clients):
        if random.random() < 0.05:
            score_satisfactions.append(np.nan)
        else:
            base_satisfaction = 5 + 0.5 * (total_depense[i] / total_depense.max()) + np.random.normal(0, 1.5)
            score_satisfactions.append(np.clip(base_satisfaction, 1, 10))
    
    tickets_support = []
    for i in range(n_clients):
        base_tickets = np.random.poisson(1)
        if not np.isnan(score_satisfactions[i]):
            satisfaction_factor = max(0, 6 - score_satisfactions[i]) / 5
        else:
            satisfaction_factor = 0.5
        tickets = base_tickets + int(total_achats[i] * 0.1) + int(satisfaction_factor * 2)
        tickets_support.append(max(0, min(tickets, 8)))
    
    sources_reference = np.random.choice(['Organique', 'Social Media', 'Email', 'Paye Ads', 'Reference'], 
                                       n_clients, p=[0.3, 0.25, 0.2, 0.15, 0.1])
    
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

if __name__ == "__main__":
    main()
