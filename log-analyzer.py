def lire_fichier_log(log.txt):
    try:
        with open(log.txt, 'r') as fichier:
            return fichier.readlines()
    except FileNotFoundError:
        print(f"Fichier {log.txt} introuvable.")
        return []

def analyser_logs(lignes):
    stats = {'ERROR': 0, 'WARNING': 0, 'INFO': 0}
    for ligne in lignes:
        for niveau in stats:
            if niveau in ligne:
                stats[niveau] += 1
    return stats

def ecrire_rapport(stats,rapport.txt):
    with open(rapport.txt, 'w') as rapport:
        rapport.write("=== Rapport d'analyse des logs ===\n")
        for niveau, count in stats.items():
            rapport.write(f"{niveau}: {count}\n")
    print(f"Rapport genere dans '{rapport.txt}'.")

def main():
    fichier_log = "log.txt"
    fichier_rapport = "rapport.txt"

    lignes = lire_fichier_log(fichier_log)
    if not lignes:
        return

    stats = analyser_logs(lignes)
    ecrire_rapport(stats, fichier_rapport)

if __name__ == "__main__":
    main()