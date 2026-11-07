"""Applies final, complete diplomatic formatting to dcms-framework-for-the-future-2003.
"""
from pathlib import Path
import re

FILE_PATH = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

def apply_clean():
    text = FILE_PATH.read_text(encoding="utf-8")

    # 1. Restore 2.11 on Page 16
    para_2_11 = """**2.11** In future, libraries will have a critical role in helping promote greater equality of access to and capability in using information, engaging in learning and acquiring knowledge. They will act as gateways to knowledge held in other institutions, such as universities and colleges, museums and archives as cultural and learning resources become more widely accessible. That will place new emphasis on the skills of librarians in understanding user needs and navigating through the resources to satisfy those needs."""
    
    if "**2.11**" not in text:
        text = text.replace(
            "**2.10** However, access to and the ability to use information and knowledge are not equally distributed. About seven million adults in England are judged to be functionally illiterate. Affluent families are far more likely to be able to give their children access to books, computers and the internet than poorer families. If we do not guard against it, the economic returns from knowledge and skills will go disproportionately to those groups and places that are already rich in both.",
            "**2.10** However, access to and the ability to use information and knowledge are not equally distributed. About seven million adults in England are judged to be functionally illiterate. Affluent families are far more likely to be able to give their children access to books, computers and the internet than poorer families. If we do not guard against it, the economic returns from knowledge and skills will go disproportionately to those groups and places that are already rich in both.\n\n" + para_2_11
        )

    # 2. Fix Page 14: separate 2.2 and Dyke House case study
    p14_old_fragment = """**2.2** First, libraries create, both within and without, spaces in which communities can flourish. There are some 3,500 public libraries in England including mobiles and those which open part time. In addition to this there are close to 17,000 service points including those in community centres, The Dyke House Community Library and Resource Centre was set up in Hartlepool twelve years ago on an estate with high unemployment, crime and many single parent families. The library now provides books including talking books, videos and CDs, as well as a home for a variety of community activities and courses and free advice on employment issues. The library in the Liverpool 8 Community Law Centre serves both users and lawyers and provides much needed quiet study space. Merton libraries run special projects for refugees and asylum seekers.

sheltered accommodation, playgroups, leisure centres and youth groups. Libraries are used for meetings, performances, displays, readings and debates. Indeed increasingly, good libraries are designed with that in mind. Well run libraries help create a sense of community. They are open to all, offer safe, welcoming space and support active citizenship. The recent Beacon Council programme on Libraries as a Community Resource highlighted this."""

    p14_clean = """**2.2** First, libraries create, both within and without, spaces in which communities can flourish. There are some 3,500 public libraries in England including mobiles and those which open part time. In addition to this there are close to 17,000 service points including those in community centres, sheltered accommodation, playgroups, leisure centres and youth groups. Libraries are used for meetings, performances, displays, readings and debates. Indeed increasingly, good libraries are designed with that in mind. Well run libraries help create a sense of community. They are open to all, offer safe, welcoming space and support active citizenship. The recent Beacon Council programme on Libraries as a Community Resource highlighted this.

> ### Case Study: Community Libraries
>
> The Dyke House Community Library and Resource Centre was set up in Hartlepool twelve years ago on an estate with high unemployment, crime and many single parent families. The library now provides books including talking books, videos and CDs, as well as a home for a variety of community activities and courses and free advice on employment issues.
>
> The library in the Liverpool 8 Community Law Centre serves both users and lawyers and provides much needed quiet study space. Merton libraries run special projects for refugees and asylum seekers."""

    text = text.replace(p14_old_fragment, p14_clean)

    # 3. Fix 6.10 on Page 41
    if "**6.10**" not in text:
        text = re.sub(
            r"6\.10Community strategies should be prepared",
            "**6.10** Community strategies should be prepared",
            text
        )

    # 4. Fix Barnet case study on Page 42
    barnet_old = """The London Borough of Barnet Library Service includes as a key service priority contributing to community safety, social cohesion and active citizenship. Initiatives include targeted study support and reading programmes, youth outreach work and a special service for the Iranian community."""
    barnet_clean = """> ### Case Study: Barnet Community Safety and Outreach
>
> The London Borough of Barnet Library Service includes as a key service priority contributing to community safety, social cohesion and active citizenship. Initiatives include targeted study support and reading programmes, youth outreach work and a special service for the Iranian community."""
    text = text.replace(barnet_old, barnet_clean)

    # 5. Fix subheadings across chapters
    subheads = [
        "Quality book stock",
        "The importance of reading",
        "Supporting early learning",
        "Supporting students and pupils",
        "Promoting adult literacy",
        "The role of the library service",
        "Broadband internet access",
        "Online learning and community content",
        "Partnerships with broadcasters and public bodies",
        "Revitalising buildings and physical spaces",
        "Social inclusion and reaching non-users",
        "Conclusions",
        "National leadership and regional capacity",
        "Planning, standards and inspection",
        "Working in partnership",
    ]
    for sh in subheads:
        # replace standalone line
        text = re.sub(rf"\n{re.escape(sh)}\n", f"\n### {sh}\n", text)

    # Clean multiple consecutive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    FILE_PATH.write_text(text, encoding="utf-8")
    print("Applied final clean successfully.")

if __name__ == "__main__":
    apply_clean()
