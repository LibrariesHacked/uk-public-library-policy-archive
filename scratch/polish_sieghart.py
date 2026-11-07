"""Format independent-library-report-for-england-2014 to updated diplomatic standards.
"""
from pathlib import Path
import re

p = Path("archive/reports/independent-library-report-for-england-2014/report.md")
text = p.read_text(encoding="utf-8")

# Title page
title_page = """<!-- PAGE: 1 -->

# Independent Library Report for England

**Department for Culture, Media & Sport**  
*18 December 2014*"""

text = re.sub(r"<!-- PAGE: 1 -->.*?<!-- PAGE: 2 -->", f"{title_page}\n\n<!-- PAGE: 2 -->", text, flags=re.DOTALL)

# Contents page
toc = """<!-- PAGE: 3 -->

## Contents

- [Foreword](#page-4) (p. 4)
- [Actions](#page-9) (p. 9)
- [Digital library network](#page-11) (p. 11)
- [Library taskforce](#page-14) (p. 14)
- [Wider government initiatives](#page-17) (p. 17)
- [E-lending](#page-19) (p. 19)
- [Professional development](#page-21) (p. 21)
- [Volunteers and community-led libraries](#page-22) (p. 22)
- [Role of local government](#page-24) (p. 24)
- [Case studies](#page-27) (p. 27)"""

text = re.sub(r"<!-- PAGE: 3 -->.*?<!-- PAGE: 4 -->", f"{toc}\n\n<!-- PAGE: 4 -->", text, flags=re.DOTALL)

# Recommendations
text = text.replace("1.  The provision of a national digital resource", "**1.** The provision of a national digital resource")
text = text.replace("2.  The setting up of a task and finish force", "**2.** The setting up of a task and finish force")
text = text.replace("3.  The task force, to work with local authorities", "**3.** The task force, to work with local authorities")

# Foreword signoff
text = text.replace("William Sieghart & Panel ─ Independent Library Report", "**William Sieghart & Panel**  \n*Independent Library Report*")

p.write_text(text, encoding="utf-8")
print("Polished Sieghart report.")
