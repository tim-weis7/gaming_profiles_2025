import pandas as pd
from sqlalchemy import create_engine

# ---------------------------
# 1. DB-Verbindung
# ---------------------------
# Nutze hier Benutzer, Passwort, DB-Namen und Host wie in deinem Docker-Setup
engine = create_engine("postgresql://postgres:password@localhost:5432/gaming_profiles")

# ---------------------------
# 2. Funktion zum Laden von Tabellen
# ---------------------------
def load_table(table_name: str, limit: int = None) -> pd.DataFrame:
    """
    Lädt eine Tabelle oder View aus der DB.
    Optional mit LIMIT, um nur Teildaten zu laden.
    """
    sql = f"SELECT * FROM {table_name}"
    if limit:
        sql += f" LIMIT {limit}"
    try:
        df = pd.read_sql(sql, engine)
        print(f"Tabelle '{table_name}' erfolgreich geladen. Zeilen: {len(df)}")
        return df
    except Exception as e:
        print(f"Fehler beim Laden von '{table_name}': {e}")
        return pd.DataFrame()

# ---------------------------
# 3. Test / Debug
# ---------------------------
if __name__ == "__main__":
    # Beispiel: erste 5 Zeilen aus dem Schema 'public' Tabelle 'profiles'
    df_profiles = load_table("profiles", limit=5)
    print(df_profiles)