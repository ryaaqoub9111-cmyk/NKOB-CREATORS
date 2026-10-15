/* Portfolio data. To add a REAL project:
   1) copy the image to assets/media/ (e.g. assets/media/my-project.webp, 3:2 ratio, ~1200x800 recommended)
   2) add an object to "projects" (see the commented example at the bottom)
   3) for a video: add "video": "assets/media/my-video.mp4" and "poster": "assets/media/my-video.jpg"
   The entries below are demo CONCEPTS (labelled "Concept"): they are not client projects. */
window.NKOB_PROJECTS = {
  categories: {
    web: "Website", tourism: "Tourism", branding: "Brand identity", design: "Graphic design",
    video: "Video", photo: "Photo", digital: "SEO & digital"
  },
  projects: [
    {
      category: "web", title: "Riad booking experience", label: "Concept", service: "Tourism & Booking",
      image: "assets/img/concepts/web.svg", alt: "Concept of a booking interface with an availability calendar",
      description: "Concept website for a riad: booking flow, availability calendar and multilingual interface. Demo visual, not from a client order."
    },
    {
      category: "tourism", title: "Coastal excursions — Essaouira", label: "Concept", service: "Tourism & Booking",
      image: "assets/img/concepts/tourism.svg", alt: "Concept landing page for coastal excursions",
      description: "Concept landing page for a coastal excursion operator: booking call-to-action, itinerary and gallery. Demo visual, not a client project."
    },
    {
      category: "branding", title: "Artisan studio identity", label: "Concept", service: "Brand Identity",
      image: "assets/img/concepts/branding.svg", alt: "Concept brand identity: logo, cards and colour palette",
      description: "Concept identity for a local craft studio: logo, colour system and applications. Demo visual, not a client project."
    },
    {
      category: "design", title: "Poster series — social campaign", label: "Concept", service: "Brand Identity",
      image: "assets/img/concepts/design.svg", alt: "Concept of three posters for a social media campaign",
      description: "Concept poster series and social templates for print and digital. Demo visual, not a client project."
    },
    {
      category: "video", title: "Hotel promo video", label: "Concept", service: "Video & Photo",
      image: "assets/img/concepts/video.svg", alt: "Concept storyboard for a hotel promotional video",
      description: "Demo storyboard for a short promotional video designed for web and social media. No client video is published here."
    },
    {
      category: "photo", title: "Chefchaouen photo series", label: "Concept", service: "Video & Photo",
      image: "assets/img/concepts/photo.svg", alt: "Concept photo board: landscapes, local life and architecture",
      description: "Concept photography series: landscapes, local life and architecture. Demo visual."
    },
    {
      category: "digital", title: "Local SEO & Google Business", label: "Concept", service: "SEO & Google Business",
      image: "assets/img/concepts/digital.svg", alt: "Concept of local visibility: search, business listing and growth chart",
      description: "Concept local-visibility strategy: on-page optimisation, Google business listing and local citations. Demo illustration with no result figures."
    }
    /* Example (copy, uncomment, adapt):
    ,{
      category: "web", title: "Project name", label: "Client: Name", service: "Website",
      image: "assets/media/my-project.webp", alt: "Screenshot of the website of …",
      video: "assets/media/my-project.mp4", poster: "assets/media/my-project.jpg",
      description: "What you built, for whom, with which REAL results.",
      links: [{ label: "Visit the site", url: "https://…" }]
    }
    */
  ]
};
