#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour corriger les erreurs dans le notebook
"""

import json

def fix_notebook_errors():
    """Corriger les erreurs dans le notebook"""
    
    # Lire le notebook
    with open('01_data_exploration.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Parcourir toutes les cellules
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Récupérer le code source
            source = cell['source']
            
            # Corriger les erreurs
            for i, line in enumerate(source):
                # Corriger np.random.etreta -> np.random.beta
                if 'np.random.etreta' in line:
                    source[i] = line.replace('np.random.etreta', 'np.random.beta')
                
                # Corriger d'autres erreurs potentielles
                if 'relgraphiqueation' in line:
                    source[i] = line.replace('relgraphiqueation', 'relation')
                
                if 'correlgraphiqueations' in line:
                    source[i] = line.replace('correlgraphiqueations', 'correlations')
                
                if 'correlgraphiquees' in line:
                    source[i] = line.replace('correlgraphiquees', 'correlées')
                
                if 'age_facar' in line:
                    source[i] = line.replace('age_facar', 'age_factor')
                
                if 'satisfaction_facar' in line:
                    source[i] = line.replace('satisfaction_facar', 'satisfaction_factor')
    
    # Sauvegarder le notebook corrigé
    with open('01_data_exploration.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print("Notebook corrige avec succes!")

if __name__ == "__main__":
    fix_notebook_errors()