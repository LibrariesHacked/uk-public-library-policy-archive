import subprocess
from pathlib import Path

content = subprocess.check_output(['git', 'show', 'HEAD:catalogue/planned-reports.yaml'], text=True, encoding='utf-8')

# Normalize newlines
content = content.replace("\r\n", "\n")

target1 = """  - id: dcms-framework-for-the-future-2003
    title: "Framework for the Future: Libraries, Learning and Information in the Next Decade"
    short_title: "Framework for the Future (2003)"
    year: 2003
    publisher: "Department for Culture, Media and Sport"
    country: "England"
    category: "ENGLAND"
    document_type: "strategy"
    verified: false
    status: planned"""

rep1 = """  - id: dcms-framework-for-the-future-2003
    title: "Framework for the Future: Libraries, Learning and Information in the Next Decade"
    short_title: "Framework for the Future (2003)"
    year: 2003
    publisher: "Department for Culture, Media and Sport"
    country: "England"
    category: "ENGLAND"
    document_type: "strategy"
    verified: true
    status: archived
    archived_id: dcms-framework-for-the-future-2003"""

if target1 not in content:
    raise ValueError("Target 1 not found in planned-reports.yaml")
content = content.replace(target1, rep1, 1)

target2 = """  - id: independent-library-report-for-england-2014
    title: "Independent Library Report for England"
    short_title: "Independent Library Report for England (2014)"
    year: 2014
    publisher: "Department for Culture, Media and Sport"
    country: "England"
    category: "ENGLAND"
    document_type: "independent-review"
    verified: false
    status: planned"""

rep2 = """  - id: independent-library-report-for-england-2014
    title: "Independent Library Report for England"
    short_title: "Independent Library Report for England (2014)"
    year: 2014
    publisher: "Department for Culture, Media and Sport"
    country: "England"
    category: "ENGLAND"
    document_type: "independent-review"
    verified: true
    status: archived
    archived_id: independent-library-report-for-england-2014"""

if target2 not in content:
    raise ValueError("Target 2 not found in planned-reports.yaml")
content = content.replace(target2, rep2, 1)

Path("catalogue/planned-reports.yaml").write_text(content, encoding="utf-8")
print("Successfully restored and updated catalogue/planned-reports.yaml!")

