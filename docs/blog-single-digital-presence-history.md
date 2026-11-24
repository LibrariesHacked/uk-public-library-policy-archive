---
title: "From Culture Grid to LibraryOn: The 30-Year Quest for a Single Digital Presence in UK Public Libraries"
subtitle: "A retrospective on three decades of national portals, data aggregation, open APIs, and structural silos."
author: "Libraries Hacked"
date: "2026-11-24"
reading_time: "7 min read"
tags:
  - public-libraries
  - open-data
  - single-digital-presence
  - digital-infrastructure
  - library-policy
---

# From Culture Grid to LibraryOn: The 30-Year Quest for a Single Digital Presence in UK Public Libraries

In November 2026, the British Library published its comprehensive evaluation report on [LibraryOn](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/single-digital-presence-programme-report/report.md) — the culmination of a four-year, £3.4 million capital investment funded by Arts Council England to build a modern "Single Digital Presence" for public libraries.

With a newly unified directory of over 3,000 library service points, a public-facing discovery platform, and nearly £1.8 million disbursed directly to local library services for digital innovation, LibraryOn marks the most concerted national digital effort for English libraries in over a decade.

Yet for anyone who has followed the digital policy landscape of UK public libraries over the last thirty years, the story of the Single Digital Presence is not a new one. It is a cyclical epic spanning four distinct technological eras: from the lottery-funded hardware rollout of the late 1990s, through the open metadata APIs of the Culture Grid in the 2000s, to the ill-fated "Bookmark Your Library" portal of 2013, and finally to the contemporary discovery architecture of LibraryOn.

Each chapter set out with the same noble vision: to unite the UK’s fragmented local library services into a cohesive, findable, and transactional national digital offer. And each chapter ran headfirst into the same structural immovable object: local authority autonomy and proprietary Library Management System (LMS) vendor silos.

```mermaid
flowchart TD
    subgraph ERA1 ["1. The Connectivity Era (1997–2004)"]
        PN["The People's Network (1997–2004)<br/>30,000+ PCs & broadband in 4,000+ libraries"]
    end

    subgraph ERA2 ["2. The Aggregation Era (2004–2012)"]
        PNDS["PNDS & Enquire (2004–2008)<br/>OAI-PMH metadata harvesting & 24/7 reference chat"]
        CG["Culture Grid & APIs (2008–2012)<br/>MLA & Collections Trust: Solr APIs, open metadata aggregation"]
        FAL["Find a Library Project (2010–2012)<br/>First standardized open dataset of UK library service points"]
        PNDS --> CG
        CG --> FAL
    end

    subgraph ERA3 ["3. The First Portal Attempt (2013–2015)"]
        BYL["Bookmark Your Library (2013–2015)<br/>SCL, ACE, OCLC: FABLibraries union catalogue & Enquire chat"]
        FAIL["BiblioCommons Critique (2015)<br/>'New paint, but no new plumbing'<br/>Isolated traffic (30k/yr) & closed LMS silos"]
        BYL --> FAIL
    end

    subgraph ERA4 ["4. Modern Single Digital Presence (2014–2026)"]
        SR["The Sieghart Review (2014)<br/>Recommends a Single Digital Presence for English libraries"]
        BL5["British Library Scoping Report (2019)<br/>Five approaches: shared LMS vs. brand & discovery"]
        LON["LibraryOn Programme (2022–2026)<br/>National brand, 3,000+ branches mapped, open API, £1.8m grants"]
        SR --> BL5 --> LON
    end

    PN --> PNDS
    FAL -.->|"Austerity cliff-edge (2012)<br/>Data preserved by open data community"| BYL
    FAIL --> SR
    FAL -.->|"Open dataset lineage"| LON

    classDef era fill:#f8f9fa,stroke:#cbd5e1,stroke-width:1px,color:#0f172a;
    classDef highlight fill:#eff6ff,stroke:#3b82f6,stroke-width:2px,color:#1e3a8a;
    classDef warning fill:#fff1f2,stroke:#f43f5e,stroke-width:2px,color:#881337;
    classDef success fill:#f0fdf4,stroke:#22c55e,stroke-width:2px,color:#14532d;

    class PN,PNDS,CG,FAL highlight;
    class FAIL warning;
    class LON success;
```

Here is the 30-year history of how we got here, why earlier iterations stalled, and what the evidence tells us about the future of library data and digital infrastructure.

---

## 1. The Hardware & Connectivity Era (1997–2004)

The journey began not with web applications or shared APIs, but with wires and beige desktop computer towers. 

In 1997, the Library and Information Commission (LIC) published its landmark report, [New Library: The People's Network](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/lic-new-library-the-peoples-network-1997/report.md), followed a year later by [Building the New Library Network](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/lic-building-the-new-library-network-1998/report.md). The thesis was revolutionary for its time: public libraries should serve as the universal public on-ramp to the "Information Superhighway."

Backed by more than £100 million of National Lottery funding through the New Opportunities Fund, the People's Network successfully installed over 30,000 internet terminals and broadband connections across more than 4,000 public library buildings by 2004. 

It was a triumph of capital infrastructure. However, once the computers were in place and the public was logging on, an obvious question arose: *Where was the shared digital content, and how would users discover what was held across the country's public libraries?*

---

## 2. The Aggregation Era: PNDS, Culture Grid, and "Find a Library" (2004–2012)

By the mid-2000s, attention shifted from physical connectivity to digital discovery. The Museums, Libraries and Archives Council (MLA) took charge of coordinating national digital initiatives, giving birth to two foundational projects:

### The People's Network Discovery Service (PNDS) & Enquire
The MLA established the People’s Network Discovery Service, which sought to harvest and cross-search digital content across local libraries, archives, and regional hubs. Contributors exposed collections via **OAI-PMH** (Open Archives Initiative Protocol for Metadata Harvesting) using the **PNDS Dublin Core Application Profile (PNDS DCAP)**. 

Alongside this sat **Enquire**, a 24/7 virtual reference enquiry service. Powered by OCLC’s QuestionPoint software and staffed collaboratively by public librarians across the country, Enquire demonstrated that library staff could deliver a shared, live national service even if their physical services remained local.

### The Culture Grid APIs
In 2008, the MLA expanded this into the **Data Aggregation Programme**, partnering with the **Collections Trust** to launch the **Culture Grid**. 

The Culture Grid was an ambitious open-data and interoperability engine. Rather than simply building a consumer website, it provided a centralized metadata aggregation platform with **SOLR REST APIs**, OpenSearch endpoints, and OAI-PMH harvesting. It aggregated millions of digital objects and catalog records from over 50 contributing institutions, syndicating UK cultural collections directly to Europeana, the BBC, and Wikipedia.

### The Original "Find a Library" Project
Crucially for public libraries, the Culture Grid team recognized a glaring blind spot: the UK had no single, authoritative open dataset of where public libraries actually were, when they were open, or what services they provided.

Working in partnership with the Society of Chief Librarians (SCL) and Directgov (the predecessor to GOV.UK), the MLA and Collections Trust collated and structured data for over 4,000 public library service points into a national directory. The **Find a Library API** allowed external developers and public portals to query local library services by postcode or coordinates for the very first time.

### Why the Aggregation Era Stalled
The Culture Grid was technically forward-thinking, but politically vulnerable:
1. **The 2010 Austerity Cliff-Edge**: In the 2010 government spending review, the Coalition government announced the abolition of the MLA under its "bonfire of the quangos." By March 2012, the MLA was formally wound down, and central strategic funding for national data aggregation disappeared.
2. **Metadata Burden**: Small local authorities struggled to maintain strict OAI-PMH endpoints and PNDS Dublin Core schemas without ongoing central technical assistance.
3. **Retirement**: The Collections Trust eventually retired the Culture Grid around 2015. 

However, this work was not lost. The open data legacy of the Collections Trust dataset formed the foundation upon which grassroots initiatives—including **Libraries Hacked** (`librarydata.uk`)—later stepped in to crowdsource, clean, and maintain open public library datasets using open government licenses and Wikidata.

---

## 3. The First "Single Digital Presence": Bookmark Your Library (2013–2015)

In March 2013, the Society of Chief Librarians (now Libraries Connected), Arts Council England, The Reading Agency, and OCLC launched **Bookmark Your Library** (`bookmarkyourlibrary.org.uk`).

Promoted as a single national digital destination, Bookmark Your Library attempted to bundle three distinct elements into one consumer portal:
1. **FABLibraries (*Find a Book in Libraries*, `fablibraries.worldcat.org`)**: A national union catalogue powered by OCLC WorldCat, ingesting catalog dumps mirrored from **UnityUK** (the UK's interlending database).
2. **Enquire**: The 24/7 virtual chat service.
3. **Find a Library**: A service directory powered by the Collections Trust location dataset.

### The Post-Mortem: "New Paint, But No New Plumbing"
Despite heavy promotional campaigns, Bookmark Your Library quickly proved to be a cautionary tale. In late 2015, BiblioCommons and SCL published the landmark report [Essential Digital Infrastructure for Public Libraries in England: A plan for moving forward](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/scl-essential-digital-infrastructure-2015/report.md). The report delivered an uncompromising critique of the Bookmark Your Library model:

- **Surface Paint vs. Foundational Plumbing**: Users on Bookmark Your Library could search for a title across the country, but the platform had no live two-way connection to local Library Management Systems. A user could not see if a book was actually sitting on the shelf, could not join their local library online, and could not reserve the book without being kicked out to a separate, disjointed local council OPAC.
- **The "Island" Trap and Traffic Reality**: Local authority library catalogues already enjoyed massive, organic footfall—a typical council catalogue (like Doncaster) received around 300,000 visits per month. In contrast, **Bookmark Your Library attracted roughly 30,000 visits in an entire year across the whole of England**. By isolating national content on an external marketing portal rather than integrating into local discovery layers, the platform failed to reach real users.
- **LMS Vendor Fragmentation**: With 151 English library authorities using disparate proprietary LMS software (Axiell, Civica, SirsiDynix, Infor, Capita), the lack of standardized, open transactional APIs made real interoperability impossible.

As SCL President Ciara Eastell concluded at the time: *"We can no longer think of a digital offer as something optional or separate... they provide new paint, but no new plumbing."*

---

## 4. Re-imagining the Vision: Sieghart to the British Library Scoping (2014–2019)

Even as Bookmark Your Library stumbled, national appetite for a solution only intensified:

- **[The Sieghart Review (2014)](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/independent-library-report-for-england-2014/report.md)**: William Sieghart’s *Independent Library Report for England* formally embedded the phrase **"Single Digital Presence"** into government policy, calling for a unified national digital network, single catalogue, and national library card.
- **[Libraries Deliver: Ambition for Public Libraries in England (2016)](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/libraries-taskforce-ambition-action-plan-2016/report.md)**: The newly formed Libraries Taskforce reaffirmed the Single Digital Presence as one of its seven core ambitions.
- **[Five Approaches to a Single Digital Presence (2019)](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/single-digital-presence-scoping-report/report.md)**: Funded by Arts Council England and the Carnegie UK Trust, the British Library led a thorough scoping exercise that modeled five potential paths forward:
  1. *Deep Shared Infrastructure*: A single national LMS procured for all authorities.
  2. *UK-Wide Content Discovery*: A national aggregator for digitized local history and public collections (akin to Gallica or Trove).
  3. *Unified Digital Lending*: A single national e-book platform.
  4. *Safe Social Space*: A community platform connecting readers and staff.
  5. *One Library Brand*: A unifying brand identity and digital "front door."

The 2019 scoping report concluded that procuring a single national LMS was neither politically feasible nor immediately desirable given local governance autonomy. Instead, it recommended focusing on brand identity, national promotion, and open sector collaboration.

---

## 5. LibraryOn (2022–2026): A Modern Front Door

In 2022, backed by a £3.4 million capital grant from Arts Council England and £1.4 million in British Library revenue match, the British Library launched the **LibraryOn** programme.

The newly released [LibraryOn Programme Evaluation (November 2026)](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/single-digital-presence-programme-report/report.md) demonstrates clear and tangible successes within its capital remit:

- **A Vibrant Public-Facing Brand**: Created `libraryon.org`, positioning public libraries as vibrant, essential modern community hubs.
- **National Library Finder & Open Dataset**: Built an interactive map and open API encompassing over 3,000 public library locations, integrating self-service data management for library authorities and standardizing accessibility, facilities, and service metadata (with acknowledged collaboration from Libraries Hacked).
- **Audience Reach**: Generated over 280,000 visitor sessions, with 22% of visitors following onward referral links directly to local council library websites.
- **Local Capacity Investment**: Disbursed nearly £1.8 million through 63 digital grants across 90 English library authorities (59% of all services), funding virtual 3D tours, redesigned local websites, app development, and LMS integrations.
- **Sector Upskilling**: Reached 77% of English public library services through expert community-of-practice webinars and masterclasses.

---

## 6. What 30 Years of Policy Teaches Us About Library Data

Looking back from the People's Network in 1997 to the completion of LibraryOn in 2026, several inescapable architectural lessons emerge for anyone working with library data:

### 1. Portals Cannot Substitute for Plumbing
The central finding of the 2015 BiblioCommons report remains just as true in 2026: **a digital front door can inspire, but it cannot transact without backend plumbing**. 

Until a user can click "Join" on a national website and instantly receive a working digital card, or click "Borrow" and have a physical hold placed on their local authority LMS or open an e-book in their browser, national platforms will inevitably act as signposts rather than services.

### 2. The Contrast Between England and Its Neighbors
The divergence between UK nations is instructive:
- In the **Republic of Ireland**, the Local Government Management Agency (LGMA) centrally procured a single shared LMS (**Libraries Ireland**, running Innovative Sierra) across all 31 local authorities. Every citizen holds a single card capable of reserving any book from any public library across the entire country with centralized courier delivery.
- In **Scotland**, the Scottish Library and Information Council (SLIC) facilitated consortia-level LMS sharing across multiple local authorities.
- In **Northern Ireland**, Libraries NI operates as a single regional authority with a single unified catalog.
- In **England**, 151 separate local authorities remain bound to individual council procurement frameworks, meaning shared infrastructure requires voluntary consensus rather than statutory alignment.

### 3. Open Data is the Only Infrastructure That Survives
Centralized platforms and government programs come and go with funding cycles. The MLA was abolished; the Culture Grid was retired; Bookmark Your Library was shuttered; LibraryOn's capital delivery period has now concluded.

What endures through all of these transitions is **standardized open data**. 

When library locations, opening times, unique identifiers, and catalog holdings are exposed via open, machine-readable standards under permissive licenses, the ecosystem does not collapse when a project ends. Third-party developers, community advocates, transport apps, and local authorities can continue building upon that foundation.

---

## Relevant Policy Archive Reports

Every key milestone cited in this article is fully transcribed, catalogued, and openly readable in the [UK Public Library Policy Archive](https://github.com/LibrariesHacked/uk-public-library-policy-archive):

* **1997**: [New Library: The People's Network](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/lic-new-library-the-peoples-network-1997/report.md) — *Library and Information Commission*
* **1998**: [Building the New Library Network](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/lic-building-the-new-library-network-1998/report.md) — *Library and Information Commission*
* **2003**: [Framework for the Future: 10 Year Vision](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/dcms-framework-for-the-future-2003/report.md) — *DCMS*
* **2014**: [Independent Library Report for England (The Sieghart Review)](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/independent-library-report-for-england-2014/report.md) — *William Sieghart / DCMS*
* **2015**: [Essential Digital Infrastructure for Public Libraries in England](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/scl-essential-digital-infrastructure-2015/report.md) — *BiblioCommons / Society of Chief Librarians*
* **2016**: [Libraries Deliver: Ambition for Public Libraries in England 2016–2021](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/libraries-taskforce-ambition-action-plan-2016/report.md) — *Libraries Taskforce*
* **2019**: [Digital Transformation for UK Public Libraries: Five Approaches to a 'Single Digital Presence'](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/single-digital-presence-scoping-report/report.md) — *The British Library / Arts Council England / Carnegie UK Trust*
* **2026**: [LibraryOn Programme Evaluation: Shaping the Single Digital Presence for Libraries](https://github.com/LibrariesHacked/uk-public-library-policy-archive/tree/main/archive/reports/single-digital-presence-programme-report/report.md) — *The British Library / Arts Council England*
