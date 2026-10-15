/* Données du portfolio. Pour ajouter un VRAI projet :
   1) copiez l'image dans assets/media/ (ex. assets/media/mon-projet.webp, ratio 3:2 conseillé, ~1200×800)
   2) ajoutez un objet dans "projects" (voir l'exemple commenté plus bas)
   3) pour une vidéo : ajoutez "video": "assets/media/ma-video.mp4" et "poster": "assets/media/ma-video.jpg"
   Les entrées ci-dessous sont des CONCEPTS de démonstration (label « Concept ») : ce ne sont pas des projets clients. */
window.NKOB_PROJECTS = {
  categories: {
    web: "Site web", tourism: "Tourisme", branding: "Identité visuelle", design: "Design graphique",
    video: "Vidéo", photo: "Photo", digital: "SEO & digital"
  },
  projects: [
    {
      category: "web", title: "Réservation de riad", label: "Concept", service: "Tourisme & réservation",
      image: "assets/img/concepts/web.svg", alt: "Concept d'interface de réservation avec calendrier de disponibilités",
      description: "Concept de site pour un riad : parcours de réservation, calendrier de disponibilités et interface multilingue. Visuel de démonstration, non issu d'une commande client."
    },
    {
      category: "tourism", title: "Excursions côtières — Essaouira", label: "Concept", service: "Tourisme & réservation",
      image: "assets/img/concepts/tourism.svg", alt: "Concept de page d'atterrissage pour excursions côtières",
      description: "Concept de page d'atterrissage pour un opérateur d'excursions côtières : appel à la réservation, itinéraire et galerie. Visuel de démonstration, non client."
    },
    {
      category: "branding", title: "Identité d'un atelier artisanal", label: "Concept", service: "Identité visuelle",
      image: "assets/img/concepts/branding.svg", alt: "Concept d'identité visuelle : logo, cartes et palette de couleurs",
      description: "Concept d'identité pour un atelier d'artisanat local : logo, système de couleurs et déclinaisons. Visuel de démonstration, non client."
    },
    {
      category: "design", title: "Série d'affiches — campagne sociale", label: "Concept", service: "Identité visuelle",
      image: "assets/img/concepts/design.svg", alt: "Concept de trois affiches pour une campagne sur les réseaux sociaux",
      description: "Concept de série d'affiches et de gabarits pour réseaux sociaux et impression. Visuel de démonstration, non client."
    },
    {
      category: "video", title: "Promo vidéo — hôtel", label: "Concept", service: "Vidéo & photo",
      image: "assets/img/concepts/video.svg", alt: "Concept de storyboard pour une vidéo promotionnelle d'hôtel",
      description: "Storyboard de démonstration pour une vidéo promotionnelle courte, pensée pour le web et les réseaux sociaux. Aucune vidéo client n'est publiée ici."
    },
    {
      category: "photo", title: "Série photo — Chefchaouen", label: "Concept", service: "Vidéo & photo",
      image: "assets/img/concepts/photo.svg", alt: "Concept de planche photo : paysages, vie locale et architecture",
      description: "Concept de série photographique : paysages, vie locale et architecture. Visuel de démonstration."
    },
    {
      category: "digital", title: "SEO local & Google Business", label: "Concept", service: "SEO & Google Business",
      image: "assets/img/concepts/digital.svg", alt: "Concept de visibilité locale : recherche, fiche d'établissement et courbe de croissance",
      description: "Concept de stratégie de visibilité locale : optimisation on-page, fiche d'établissement Google et citations locales. Illustration de démonstration, sans chiffres de résultats."
    }
    /* Exemple (à copier, décommenter, adapter) :
    ,{
      category: "web", title: "Nom du projet", label: "Client : Nom", service: "Site web",
      image: "assets/media/mon-projet.webp", alt: "Capture d'écran du site de …",
      video: "assets/media/mon-projet.mp4", poster: "assets/media/mon-projet.jpg",
      description: "Ce que vous avez réalisé, pour qui, avec quels résultats RÉELS.",
      links: [{ label: "Voir le site", url: "https://…" }]
    }
    */
  ]
};
