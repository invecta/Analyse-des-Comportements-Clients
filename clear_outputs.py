#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour nettoyer les outputs du notebook
"""

import json

def clear_notebook_outputs():
    """Nettoyer tous les outputs du notebook"""
    
    # Lire le notebook
    with open('01_data_exploration.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Parcourir toutes les cellules
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Vider les outputs
            cell['outputs'] = []
            # Réinitialiser l'execution_count
            cell['execution_count'] = None
    
    # Sauvegarder le notebook nettoyé
    with open('01_data_exploration.ipynb', 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print("Notebook nettoye avec succes!")

if __name__ == "__main__":
    clear_notebook_outputs()
