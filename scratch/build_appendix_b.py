"""Build structured Markdown tables for Appendix B (Pages 55-59).
"""
import re
from pathlib import Path
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

part3 = "archive/reports/dcms-framework-for-the-future-2003/source/Framework_for_the_Future3.pdf"
pages = list(extract_pages(part3))

# Page 55: Project Stakeholder Group
p55_table = """<!-- PAGE: 55 -->

## Appendix B -- Acknowledgments

In July 2002 the Department for Culture, Media and Sport set up a project stakeholder group with the following terms of reference 'to guide the DCMS in the development of a new strategic framework for the public library service'. Membership of the group is set out below.

| Name | Role | Organisation |
| :--- | :--- | :--- |
| Alex Stewart (Chair) | Director, Museums, Galleries, Libraries & Heritage Group | Department for Culture, Media and Sport |
| Chris Batt | Director, Libraries and Information Society Team | Resource: The Council for Museums, Archives and Libraries |
| Tony Belmega | Assistant Director, Policy and Development and Head of Adult Learning | Learning and Skills Council |
| Margaret Bennett | Head of Lifelong Learning and Technologies | Department for Education and Skills |
| Jon Boagey | Head of Information Services | National Youth Agency |
| Lyn Brown | Chair of Cultural Services Executive | Local Government Association |
| John Hicks | Chairman | Advisory Council on Libraries |
| Julie Hill | Senior Project Officer | Local Government Association |
| Bill Macnaught | Head of Cultural Development | Gateshead Council |
| Bob McKee | Chief Executive | CILIP |
| Martin Molloy | Director of Libraries and Heritage | Derbyshire County Council |
| Miranda McKearney | Director | The Reading Agency |
| Neil McClelland | Director | National Literacy Trust |
| Graham Walker | Director of the Central Strategy Unit | Office of the e-Envoy |
| Alan Wells | Director | The Basic Skills Agency |
| Janet Evans | Head of Museums, Libraries and Archives Division | Department for Culture, Media and Sport |
| Mandy Barrie | Head of Libraries and ICT Development Branch | Department for Culture, Media and Sport |
| Peter Beauchamp | Chief Library Adviser | Department for Culture, Media and Sport |
| Roger Stratton-Smith | Head of Local Government Team, Libraries, Local Regional and International Division | Department for Culture, Media and Sport |
| Alex Petrovic (Secretary) | Policy Adviser, Libraries and ICT Development Branch | Department for Culture, Media and Sport |"""

# Page 56: Advisory Council on Libraries + start of general contributors
p56_table = """<!-- PAGE: 56 -->

The Department for Culture, Media and Sport would like to thank the members of the Advisory Council on Libraries (ACL) for their advice and guidance. Membership of the ACL is set out below.

| Name | Role | Organisation |
| :--- | :--- | :--- |
| John Hicks (Chairman) | Chairman | Advisory Council on Libraries |
| Chris Batt | Director, Libraries and Information Society Team | Resource: The Council for Museums, Archives and Libraries |
| Keith Crawshaw | Head of Leisure Services | Sheffield City Council |
| David Ball | Associate Head of Academic Services | Bournemouth University |
| Rob Froud | County Librarian | Somerset County Council |
| Graham Bulpitt | Director, Learning Centre and University Librarian | Sheffield Hallam University |
| Shelagh Levett | Head of Arts, Library and Museum Services | Bournemouth Borough Council |
| Bob McKee | Chief Executive | CILIP |
| Martin Molloy | Director of Libraries and Heritage | Derbyshire County Council |
| Guenever Pachent | Assistant Director (Libraries and Heritage) | Suffolk County Council |
| David Ruse | Assistant Director, Lifetime Learning | Westminster City Council |
| Brian Stevenson | Commissioning Inspector | Audit Commission |
| Rob Warburton | Assistant Head of Cultural Services | Kirklees Metropolitan District Council |

The Department for Culture, Media and Sport would also like to thank the following people for their assistance in the development of the new strategic framework for public libraries.

| Name | Role | Organisation |
| :--- | :--- | :--- |
| David Anderson | Director of Learning and Interpretation | Victoria and Albert Museum |
| Brian Ashley | Assistant Director (Libraries, Information and Museums) | Nottingham City Council |
| Andrea Barker | Head of Cultural Services | Stockton on Tees Borough Council |
| Micheline Beaulieu | Head, Department of Information Studies | The University of Sheffield |
| Greg Birdseye | Associate Director, Public Services Research | Audit Commission |
| Catherine Blanshard | Head of Library and Information Service | Leeds City Council |
| Eric Bohl | Corporate Director (Customer Services) | London Borough of Tower Hamlets |"""

# Page 57: General contributors
p57_table = """<!-- PAGE: 57 -->

| Name | Role | Organisation |
| :--- | :--- | :--- |
| Steve Bundred | Chief Executive | London Borough of Camden |
| Tim Coates | Independent Consultant | |
| Sheila Corrall | Director of Academic Services | The University of Southampton |
| Hilary Cottam | Director -- Learning and Public Services | The Design Council |
| Margaret Croucher | Research Programme Manager | Resource: The Council for Museums, Archives and Libraries |
| Kate Davenport | Head of Libraries | Bristol City Council |
| Ray De Graff | ICT Strategy Officer | North Yorkshire County Council |
| Jonathan Douglas | Adviser for Youth and School Libraries | CILIP |
| Shiraz Durrani | Strategy and Commissioning Officer, Merton Libraries | London Borough of Merton |
| Diana Edmonds | Managing Director | Instant Library Ltd |
| Judith Elkin | Dean of Faculty, Computing, Information and English | University of Central England |
| Annie Everall | Service Manager, Young People & Policy Development | Derbyshire Libraries and Heritage Department |
| Ian Everall | Black Country ICT Co-ordinator | Black Country Consortium |
| Pat Flynn | Head of Library and Information Services | Leicester City Council |
| Tom Forrest | Director | Opening the Book |
| Kathleen Frenchman | Liaison Officer | Libraries for Life for Londoners |
| Fred Garnett | Head of Community Programmes | BECTA (British Educational Communications and Technology Agency) |
| Sue Greenfield | Divisional Librarian | Hampshire County Council |
| Viv Griffiths | Board Member | Resource: The Council for Museums, Archives and Libraries |
| Jane Hall | Head of Libraries, Arts and Information | Sunderland Metropolitan District Council |
| Kevin Harris | Information Manager | Community Development Foundation |
| Ruth Harrison | Project Manager | The Reading Agency |
| David Haynes | Head of CILIP Consultancy Services | CILIP |"""

# Page 58: General contributors
p58_table = """<!-- PAGE: 58 -->

| Name | Role | Organisation |
| :--- | :--- | :--- |
| Debbie Hicks | Policy and Strategy | The Reading Agency |
| Jennifer Holland | Head of Libraries and Information | Norfolk County Council |
| Mike Hosking | Head of Libraries and Information Services | Cambridgeshire County Council |
| Natasha Innocent | Reader Development Project Manager | London Libraries Development Agency |
| Ian M. Johnson | Head of the School of Information and Media | The Robert Gordon University, Aberdeen |
| Pam Jones | Learning Resource Manager | Knowsley Library Service |
| Brian King | Strategic Policy Advisor | Audit Commission Inspection Service |
| Trevor Knight | Executive Head of Library, Heritage and Registration Services | London Borough of Sutton |
| David Lindley | Sales and Marketing Director | Books for Students |
| Joyce Little | Head of Libraries and Information Services | Liverpool City Council |
| Brian Loader | Director, Community Informatics Research & Applications Unit (CIRA) | University of Teesside |
| Lindsay Mackie | Director | Diana, Princess of Wales Memorial Award for Young People |
| Peter Marchant | Head of Libraries | Knowsley Metropolitan Borough Council |
| Roger McMaster | County Manager for Suffolk Libraries and Heritage | Suffolk County Council |
| Norma Monks | Assistant Director of Culture, Leisure and Sport | Blackburn with Darwen Borough Council |
| David Murray | Director | London Libraries Development Agency |
| Julia Newton | Head of Libraries and Information Service | London Borough of Lewisham |
| Janet O'Hehir | Lending Time Project Director | CSV |
| John Pateman | Head of Libraries and Heritage Services | London Borough of Merton |
| Jenny Poad | Library Services Manager | Bedfordshire County Council |
| David Potts | Senior Network Adviser | Resource: The Council for Museums, Archives and Libraries |"""

# Page 59: General contributors
p59_table = """<!-- PAGE: 59 -->

| Name | Role | Organisation |
| :--- | :--- | :--- |
| John Readman | Head of Libraries, Archives and Arts | London Borough of Lambeth |
| Geoff Smith | Head of Cooperation and Partnerships | The British Library |
| Rachel Smith | Senior Policy Adviser, Central Strategy Unit | Office of the e-Envoy |
| Bjarne Stenquist | Consultant | |
| Paul Sternberg | Education Editor, Interactive | Channel 4 |
| Mark Taylor | Library & Information Services Manager | Royal Borough of Windsor and Maidenhead |
| John Turner | Service Manager | Nottingham Central Library |
| June Turner | Reader Development Coordinator for Essex Libraries | Essex County Council |
| Pam Usher | Head of Cultural Services | London Borough of Barnet |
| Bob Usherwood | Professor of Librarianship, Department of Information Studies | The University of Sheffield |
| Rachel van Riel | Director | Opening the Book |
| John Vincent | Networker | The Network -- tackling social exclusion in libraries, museums, archives and galleries |
| Robert Walters | Principal Librarian, Support Services | Bradford City Metropolitan Council |
| Heather Wills | Idea Store Programme Director | London Borough of Tower Hamlets |
| Ken Worpole | Independent Writer and Policy Consultant | |
| Eric Wright | County Libraries and Information Officer | Northamptonshire County Council |
| Chris Yapp | Client Principal | HP Global Services |"""

# Page 60: Imprint / Back cover
p60_imprint = """<!-- PAGE: 60 -->

PP496  
**Department for Culture, Media and Sport**  
2-4 Cockspur Street  
London SW1Y 5DH  
www.culture.gov.uk  
*February 2003*
"""

def update_appendix_b():
    report_path = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")
    text = report_path.read_text(encoding="utf-8")
    
    # Replace from Page 55 onwards
    pattern = r"<!-- PAGE: 55 -->.*"
    replacement = f"{p55_table}\n\n{p56_table}\n\n{p57_table}\n\n{p58_table}\n\n{p59_table}\n\n{p60_imprint}"
    new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)
    report_path.write_text(new_text, encoding="utf-8")
    print("Appendix B and Page 60 updated successfully.")

if __name__ == "__main__":
    update_appendix_b()
