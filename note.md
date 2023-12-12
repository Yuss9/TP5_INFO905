AUTHOR : YURTSEVEN HUSEYIN

---
### Questions de réflexion sur l'apprentissage par renforcement (Q-learning) :

1. **Comment la valeur de epsilon (dans la stratégie epsilon-greedy) influence-t-elle l’apprentissage de l’agent ?**
    - **Réponse :** Epsilon (ε) est un paramètre qui contrôle l'exploration par rapport à l'exploitation dans la stratégie epsilon-greedy. Une valeur élevée d'epsilon encourage l'exploration, ce qui signifie que l'agent choisira souvent une action aléatoire plutôt que d'exploiter la meilleure action connue. Cela peut être bénéfique au début de l'apprentissage pour découvrir de nouvelles actions potentiellement meilleures. À mesure que l'agent apprend, on peut réduire progressivement la valeur de epsilon pour privilégier l'exploitation des connaissances acquises.

2. **Quelle est l’importance du taux d’apprentissage α et du facteur de remise γ ?**
    - **Réponse :**
        - **Taux d'apprentissage (α) :** Le taux d'apprentissage contrôle la magnitude des mises à jour des valeurs Q. Un taux d'apprentissage trop élevé peut conduire à une instabilité, tandis qu'un taux trop bas peut ralentir l'apprentissage. Il est crucial de choisir un taux d'apprentissage approprié pour garantir une convergence stable et rapide.

        - **Facteur de remise (γ) :** Le facteur de remise influence la prise en compte des récompenses futures. Un γ proche de 0 fait que l'agent privilégie les récompenses immédiates, tandis qu'un γ proche de 1 considère fortement les récompenses futures. Un équilibre approprié doit être trouvé, car trop de focus sur les récompenses futures peut rendre l'agent lent à apprendre, tandis qu'une négligence totale des récompenses futures peut entraîner des décisions sous-optimales.

3. **Comment interpréter la table des Q-valeurs finale ?**
    - **Réponse :** La table des Q-valeurs représente la connaissance que l'agent a acquise sur les actions à entreprendre dans différents états. Chaque cellule de la table correspond à une paire (état, action) et contient la valeur Q associée, représentant la récompense cumulative attendue lorsque l'agent entreprend cette action dans cet état. Une Q-valeur élevée indique que l'agent considère cette action comme bénéfique dans cet état. La table des Q-valeurs finale reflète donc les préférences de l'agent basées sur son expérience d'apprentissage, et peut être utilisée pour prendre des décisions optimales dans un environnement donné.
---
AUTHOR : YURTSEVEN HUSEYIN