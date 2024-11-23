# **Architecture et Conception : Respect des Principes SOLID**

Ce dépôt contient un système modulaire conçu pour récupérer et afficher des données de diverses API (comme l'ISS et la météo), tout en respectant les principes SOLID pour une architecture propre et maintenable.

## **Diagramme UML**

Le diagramme UML ci-dessous illustre la structure du système :

![class](https://raw.githubusercontent.com/JneiraS/API_Exercices/refs/heads/exercice_two/docs/ClassUML.png)


## **Respect des principes SOLID**

Ce système a été conçu pour adhérer aux principes SOLID :

### 1. **Single Responsibility Principle (SRP)**
Chaque classe a une responsabilité unique :
- Les clients API (comme `IssLocationAPIClient`) récupèrent des données spécifiques.
- Les classes d'affichage (`DisplayISSInformations`, `DisplayWeatherRequestResults`) se concentrent uniquement sur la présentation.
- Les configurations sont gérées par `TomlConfReader`.

### 2. **Open/Closed Principle (OCP)**
L'architecture est extensible sans modifier le code existant :
- De nouveaux clients API ou formats de configuration peuvent être ajoutés en étendant les interfaces existantes (`APIClient`, `ConfigurationReader`).

### 3. **Liskov Substitution Principle (LSP)**
Les implémentations des interfaces peuvent être substituées sans impact sur le fonctionnement :
- Par exemple, n'importe quelle classe dérivée de `APIClient` peut être utilisée par les classes d'affichage.

### 4. **Interface Segregation Principle (ISP)**
Les interfaces sont spécifiques et adaptées à leurs rôles :
- `APIClient` ne définit qu'une méthode essentielle : `fetch_data`.
- Les classes implémentent uniquement les méthodes nécessaires à leur responsabilité.

### 5. **Dependency Inversion Principle (DIP)**
Les modules de haut niveau dépendent d'abstractions :
- Les classes d'affichage dépendent de l'interface `APIClient`, pas des implémentations spécifiques.
- `WeatherAPIClient` dépend de `ConfigurationReader`, une abstraction, et non de `TomlConfReader`.

## **Avantages de cette conception**
- **Modularité :** Facile à étendre (par exemple, ajouter de nouvelles API ou afficher d'autres types de données).
- **Maintenabilité :** Les responsabilités clairement définies facilitent la gestion du code.
- **Découplage :** Les dépendances sont réduites grâce à l'usage des interfaces.

## **Améliorations potentielles**
- Ajouter des mécanismes robustes de gestion des erreurs (par exemple, lors de l’appel aux API).
- Documenter ou implémenter des validations de données pour garantir l'intégrité des informations.

---

Pour plus de détails, consultez le diagramme UML ou explorez le code source.

