import re
from pathlib import Path

path = Path('archive/reports/dcms-framework-for-the-future-2003/report.md')
content = path.read_text(encoding='utf-8')
newline = '\r\n' if '\r\n' in content else '\n'
norm_content = content.replace('\r\n', '\n')

replacements = []

# 1. Page 6 -> 7: Paragraph 8 inline
t_p8 = (
    "**8.** But the innovation is not evenly spread and is frequently local and fragile. "
    "There are 149 library authorities operating through 3,500 public libraries, including mobile services. "
    "It is difficult for national policy makers to communicate with the public library service as a whole "
    "and opportunities for local innovation to be translated into national programmes which attract public funding may be lost.\n\n"
    "<!-- PAGE: 7 -->\n\n"
    "**9.** Fragmentation"
)
r_p8 = (
    "**8.** But the innovation is not evenly spread and is frequently short-lived because of a number of constraints. "
    "The public library service in England is run by 149 separate library <!-- PAGE: 7 --> authorities operating through 3,500 "
    "public libraries, including mobile services. It is difficult for national policy makers to communicate with the "
    "public library service as a whole and opportunities for local innovation to be translated into national programmes "
    "which attract public funding may be lost.\n\n"
    "**9.** Fragmentation"
)
replacements.append(("Page 6->7 P8", t_p8, r_p8))

# 2. Page 7 -> 8: Paragraph 15 inline
t_p15 = (
    "<!-- PAGE: 8 -->\n\n"
    "**15.** This matters because reading is ever more important in modern life. The rise of the internet has not displaced reading since most web pages are text based."
)
r_p15 = (
    "**15.** This matters because reading is ever more important in modern life. The rise of the internet has not displaced reading since most <!-- PAGE: 8 --> web pages are text based."
)
replacements.append(("Page 7->8 P15", t_p15, r_p15))

# 3. Page 9 -> 10: Paragraph 29 restored and inline
t_p29 = (
    "**29.** Library authorities need to survey and review the needs of the communities they serve, focusing particularly on the needs of the excluded.\n\n"
    "<!-- PAGE: 10 -->\n\n"
    "### Delivering Change"
)
r_p29 = (
    "**29.** Library authorities need to survey and review the needs of the communities they serve, <!-- PAGE: 10 --> "
    "focusing particularly on the needs of the people who do not currently use libraries but might be attracted to do so "
    "and might disproportionately benefit from the services on offer. They should be considered as a means of developing "
    "and implementing the local authority community strategy.\n\n"
    "### Delivering Change"
)
replacements.append(("Page 9->10 P29", t_p29, r_p29))

# 4. Page 15 -> 16: Paragraph 2.5 inline
t_p2_5 = (
    "Library services run a wide range of programmes designed to encourage reading especially among pre-school children, "
    "such as Bookstart, where libraries work with health visitors to provide parents and babies with packs of reading materials. "
    "Libraries provide services for local businesses, prisons and young offenders institutions, schools developing reading "
    "programmes and social services departments working with young people in care or old people who are housebound. "
    "Libraries are not just buildings. They are increasingly vital service centres for a host of information-related needs.\n\n"
    "<!-- PAGE: 16 -->\n\n"
    "**2.6** Finally"
)
r_p2_5 = (
    "Library services run a wide <!-- PAGE: 16 --> range of programmes designed to encourage reading especially among "
    "pre-school children, such as Bookstart, where libraries work with health visitors to provide parents and babies "
    "with packs of reading materials. Libraries provide services for local businesses, prisons and young offenders "
    "institutions, schools developing reading programmes and social services departments working with young people in "
    "care or old people who are housebound. Libraries are not just buildings. They are increasingly vital service "
    "centres for a host of information-related needs.\n\n"
    "**2.6** Finally"
)
replacements.append(("Page 15->16 P2.5", t_p2_5, r_p2_5))

# 5. Page 36: Bullet list continuity across page 36
t_p36 = (
    "- Online information services: libraries are using the internet to deliver their own existing services in new ways. As a result they are creating new online communities and activities\n"
    "<!-- PAGE: 36 -->\n"
    "- Content creation:"
)
r_p36 = (
    "- Online information services: libraries are using the internet to deliver their own existing services in new ways. As a result they are creating new online communities and activities <!-- PAGE: 36 -->\n"
    "- Content creation:"
)
replacements.append(("Page 35->36 list", t_p36, r_p36))

# 6. Page 36 -> 37: Online learning bullet line reunited
t_p37 = (
    "- Information: Resource will consider the scope for a national service to answer queries online that are often asked at libraries, building on local services such as Leeds' Enquiry Express and Gateshead's Ask a Librarian which allows enquirers to pose questions to librarians at any time and aims for a rapid response to all enquiries\n\n"
    "<!-- PAGE: 37 -->\n\n"
    "- Online learning: Resource will explore\n\n"
    "new opportunities for online learning such as the work currently in progress with learndirect to develop specially designed new learning services to be delivered through The People's Network."
)
r_p37 = (
    "- Information: Resource will consider the scope for a national service to answer queries online that are often asked at libraries, building on local services such as Leeds' Enquiry Express and Gateshead's Ask a Librarian which allows enquirers to pose questions to librarians at any time and aims for a rapid response to all enquiries\n"
    "- Online learning: Resource will explore <!-- PAGE: 37 --> new opportunities for online learning such as the work currently in progress with learndirect to develop specially designed new learning services to be delivered through The People's Network."
)
replacements.append(("Page 36->37 bullet", t_p37, r_p37))

# 7. Page 44: Central government bullets (line 808-810)
t_p44 = (
    "- Help identify libraries' key contribution to\n\n"
    "national and local priorities -   Set out a small number of national expectations for the public library service to deliver -   Clarify the links with the shared priorities for local government -   Encourage continuous improvement through performance management."
)
r_p44 = (
    "- Help identify libraries' key contribution to national and local priorities\n"
    "- Set out a small number of national expectations for the public library service to deliver\n"
    "- Clarify the links with the shared priorities for local government\n"
    "- Encourage continuous improvement through performance management."
)
replacements.append(("Page 44 Central Gov bullets", t_p44, r_p44))

# 8. Page 49 -> 50: Paragraph 7.44 and 7.45 and case studies
t_p50 = (
    "Developing a new relationship with the business community\n\n"
    "**7.43** We believe there is scope for public libraries to develop mutually beneficial partnerships with those businesses that recognise the importance of corporate social responsibility. Libraries provide an excellent means for such companies to implement CSR programmes aimed at supporting local communities, lifelong learning and combating social exclusion.\n\n"
    "**7.44** Innovative libraries, often supported by The Reading Agency, have had some considerable success over recent years in attracting private sponsorship to their activities. The case study examples demonstrate some of the opportunities which exist for libraries to work with publishers, booksellers, authors and private sponsors to support reading promotion. Such partnership and sponsorship arrangements deliver much more than the\n\n"
    "<!-- PAGE: 50 -->\n\n"
    "immediate goal of the project. Workplace based projects can help libraries reach new audiences. Business partnerships can bring with them development opportunities for library staff where, for example, librarians have been invited into business mentoring and skills enhancement programmes where a sharing of public and private sector expertise can be beneficial. These closer links also enable the library community to develop advocates within the business community.\n\n"
    "**7.45** Much is being done and more of this could be done. Links between private sponsors and literature are not as strong in other sectors of the arts world. The DCMS/Wolfson funded Books and Business programme is beginning to build a portfolio of business partnerships and The Reading Agency had included the During 2002 West Sussex Library Service installed ICT equipment offering free public internet access in its thirty-five libraries as part of The People's Network. The library service was able to publicise the launch of the new service to users and put in place a long-term marketing strategy to make non-library users aware of the service by drawing on the expertise of a marketing manager from a locally based firm. Networking body Arts and Business South East was able to broker the arrangement through the use of their skills bank database.\n\n"
    "The County Big Book scheme was a partnership between Cumberland Building Society and Cumbria County Council Education & Libraries. As part of their commitment to corporate social responsibility, the Cumberland Building Society wanted to support local initiatives that might not otherwise receive funding and so make a useful contribution to the local community. The Society also hoped that by demonstrating its commitment to regional activities it would be able to raise its public profile and present itself as a caring and ethical organisation.\n\n"
    "Working initially through the County Council's Education Department, the Society began to support the region's Arts in Education programme, which benefited schools, arts venues and libraries. One particularly successful initiative was the \"County Big Book\" project, a scheme involving primary schools in Cumbria and the Young People's Library Service. Schools were invited to compile their own \"Big Book\" of stories and contributions made by school children. These were submitted to a panel of judges who selected three winning books to be published and distributed around the county. As a result of the benefits it has enjoyed, the Society has now committed an ongoing donation from its annual profits to secure a continued involvement in local affairs.\n\n"
    "need to build reading inspired business partnerships as one of its key work strands."
)

r_p50 = (
    "### Developing a new relationship with the business community\n\n"
    "**7.43** We believe there is scope for public libraries to develop mutually beneficial partnerships with those businesses that recognise the importance of corporate social responsibility. Libraries provide an excellent means for such companies to implement CSR programmes aimed at supporting local communities, lifelong learning and combating social exclusion.\n\n"
    "**7.44** Innovative libraries, often supported by The Reading Agency, have had some considerable success over recent years in attracting private sponsorship to their activities. The case study examples demonstrate some of the opportunities which exist for libraries to work with publishers, booksellers, authors and private sponsors to support reading promotion. Such partnership and sponsorship arrangements deliver much more than the <!-- PAGE: 50 --> immediate goal of the project. Workplace based projects can help libraries reach new audiences. Business partnerships can bring with them development opportunities for library staff where, for example, librarians have been invited into business mentoring and skills enhancement programmes where a sharing of public and private sector expertise can be beneficial. These closer links also enable the library community to develop advocates within the business community.\n\n"
    "**7.45** Much is being done and more of this could be done. Links between private sponsors and literature are not as strong in other sectors of the arts world. The DCMS/Wolfson funded Books and Business programme is beginning to build a portfolio of business partnerships and The Reading Agency had included the need to build reading inspired business partnerships as one of its key work strands.\n\n"
    "> ### Case Study: West Sussex Library Service and Arts and Business\n"
    ">\n"
    "> During 2002 West Sussex Library Service installed ICT equipment offering free public internet access in its thirty-five libraries as part of The People's Network. The library service was able to publicise the launch of the new service to users and put in place a long-term marketing strategy to make non-library users aware of the service by drawing on the expertise of a marketing manager from a locally based firm. Networking body Arts and Business South East was able to broker the arrangement through the use of their skills bank database.\n\n"
    "> ### Case Study: The County Big Book Scheme (Cumberland Building Society & Cumbria)\n"
    ">\n"
    "> The County Big Book scheme was a partnership between Cumberland Building Society and Cumbria County Council Education & Libraries. As part of their commitment to corporate social responsibility, the Cumberland Building Society wanted to support local initiatives that might not otherwise receive funding and so make a useful contribution to the local community. The Society also hoped that by demonstrating its commitment to regional activities it would be able to raise its public profile and present itself as a caring and ethical organisation.\n"
    ">\n"
    "> Working initially through the County Council's Education Department, the Society began to support the region's Arts in Education programme, which benefited schools, arts venues and libraries. One particularly successful initiative was the \"County Big Book\" project, a scheme involving primary schools in Cumbria and the Young People's Library Service. Schools were invited to compile their own \"Big Book\" of stories and contributions made by school children. These were submitted to a panel of judges who selected three winning books to be published and distributed around the county. As a result of the benefits it has enjoyed, the Society has now committed an ongoing donation from its annual profits to secure a continued involvement in local affairs."
)
replacements.append(("Page 49->50 P7.44 and case studies", t_p50, r_p50))

for name, target, repl in replacements:
    assert target in norm_content, f"FAILED TO FIND TARGET for {name}"
    norm_content = norm_content.replace(target, repl, 1)
    print(f"Applied: {name}")

if newline == '\r\n':
    final_content = norm_content.replace('\n', '\r\n')
else:
    final_content = norm_content

path.write_text(final_content, encoding='utf-8')
print("All 8 structural and cross-page fixes applied successfully!")
