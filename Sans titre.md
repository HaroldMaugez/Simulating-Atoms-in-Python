# Scénario vidéo — Tumor Lab (hackathon UnivaBio)

Durée cible : **3 min 00**. Deadline : 6 octobre 2026, 23h45 EDT. Jugement du 7 au 14 octobre.

---

## 0. Le cadre (vérifié dans le règlement UnivaBio)

- **Aucune durée maximale ni langue imposée** dans les règles. La vidéo doit « expliquer le but du projet, montrer ses fonctionnalités et démontrer comment l'utilisateur interagit avec le prototype ».
- L'interaction utilisateur est **obligatoire** : la démo jouée à l'écran n'est pas optionnelle.
- Les 5 critères valent 5 points chacun. Le scénario ci-dessous répond à chacun à un endroit précis (tableau en section 2).
- Un point qui compte : « **Is the team honest about what's finished versus planned?** ». La séquence 5 est écrite pour ça. Ne la coupe pas, même si tu es tenté de finir plus court.
- Hébergement : YouTube en **non répertorié**, puis le lien dans ta soumission Devpost.

### Dans quelle langue tourner ?

Le jury est international (Google Labs, AWS, LinkedIn, SAP Labs…). Deux options honnêtes :

- **Voix anglaise**, avec l'accent que tu as. C'est le choix le plus sûr pour être compris de tous les juges. La narration anglaise complète est en section 4.
- **Voix française + sous-titres anglais** incrustés. Acceptable, mais une vidéo qu'il faut lire se regarde moins bien qu'une vidéo qu'on écoute.

Ne fais pas de l'anglais « pour faire bien » si tu n'es pas à l'aise : un accent assumé passe très bien, un texte récité mot à mot s'entend tout de suite. Choisis celui où tu es le plus crédible.

---

## 1. L'idée directrice

Trois minutes, trois mouvements :

1. **0:00 → 0:35 — Pourquoi.** Un problème invisible, montré en une image.
2. **0:35 → 2:05 — Comment.** La démo jouée en direct. **C'est la moitié de la vidéo.** C'est la partie que les juges regarderont vraiment.
3. **2:05 → 3:00 — Preuve et suite.** La validation scientifique, puis l'honnêteté sur l'état du projet et la direction.

La règle qui doit tout gouverner : **on ne raconte pas le projet, on le montre.** Chaque fois que tu peux montrer un écran au lieu de le décrire, montre-le.

---

## 2. Ce que le jury note, et où tu y réponds

|Critère|Ce qu'il évalue|Où dans la vidéo|
|---|---|---|
|**Idea & Innovation**|problème réel, idée neuve, différente de l'existant|Séquence 1 (hypoxie) et Séquence 3d (résistance qui émerge)|
|**Implementation**|est-ce que ça marche, difficulté technique|Séquence 3 (démo live) et Séquence 4 (validation)|
|**Health Impact & Rigor**|pour qui, est-ce que ça peut aider|Séquence 4 (31/32, validation croisée) et Séquence 5|
|**Design & Usability**|l'interface, la pensée de l'expérience|Séquence 3, tout du long : tes clics, tes lectures de courbes|
|**Presentation**|problème clair, démo qui marche, honnêteté|Structure entière + Séquence 5|

---

## 3. Le scénario, plan par plan

### SÉQUENCE 1 — L'accroche

**0:00 → 0:20 (20 s)**

|||
|---|---|
|**Image**|`fig3_coupe_spheroide.png` en plein écran, lent zoom vers le cœur central sombre|
|**Texte écran**|_Hypoxie = radiorésistance_ (apparaît à 0:12)|

**Narration :**

> « Regardez le centre de cette tumeur. Il n'y a presque plus d'oxygène. Et c'est précisément pour ça que ces cellules survivent aux radiations : sans oxygène, l'irradiation les tue beaucoup moins. C'est un mécanisme central en oncologie. Il est invisible, et personne ne peut le manipuler. »

**Pourquoi ça marche :** tu commences par une image, pas par toi. Les dix premières secondes décident si le juge continue.

---

### SÉQUENCE 2 — Qui tu es, ce que c'est

**0:20 → 0:35 (15 s)**

|||
|---|---|
|**Image**|Page d'accueil du site : le titre, le bandeau « modèle éducatif et théorique », les 5 modes|
|**Action**|léger défilement pour révéler les modes|
|**Texte écran**|_Contrôler la tumeur, épargner l'organe_|

**Narration :**

> « Je m'appelle Harold Maugez. Tumor Lab, c'est un simulateur de croissance tumorale doublé d'un jeu de stratégie. Votre mission : contrôler la tumeur sans détruire l'organe sain. Et tout ce que vous allez voir est calculé par le moteur, pas dessiné. »

⚠️ **Si tu ne montres pas le bandeau d'avertissement ici, montre-le en séquence 5.** Il doit apparaître au moins une fois : c'est un signal de sérieux pour un jury biomédical.

---

### SÉQUENCE 3 — LA DÉMO

**0:35 → 2:05 (90 s) — la moitié de la vidéo**

#### 3a · Choix du mode — 0:35 → 0:45 (10 s)

|||
|---|---|
|**Action**|Tu es **déjà connecté**. Tu cliques sur **Organe critique**|

**Narration :**

> « Je choisis le mode Organe critique. Ici, l'organe est sensible : aucune stratégie brutale ne passe. »

> 💡 **Ne filme pas le formulaire d'inscription.** Tu perds quinze secondes et le juge veut voir le produit, pas ta page de login.

#### 3b · Premier tour : mesurer avant de frapper — 0:45 → 1:05 (20 s)

|||
|---|---|
|**Action**|Tu lances le tour 1. Tu fais une **imagerie Po2** puis une **biopsie**|
|**Image**|La carte d'hypoxie s'affiche ; les profils radiaux|
|**Texte écran**|_O₂ · glucose · lactate · pH — solveur en volumes finis_|

**Narration :**

> « Premier jour, je ne traite pas encore : je mesure. L'imagerie me donne la carte d'oxygène, la biopsie l'hétérogénéité de radiosensibilité. En dessous, le solveur résout l'oxygène, le glucose, le lactate et le pH dans tout le volume — en volumes finis conservatifs. »

#### 3c · La décision : irradier — 1:05 → 1:30 (25 s)

|||
|---|---|
|**Action**|Tu appliques une **fraction modérée (1,8 Gy)**|
|**Image**|La couronne viable qui régresse, le cœur hypoxique qui tient|

**Narration :**

> « J'irradie maintenant, avec une fraction modérée. Le modèle linéaire-quadratique avec effet oxygène me dit ce qui meurt et ce qui survit. La couronne, bien oxygénée, encaisse. Le cœur hypoxique, lui, résiste. »

#### 3d · Le retournement — 1:30 → 1:50 (20 s)

**C'est le plan le plus important de la vidéo.** C'est là que ton projet devient autre chose qu'un simulateur.

|||
|---|---|
|**Image**|La repousse tumorale, puis l'indicateur de résistance qui monte|
|**Texte écran**|_La tumeur du lendemain n'est plus celle de la veille_|

**Narration :**

> « Et c'est là que tout se joue. Les cellules qui ont survécu sont les moins sensibles. Elles se divisent, elles prennent le dessus. La tumeur du lendemain n'est plus celle de la veille : elle est devenue plus résistante. Ce n'est pas un paramètre que j'ai réglé, c'est de l'évolution darwinienne, calculée par repondérage bayésien après chaque fraction. Elle se produit dans votre partie, parce que vous avez joué. »

#### 3e · Le prix à payer — 1:50 → 2:05 (15 s)

|||
|---|---|
|**Action**|Tu insistes sur la dose, ou tu montres l'écran de fin de partie|
|**Image**|Score de toxicité / NTCP qui monte, score final|

**Narration :**

> « Et si j'insiste, je paie. La toxicité du tissu sain monte, et le score me sanctionne. C'est tout le dilemme : contrôler sans détruire. »

---

### SÉQUENCE 4 — La preuve

**2:05 → 2:30 (25 s)**

|||
|---|---|
|**Image**|Page « Résultats Scientifiques ». Défilement lent : fig1, fig7 surtout|
|**Texte écran**|_31/32 checks — validation croisée par modèle à agents 3D_|

**Narration :**

> « Ce moteur n'est pas une maquette. 31 vérifications sur 32 passent contre des données expérimentales publiées : le sphéroïde EMT6/Ro, le protocole de Freyer et Sutherland. Il est validé en croisé par un modèle à agents 3D que j'ai écrit séparément. Et l'écart qui subsiste sur la nécrose en milieu riche, je le documente plutôt que de le cacher. »

---

### SÉQUENCE 5 — Où j'en suis, où je vais

**2:30 → 2:50 (20 s)**

|||
|---|---|
|**Image**|Retour bref sur le site, ou `ai.py` / un schéma simple du pipeline|
|**Texte écran**|_Ce qui est fait · ce qui reste_|

**Narration :**

> « Voilà où j'en suis aujourd'hui. Le moteur est testé, le site est encore en chantier. Et l'étape suivante est celle qui m'intéresse le plus : un réseau de neurones qui apprend des parties des joueurs, repère les stratégies qui survivent au manque d'information, et à terme prédit l'évolution d'une tumeur pour proposer un traitement. C'est un très long chemin, et je ne le franchis pas en trois semaines. »

**Ne remplace pas cette phrase par une promesse.** C'est exactement ce que le critère _Presentation_ récompense.

---

### SÉQUENCE 6 — Clôture

**2:50 → 3:00 (10 s)**

|||
|---|---|
|**Image**|Plan fixe sur la page d'accueil, URL lisible|
|**Texte écran**|_Tumor Lab — outil éducatif et théorique, non un dispositif médical_|

**Narration :**

> « Tumor Lab est un outil éducatif et théorique. Ce n'est pas un dispositif médical. Le lien est dans la description. Allez jouer. »

---

## 4. Narration anglaise (si tu tournes en anglais)

_Mêmes timecodes que la section 3._

**[0:00]** "Look at the centre of this tumour. There is almost no oxygen left. And that is exactly why these cells survive radiation: without oxygen, radiation kills them far less effectively. It's a central mechanism in oncology. It's invisible, and nobody can manipulate it."

**[0:20]** "I'm Harold Maugez. Tumor Lab is a tumour growth simulator built as a strategy game. Your mission: control the tumour without destroying the healthy organ. And everything you're about to see is computed by the engine, not drawn."

**[0:35]** "I'll pick the Critical Organ mode. Here the organ is sensitive: no brutal strategy works."

**[0:45]** "Day one, I don't treat yet — I measure. Imaging gives me the oxygen map, biopsy gives me the spread of radiosensitivity. Underneath, the solver computes oxygen, glucose, lactate and pH across the whole volume, with a conservative finite-volume scheme."

**[1:05]** "Now I irradiate, with a moderate fraction. The linear-quadratic model with the oxygen enhancement ratio tells me what dies and what survives. The well-oxygenated rim takes the hit. The hypoxic core resists."

**[1:30]** "And this is where everything happens. The cells that survived are the least sensitive ones. They divide, they take over. Tomorrow's tumour is no longer yesterday's: it has become more resistant. That's not a parameter I tuned — it's Darwinian evolution, computed by Bayesian reweighting after every fraction. It happens in your game, because you played it."

**[1:50]** "And if I push harder, I pay for it. Healthy tissue toxicity goes up, and the score penalises me. That's the whole dilemma: control without destroying."

**[2:05]** "This engine is not a mock-up. 31 of 32 verification checks pass against published experimental data: the EMT6/Ro spheroid, the Freyer and Sutherland protocol. It's cross-validated by an independent 3D agent-based model I wrote separately. And the one remaining gap, on necrosis in rich medium, I document instead of hiding."

**[2:30]** "So here's where I stand. The engine is tested, the website is still a work in progress. And the next step is the one I care about most: a neural network that learns from players' games, spots the strategies that survive under uncertainty, and eventually predicts how a tumour will evolve in order to propose a treatment. It's a very long road, and I'm not crossing it in three weeks."

**[2:50]** "Tumor Lab is an educational and theoretical tool. It is not a medical device. The link is in the description. Go play."

---

## 5. Préparation — checklist avant d'appuyer sur REC

### Sur le site, avant de tourner

- [ ]  **Le point le plus important : ajoute une entrée sans compte.** Aujourd'hui, la page d'accueil dit « Inscrivez-vous ou connectez-vous pour jouer ». Un juge qui arrive et qui doit créer un compte pour comprendre ton projet est un juge que tu risques de perdre. Un bouton _Essayer en mode démo_ ou un compte invité pré-rempli change tout, et ça sert directement le critère _Design & Usability_.
- [ ]  Crée ton compte à l'avance et **reste connecté**.
- [ ]  Fais une **répétition complète** en notant tes clics exacts, du début du mode à l'écran de score. Tu dois pouvoir rejouer la même partie sans hésiter.
- [ ]  Vérifie que la partie que tu joues **raconte la bonne histoire** : il faut que la repousse et la montée de résistance soient bien visibles après la fraction. Si ce n'est pas net, baisse la dose de la fraction ou joue un tour de plus.
- [ ]  **Note la graine** si le moteur en utilise une, pour pouvoir refaire la même démo.

### Dans ton navigateur

- [ ]  Profil propre, **barre de favoris masquée** (Ctrl+Maj+B sur Chrome/Edge).
- [ ]  Zoom à 100 %. Ouvre la console développeur une fois pour vérifier qu'aucune erreur rouge ne s'affiche.
- [ ]  Ferme tous les onglets sauf le site, et **toutes** les notifications système : Discord, mail, mises à jour.
- [ ]  Mode Ne pas déranger activé.

### Enregistrement

- [ ]  **OBS Studio** (gratuit) ou Loom. 1920×1080, 30 images par seconde minimum.
- [ ]  **Enregistre ta voix sur une piste séparée.** Tu pourras corriger un mot sans refaire la capture d'écran. Micro près de la bouche, pièce calme, une couverture derrière toi si la pièce résonne.
- [ ]  Bouge la souris **lentement**, et marque une courte pause avant et après chaque phrase : ça te donne des points de coupe au montage.
- [ ]  Si un plan rate, **coupe et refais**. Ne garde jamais un moment d'hésitation.

### Montage

- [ ]  **Sous-titres incrustés.** Beaucoup de juges regardent sans le son, et les sous-titres automatiques de YouTube sont mauvais sur un accent. Génère un `.srt` et incruste-le.
- [ ]  Musique libre de droits, **volume très bas** (‑25 dB sous ta voix). Pas de musique du tout vaut mieux qu'une musique trop forte.
- [ ]  Dernière vérification : regarde ta vidéo **sans le son**. Si tu comprends encore tout ce qui se passe, elle est bonne.

### Après

- [ ]  Upload YouTube **non répertorié**, titre propre, description avec le lien du site et du dépôt.
- [ ]  Ajoute le lien dans ta soumission Devpost (la vidéo est une pièce obligatoire du rendu).
- [ ]  Deux améliorations gratuites sur le dépôt pendant que tu y es : remplis la section **About** (description + lien du site, elle est vide), et ajoute l'URL du site en haut du README.

---

## 6. Version courte, si tu veux tenir en 1 min 30

Si le temps te manque, sacrifie dans cet ordre :

1. **Séquence 4** (la preuve) → réduis à une phrase : « 31 vérifications sur 32 passent contre des données publiées. » Les figures restent à l'écran pendant la phrase.
2. **Séquence 2** → fusionne-la avec la séquence 1 : « Je m'appelle Harold, et j'ai construit un simulateur qui rend ce mécanisme jouable. »
3. **Séquence 3b** (la mesure) → passe directement à l'irradiation.

**Ne sacrifie jamais** la séquence 3d (le retournement darwinien) ni la séquence 5 (l'honnêteté) : c'est là que sont tes points.