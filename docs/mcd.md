
```mermaid

    erDiagram 
    # Entités Données Elections not clean
    entity Département {
        CodeDuDépartement (Clé primaire)
        LibelléDuDépartement
    }

    entity Circonscription {
        CodeDeLaCirconscription (Clé primaire)
        LibelléDeLaCirconscription
    }

    entity Commune {
        CodeDeLaCommune (Clé primaire)
        LibelléDeLaCommune
    }

    entity BureauDeVote {
        CodeDuBureauDeVote (Clé primaire)
        Inscrits
        Abstentions
        PourcentageAbstentions
        Votants
        PourcentageVotants
        Blancs
        PourcentageBlancs
        Nuls
        PourcentageNuls
        Exprimés
        PourcentageExprimés
    }

    entity Candidat {
        NuméroDePanneau
        Sexe
        Nom
        Prénom
    }

    entity RésultatDuVote {
        Voix
        PourcentageVoixParInscrits
        PourcentageVoixParExprimés
    }

    # Relations
    Département ||--o{ Circonscription : Appartient
    Département ||--o{ Commune : Contient
    Commune }|o--o{ BureauDeVote : Contient
    BureauDeVote }|o--o|{ Candidat : VotePour
    BureauDeVote }|o--o|{ RésultatDuVote : DonneRésultatPour

```