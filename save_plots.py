#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de Graphiques pour la Présentation Académique
Analyse des Comportements Clients - Suisse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import random
import warnings
warnings.filterwarnings('ignore')

def generate_and_save_plots():
    """Générer et sauvegarder tous les graphiques utilisés dans le projet"""
    
    # Générer les données (même fonction que dans le notebook)
    np.random.seed(42)
    random.seed(42)
    n_clients = 1000
    
    # Générer les données
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
    
    # 1. Distribution des âges par genre
    plt.figure(figsize=(10, 6))
    for genre in df['genre'].unique():
        mask = df['genre'] == genre
        plt.hist(df[mask]['age'], alpha=0.7, label=genre, bins=20)
    plt.xlabel('Age')
    plt.ylabel('Nombre de Clients')
    plt.title('Distribution des Ages par Genre')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('age_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Dépenses par ville
    plt.figure(figsize=(12, 6))
    ville_stats = df.groupby('ville')['total_depense'].agg(['mean', 'count']).sort_values('mean', ascending=False)
    bars = plt.bar(ville_stats.index, ville_stats['mean'], color='skyblue', alpha=0.7)
    plt.xlabel('Ville')
    plt.ylabel('Dépenses Moyennes (CHF)')
    plt.title('Dépenses Moyennes par Ville Suisse')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Ajouter les valeurs sur les barres
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{height:.1f} CHF', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('spending_by_city.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Types d'abonnement
    plt.figure(figsize=(8, 8))
    abonnement_counts = df['type_abonnement'].value_counts()
    colors = ['lightcoral', 'lightblue', 'lightgreen']
    wedges, texts, autotexts = plt.pie(abonnement_counts.values, labels=abonnement_counts.index, 
                                      autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Distribution des Types d\'Abonnement')
    plt.axis('equal')
    plt.savefig('subscription_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Corrélation dépenses vs satisfaction
    plt.figure(figsize=(10, 6))
    df_clean = df.dropna(subset=['score_satisfaction'])
    plt.scatter(df_clean['total_depense'], df_clean['score_satisfaction'], alpha=0.6, c='purple')
    plt.xlabel('Total Dépensé (CHF)')
    plt.ylabel('Score de Satisfaction')
    plt.title('Corrélation: Dépenses vs Satisfaction')
    plt.grid(True, alpha=0.3)
    
    # Ajouter une ligne de tendance
    z = np.polyfit(df_clean['total_depense'], df_clean['score_satisfaction'], 1)
    p = np.poly1d(z)
    plt.plot(df_clean['total_depense'], p(df_clean['total_depense']), "r--", alpha=0.8)
    
    plt.tight_layout()
    plt.savefig('spending_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 5. Segmentation par dépenses
    plt.figure(figsize=(10, 6))
    df['segment_depenses'] = pd.cut(df['total_depense'], 
                                   bins=[0, 200, 500, 1000, float('inf')], 
                                   labels=['Faible', 'Moyen', 'Élevé', 'VIP'])
    segment_counts = df['segment_depenses'].value_counts()
    
    bars = plt.bar(segment_counts.index, segment_counts.values, 
                  color=['red', 'orange', 'yellow', 'green'], alpha=0.7)
    plt.xlabel('Segment de Dépenses')
    plt.ylabel('Nombre de Clients')
    plt.title('Segmentation des Clients par Dépenses')
    plt.grid(True, alpha=0.3)
    
    # Ajouter les pourcentages
    total = len(df)
    for i, bar in enumerate(bars):
        height = bar.get_height()
        percentage = (height / total) * 100
        plt.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{height}\n({percentage:.1f}%)', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('spending_segments.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 6. Sources d'acquisition
    plt.figure(figsize=(10, 6))
    source_counts = df['source_reference'].value_counts()
    bars = plt.bar(source_counts.index, source_counts.values, color='lightblue', alpha=0.7)
    plt.xlabel('Source d\'Acquisition')
    plt.ylabel('Nombre de Clients')
    plt.title('Distribution des Sources d\'Acquisition')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Ajouter les pourcentages
    for bar in bars:
        height = bar.get_height()
        percentage = (height / total) * 100
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                f'{percentage:.1f}%', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.savefig('acquisition_sources.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 7. Types d'appareils
    plt.figure(figsize=(8, 8))
    device_counts = df['type_appareil'].value_counts()
    colors = ['lightcoral', 'lightblue', 'lightgreen']
    wedges, texts, autotexts = plt.pie(device_counts.values, labels=device_counts.index, 
                                      autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Distribution des Types d\'Appareils')
    plt.axis('equal')
    plt.savefig('device_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 8. Métriques de performance
    plt.figure(figsize=(12, 8))
    
    # Calculer les métriques
    clv_moyen = df['total_depense'].mean()
    satisfaction_moyenne = df['score_satisfaction'].mean()
    duree_vie_moyenne = (df['derniere_activite'] - df['date_inscription']).dt.days.mean()
    taux_rebond_moyen = df['taux_rebond'].mean() * 100
    
    metrics = ['CLV Moyen\n(CHF)', 'Satisfaction\nMoyenne', 'Durée Vie\n(jours)', 'Taux Rebond\n(%)']
    values = [clv_moyen, satisfaction_moyenne, duree_vie_moyenne, taux_rebond_moyen]
    colors = ['green', 'blue', 'orange', 'red']
    
    bars = plt.bar(metrics, values, color=colors, alpha=0.7)
    plt.ylabel('Valeur')
    plt.title('Métriques Clés de Performance')
    plt.grid(True, alpha=0.3)
    
    # Ajouter les valeurs sur les barres
    for bar, value in zip(bars, values):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + max(values)*0.01,
                f'{value:.1f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('performance_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Tous les graphiques ont ete generes et sauvegardes!")
    return True

if __name__ == "__main__":
    generate_and_save_plots()
