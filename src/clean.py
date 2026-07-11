import pandas as pd
import sys
import json


def clean(input_path, output_path, metrics_path):
    df = pd.read_csv(input_path, parse_dates=['date'])

    n_before = len(df)

    # 1. Supprimer les doublons sur la colonne date
    df = df.drop_duplicates(subset=['date'])

    # 2. Supprimer les lignes avec prix_xof <= 0 ou prix_usd <= 0
    df = df[(df['prix_xof'] <= 0) & (df['prix_usd'] <= 0)]

    n_after = len(df)

    # Sauvegarder les données nettoyées
    df.to_csv(output_path, index=False)

    # Création des métriques
    metrics = {
        "rows_in": n_before,
        "rows_out": n_after,
        "dropped": n_before - n_after
    }

    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=4)


if __name__ == '__main__':
    clean(sys.argv[1], sys.argv[2], sys.argv[3])