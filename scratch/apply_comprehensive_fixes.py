"""Comprehensive script to apply all requested refinements to dcms-framework-for-the-future-2003:

1. Seamless page markers within split paragraphs (Page 6->7, Page 7->8, Page 9->10, Page 15->16).
2. Embed all content images (Pages 4, 5, 13, 14, 15, 18, 21, 39, 41, 42).
3. Fix '## 7 Delivering Change' heading on Page 43.
4. Format standalone headings in Chapter 7 (### Greater recognition..., ### Better sectoral leadership...).
5. Bold all terms in Appendix A Glossary.
6. Format Appendix B Acknowledgments into 3-column Markdown tables.
"""
import re
from pathlib import Path

FILE_PATH = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

def run():
    text = FILE_PATH.read_text(encoding="utf-8")

    # 1. Seamless page markers within split paragraphs
    # Page 6 -> 7
    old_p6_7 = """**8.** But the innovation is not evenly spread and is frequently local and fragile. There are 149 library\n\n<!-- PAGE: 7 -->\n\nauthorities operating through 3,500 public libraries"""
    new_p6_7 = """**8.** But the innovation is not evenly spread and is frequently local and fragile. There are 149 library\n<!-- PAGE: 7 -->\nauthorities operating through 3,500 public libraries"""
    text = text.replace(old_p6_7, new_p6_7)

    # Page 7 -> 8
    old_p7_8 = """**15.** This matters because reading is ever more critical in a knowledge-driven society. Most\n\n<!-- PAGE: 8 -->\n\nweb pages are text based."""
    new_p7_8 = """**15.** This matters because reading is ever more critical in a knowledge-driven society. Most\n<!-- PAGE: 8 -->\nweb pages are text based."""
    text = text.replace(old_p7_8, new_p7_8)

    # Page 9 -> 10
    old_p9_10 = """**29.** Library authorities need to survey and review the needs of the communities they serve,\n\n<!-- PAGE: 10 -->\n\nfocusing particularly on the needs of the excluded."""
    new_p9_10 = """**29.** Library authorities need to survey and review the needs of the communities they serve,\n<!-- PAGE: 10 -->\nfocusing particularly on the needs of the excluded."""
    text = text.replace(old_p9_10, new_p9_10)

    # Page 15 -> 16
    old_p15_16 = """Library services run a wide\n\n<!-- PAGE: 16 -->\n\nrange of programmes designed to encourage reading"""
    new_p15_16 = """Library services run a wide\n<!-- PAGE: 16 -->\nrange of programmes designed to encourage reading"""
    text = text.replace(old_p15_16, new_p15_16)

    # 2. Embed images
    # Page 4: Tessa Blackstone portrait
    p4_intro = """## Foreword by Minister of State for the Arts\n\n![Tessa Blackstone](assets/figure-004.jpg)\n\n*Tessa Blackstone, Minister of State for the Arts*\n\nGoing to the library"""
    text = re.sub(r"## Foreword by Minister of State for the Arts\s+Going to the library", p4_intro, text)

    # Page 5: Tessa Blackstone signature
    p5_sig = """![Tessa Blackstone signature](assets/figure-005-signature.jpg)\n\n**Tessa Blackstone**"""
    text = text.replace("**Tessa Blackstone**", p5_sig)

    # Page 13: Sutton library photo
    sutton13_old = "Supporting early learning. Courtesy of London Borough of Sutton Library, Heritage and Registration Services."
    sutton13_new = "![Supporting early learning](assets/figure-013.jpg)\n\n*Supporting early learning. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.*"
    text = text.replace(sutton13_old, sutton13_new)

    # Page 14: Bournemouth Central Library photo (inside blockquote)
    bm_old = "*Bournemouth Central Library courtesy of Bournemouth Libraries, Leisure and Tourism Directorate. Photographer: John Tardiff of Arthouse.*"
    bm_new = "> ![Bournemouth Central Library](assets/figure-014.jpg)\n>\n> *Bournemouth Central Library courtesy of Bournemouth Libraries, Leisure and Tourism Directorate. Photographer: John Tardiff of Arthouse.*"
    text = text.replace(bm_old, bm_new)

    # Page 15: Promoting reading photo
    sutton15_old = "Promoting reading. Courtesy of London Borough of Sutton Library, Heritage and Registration Services."
    sutton15_new = "![Promoting reading](assets/figure-015.jpg)\n\n*Promoting reading. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.*"
    text = text.replace(sutton15_old, sutton15_new)

    # Page 18: Norfolk & Norwich photo (inside blockquote)
    norwich_old = "*Library users at the Norfolk & Norwich Millennium Library. Courtesy of Norfolk Library and Information Service. Photographer: Jacqueline Wyatt Photography.*"
    norwich_new = "> ![Norfolk & Norwich Millennium Library](assets/figure-018.jpg)\n>\n> *Library users at the Norfolk & Norwich Millennium Library. Courtesy of Norfolk Library and Information Service. Photographer: Jacqueline Wyatt Photography.*"
    text = text.replace(norwich_old, norwich_new)

    # Page 21: Idea Store photo (inside blockquote)
    idea_old = "*Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*"
    idea_new = "> ![Prototype Idea Store at Bow](assets/figure-021.jpg)\n>\n> *Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*"
    text = text.replace(idea_old, idea_new)

    # Page 41: Fazakerley photo
    faz_old = "Fazakerley Community Library. Courtesy of Liverpool Libraries"
    # check how it appears on page 41
    text = re.sub(r"Fazakerley Community Library\. Courtesy of Liverpool Libraries[^\n]*", "![Fazakerley Community Library](assets/figure-041.jpg)\n\n*Fazakerley Community Library. Courtesy of Liverpool Libraries and Information Services.*", text)

    # Page 42: Cookham photo
    cook_old = "Cookham Library. Courtesy of Royal Borough of Windsor and Maidenhead"
    text = re.sub(r"Cookham Library\. Courtesy of Royal Borough of Windsor and Maidenhead[^\n]*", "![Cookham Library](assets/figure-042.jpg)\n\n*Cookham Library. Courtesy of Royal Borough of Windsor and Maidenhead Library Service.*", text)

    # 3. Fix '## Delivering Change\n\n7' -> '## 7 Delivering Change'
    text = re.sub(r"## Delivering Change\s+7\s+\*\*7\.1\*\*", "## 7 Delivering Change\n\n**7.1**", text)

    # 4. Format standalone headings in Chapter 7
    text = text.replace("\nGreater recognition by central government\n", "\n### Greater recognition by central government\n")
    text = text.replace("\nBetter sectoral leadership at national and local level\n", "\n### Better sectoral leadership at national and regional level\n")

    # 5. Bold all terms in Appendix A Glossary
    glossary_terms = [
        "Advisory Council on Libraries (ACL)",
        "Annual Library Plans (ALPs)",
        "Beacon Libraries",
        "Booktrust",
        "The Chartered Institute of Library and Information Professionals (CILIP)",
        "Culture Online",
        "The Department for Culture, Media and Sport (DCMS)",
        "DCMS/Wolfson Public Libraries Challenge Fund",
        "The Department for Education and Skills (DfES)",
        "Learndirect/University for industry (Ufi)",
        "Learning and Skills Council (LSC)",
        "London Libraries Development Agency (LLDA)",
        "National Literacy Trust",
        "North East Museums, Libraries and Archives Council (NEMLAC)",
        "Opening the Book Ltd",
        "The People's Network",
        "Public Library Service",
        "Public Library Standards",
        "The Reading Agency (TRA)",
        "Resource: The Council for Museums, Archives and Libraries",
        "School Library Services",
        "South East Museum, Library & Archive Council (SEMLAC)",
        "Society of Chief Librarians (SCL)",
        "Sure Start",
        "UK online",
    ]
    for term in glossary_terms:
        # Bold term at start of line
        text = re.sub(rf"\n{re.escape(term)}\s+", f"\n**{term}** ", text)

    FILE_PATH.write_text(text, encoding="utf-8")
    print("Applied refinements 1-5.")

if __name__ == "__main__":
    run()
