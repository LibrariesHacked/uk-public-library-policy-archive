from pathlib import Path
import re

path = Path('archive/reports/independent-library-report-for-england-2014/report.md')
content = path.read_text(encoding='utf-8')
newline = '\r\n' if '\r\n' in content else '\n'
norm = content.replace('\r\n', '\n')

# 1. Footnote 1: line 163
t1 = "This can build on the work from Library 211 which has begun to explore how"
r1 = "This can build on the work from Library 21[^1] which has begun to explore how"
assert t1 in norm
norm = norm.replace(t1, r1, 1)

# Remove raw definition 1
t1_def = "\n\n1 http://www.theliteraryplatform.com/collective/library-21-research-and-feasibility-study/\n\n"
assert t1_def in norm
norm = norm.replace(t1_def, "\n\n", 1)

# 2. Footnote 2: line 239
t2 = "The Cabinet Office's Digital Inclusion Strategy2 sets out how it will help"
r2 = "The Cabinet Office's Digital Inclusion Strategy[^2] sets out how it will help"
assert t2 in norm
norm = norm.replace(t2, r2, 1)

# Remove raw definition 2
t2_def = "\n\n2 https://www.gov.uk/government/publications/government-digital-inclusion-strategy\n\n"
assert t2_def in norm
norm = norm.replace(t2_def, "\n\n", 1)

# 3. Footnote 3: line 279
t3 = "Following our recommendations from the 2013 e-lending report3, the government"
r3 = "Following our recommendations from the 2013 e-lending report[^3], the government"
assert t3 in norm
norm = norm.replace(t3, r3, 1)

# Remove raw definition 3
t3_def = "\n\n3 https://www.gov.uk/government/publications/an-independent-review-of-e-lending-in-public-libraries-in-england\n\n"
assert t3_def in norm
norm = norm.replace(t3_def, "\n\n", 1)

# 4. Footnotes 4, 5, 6: lines 314-316
t4 = "- The Community Knowledge Hub for Libraries4\n- Learning from experience: guiding principles for local authorities5\n- Learning from experience: summary briefing for local authorities6"
r4 = "- The Community Knowledge Hub for Libraries[^4]\n- Learning from experience: guiding principles for local authorities[^5]\n- Learning from experience: summary briefing for local authorities[^6]"
assert t4 in norm
norm = norm.replace(t4, r4, 1)

# Remove raw definition 4, 5, 6
# Check exact string in norm
m = re.search(r'\n\n4 http://libraries\.communityknowledgehub\.org\.uk/.*?\n\n', norm)
assert m, "Failed to find raw def 4, 5, 6"
norm = norm[:m.start()] + "\n\n" + norm[m.end():]

# 5. Footnote 7: line 322
t7 = "- Rural library services in England: exploring recent changes and possible futures7"
r7 = "- Rural library services in England: exploring recent changes and possible futures[^7]"
assert t7 in norm
norm = norm.replace(t7, r7, 1)

# Remove raw definition 7
m7 = re.search(r'\n\n7 http://www\.opm\.co\.uk/publications/rural-library-services-in-england-exploring-recent-changes-and-possible-\s*futures/\n\n', norm)
assert m7, "Failed to find raw def 7"
norm = norm[:m7.start()] + "\n\n" + norm[m7.end():]

# 6. Footnote 8: line 350
t8 = "'to provide a comprehensive and efficient library service for all persons desiring to make use thereof'8 taking into account"
r8 = "'to provide a comprehensive and efficient library service for all persons desiring to make use thereof'[^8] taking into account"
assert t8 in norm
norm = norm.replace(t8, r8, 1)

# Remove raw definition 8
t8_def = "\n\n8 http://www.legislation.gov.uk/ukpga/1964/75/contents\n\n"
assert t8_def in norm
norm = norm.replace(t8_def, "\n\n", 1)

# 7. Footnote 9: line 376
t9 = "- The Mutuals Support Programme9 is a £10m fund to support services"
r9 = "- The Mutuals Support Programme[^9] is a £10m fund to support services"
assert t9 in norm
norm = norm.replace(t9, r9, 1)

# Remove raw definition 9
t9_def = "\n\n9 https://www.gov.uk/government/groups/mutuals-information-service\n\n"
assert t9_def in norm
norm = norm.replace(t9_def, "\n\n", 1)

# 8. Footnote 10: line 443
t10 = "The Access to Research initiative10 gives free, walk-in access"
r10 = "The Access to Research initiative[^10] gives free, walk-in access"
assert t10 in norm
norm = norm.replace(t10, r10, 1)

# Remove raw definition 10
t10_def = "\n\n10 http://www.accesstoresearch.org.uk/\n\n"
assert t10_def in norm
norm = norm.replace(t10_def, "\n\n", 1)

# Add ## Footnotes section at end of document
footnotes_section = """\n\n## Footnotes

[^1]: <http://www.theliteraryplatform.com/collective/library-21-research-and-feasibility-study/>
[^2]: <https://www.gov.uk/government/publications/government-digital-inclusion-strategy>
[^3]: <https://www.gov.uk/government/publications/an-independent-review-of-e-lending-in-public-libraries-in-england>
[^4]: <http://libraries.communityknowledgehub.org.uk/>
[^5]: <http://www.artscouncil.org.uk/advice-and-guidance/browse-advice-and-guidance/community-libraries-learning-experience-guiding-principles-local-authorities>
[^6]: <http://www.artscouncil.org.uk/media/uploads/pdf/Community_libraries_research_2013_summary_report.pdf>
[^7]: <http://www.opm.co.uk/publications/rural-library-services-in-england-exploring-recent-changes-and-possible-futures/>
[^8]: <http://www.legislation.gov.uk/ukpga/1964/75/contents>
[^9]: <https://www.gov.uk/government/groups/mutuals-information-service>
[^10]: <http://www.accesstoresearch.org.uk/>
"""

norm = norm.strip() + footnotes_section

if newline == '\r\n':
    final = norm.replace('\n', '\r\n')
else:
    final = norm

path.write_text(final, encoding='utf-8')
print("Successfully converted all 10 Sieghart footnotes into consolidated endnotes!")
