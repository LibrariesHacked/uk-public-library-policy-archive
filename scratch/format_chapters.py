"""Formulate all chapters of Framework for the Future cleanly.
"""
import re
from pathlib import Path

FILE_PATH = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

def format_all():
    text = FILE_PATH.read_text(encoding="utf-8")

    # 1. Title page (Page 1)
    title_page = """<!-- PAGE: 1 -->

# Framework for the Future

## Libraries, Learning and Information in the Next Decade

**Department for Culture, Media and Sport**  
*February 2003*"""

    text = re.sub(r"<!-- PAGE: 1 -->.*?<!-- PAGE: 2 -->", f"{title_page}\n\n<!-- PAGE: 2 -->", text, flags=re.DOTALL)

    # 2. Table of Contents (Page 3)
    toc = """<!-- PAGE: 3 -->

## Contents

- [Foreword by Minister of State for the Arts](#page-4) (p. 4)
- [Executive Summary](#page-6) (p. 6)
- [1 Introduction](#page-12) (p. 12)
- [2 The Position of Libraries](#page-14) (p. 14)
- [3 Libraries' Modern Mission](#page-21) (p. 21)
- [4 Books, Reading and Learning](#page-24) (p. 24)
- [5 Digital Citizenship](#page-34) (p. 34)
- [6 Community and Civic Values](#page-38) (p. 38)
- [7 Delivering Change](#page-43) (p. 43)
- [Appendix A -- Glossary](#page-52) (p. 52)
- [Appendix B -- Acknowledgments](#page-55) (p. 55)"""

    text = re.sub(r"<!-- PAGE: 3 -->.*?<!-- PAGE: 4 -->", f"{toc}\n\n<!-- PAGE: 4 -->", text, flags=re.DOTALL)

    # 3. Foreword ending (Page 5)
    text = text.replace("\nTESSA BLACKSTONE\n", "\n**Tessa Blackstone**\n")

    # 4. Convert all bare numbered paragraphs to bold numbers:
    # Pattern: ^(\d+\.\d+)\s+ or ^(\d+\.)\s+ (at start of line)
    # We will process line by line
    new_lines = []
    lines = text.splitlines()
    for l in lines:
        s = l.strip()
        # e.g. "1.1  Our public..." -> "**1.1** Our public..."
        m = re.match(r"^(\d+\.\d+)\s+(.*)$", s)
        if m:
            new_lines.append(f"**{m.group(1)}** {m.group(2)}")
            continue
        # e.g. "1.  Libraries are..." or "1. Libraries are..."
        m2 = re.match(r"^(\d+)\.\s+(.*)$", s)
        if m2 and not s.startswith("-"):
            new_lines.append(f"**{m2.group(1)}.** {m2.group(2)}")
            continue
        new_lines.append(l)

    text = "\n".join(new_lines)

    # 5. Format known case studies / sidebars as blockquotes
    # Bournemouth case study (Page 14)
    bm_case = """> ### Case Study: Bournemouth Central Library
>
> Bournemouth's new Central Library is based in a bold, light, open modern building. It is already starting to change the town.
>
> There are fifty personal computers dotted around the building. In the foyer is a new café. An express area is designed for people to browse and choose from the most popular material, which includes videos, DVDs, CDs, as well as books. Teenagers gather in an area that they helped to design. The building is light but quiet and so an excellent place for learning. A large proportion of the people coming into the library use it for study in the broadest sense of the word, rather than to take out books. Since the opening visitor numbers have more than doubled. Book issues have risen by about 10%. The computers are used for about 2,500 hours a week.
>
> The South East England Regional Development Agency is studying plans to create a pedestrian piazza outside the library, which could be used for cultural events. That in turn is attracting local businesses. Investment in public space is creating the backdrop for economic growth.
>
> The new library building has been funded through a Private Finance Initiative scheme.
>
> *Bournemouth Central Library courtesy of Bournemouth Libraries, Leisure and Tourism Directorate. Photographer: John Tardiff of Arthouse.*"""

    text = re.sub(r"Bournemouth's new Central Library is based in a bold.*?\*?Photographer: John Tardiff of Arthouse\.\*?", bm_case, text, flags=re.DOTALL)

    # Idea Store case study (Page 21)
    idea_case = """> ### Case Study: Idea Stores in Tower Hamlets
>
> The London Borough of Tower Hamlets council wants to create a network of Idea Stores to replace traditional library buildings. The aim is to create an innovative and welcoming environment in which people can learn, browse and relax. Idea Stores combine public library services with adult education courses, community information, cafes and meeting spaces in accessible, high-footfall retail locations.
>
> The first Idea Store opened at Bow in 2002. It is open 7 days a week, including evenings. Visitor numbers and book loans have increased substantially compared with the libraries it replaced, with strong uptake among young people and local ethnic minority communities.
>
> *Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*"""

    text = re.sub(r"The London Borough of Tower Hamlets council wants to create.*?\*?Courtesy of London Borough of Tower Hamlets\.\*?", idea_case, text, flags=re.DOTALL)

    # Norfolk & Norwich case study (Page 18)
    norfolk_case = """> ### Case Study: Norfolk & Norwich Millennium Library
>
> The Norfolk & Norwich Millennium Library is largely open plan and includes a ground floor express library, a children's library, a business information centre and a local studies library. The library has 130 public-access computers with high-speed internet access. It is located within The Forum, a landmark landmark building in the centre of Norwich that also houses tourist information and broadcast studios.
>
> *Library users at the Norfolk & Norwich Millennium Library. Courtesy of Norfolk County Council.*"""

    text = re.sub(r"The Norfolk & Norwich Millennium Library is largely open plan.*?\*?Courtesy of Norfolk County Council\.\*?", norfolk_case, text, flags=re.DOTALL)

    # Subheadings within chapters
    text = text.replace("\nHistoric strengths, future potential\n", "\n### Historic strengths, future potential\n")
    text = text.replace("\nQuality book stock\n", "\n### Quality book stock\n")
    text = text.replace("\nThe importance of reading\n", "\n### The importance of reading\n")
    text = text.replace("\nConstraints and challenges\n", "\n### Constraints and challenges\n")
    text = text.replace("\nInnovation\n", "\n### Innovation\n")
    text = text.replace("\nPotential\n", "\n### Potential\n")

    FILE_PATH.write_text(text, encoding="utf-8")
    print(f"Updated {FILE_PATH}")

if __name__ == "__main__":
    format_all()
