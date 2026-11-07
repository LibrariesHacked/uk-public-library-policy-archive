"""Replace Executive Summary (Pages 6-11) with the exact, verified diplomatic text.
"""
from pathlib import Path
import re

FILE_PATH = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")

EXECUTIVE_SUMMARY = """<!-- PAGE: 6 -->

## Executive Summary

### Introduction

**1.** Libraries are a much valued public institution built around a shared ideal: to make available resources that can be used by all members of the community to stimulate imagination and inquiry, through literature and reference, for culture and commerce. They are open to all and should benefit most those least able to afford private provision.

**2.** More people go to the library than to cinemas or football grounds. The public library service is a huge asset handed down by generations of social reformers. Its role is just as relevant in the twenty-first century as in the nineteenth.

**3.** Framework for the Future will help local and library authorities agree on the modern mission for this vital service with central government and their local communities. It will give the public library service network a shared sense of purpose. It concentrates on libraries' roles in developing reading and learning, digital skills and services, community cohesion and civic values.

**4.** Framework for the Future is the Government's vision for the public library service based on extensive consultation with Resource (The Council for Museums, Archives and Libraries), library authorities, professional and advisory bodies, including the Advisory Council on Libraries (ACL), the Chartered Institute of Library and Information Professionals (CILIP), and the Society of Chief Librarians (SCL) and other key stakeholder organisations, as well as libraries' partners in national and local government.

### The Position of Libraries

**5.** Libraries have four key strengths. They offer neutral welcoming community space and support active citizenship. They hold enormous stocks of material. This ranges beyond books to include DVDs, videos, CDs and computer software. National Lottery investment has equipped all public libraries in the UK with ICT infrastructure offering public internet access. They offer a wide range of services. As well as lending books, they operate as community centres of formal and informal learning. They promote reading across the age range starting with young babies and continuing through adulthood. They provide access to information and advice. And they are run by committed staff.

**6.** Libraries have the potential to do still more. Knowledge, skills and information are becoming more important to our lives economically, socially and as citizens. Libraries have a central role to play in ensuring everyone has access to the resources, information and knowledge they need -- particularly those groups in society who will otherwise be disadvantaged, including people who are less affluent and people with literacy problems.

**7.** The best libraries are showing the way forward. Librarians are developing new skills to help library users access ICT and use the internet. There has been a big expansion in reader development work. Eye-catching new library buildings have opened in a number of cities and other places are seeking radically to re-define the ways in which library services are delivered.

**8.** But the innovation is not evenly spread and is frequently local and fragile. There are 149 library

<!-- PAGE: 7 -->

authorities operating through 3,500 public libraries, including mobile services. It is difficult for national policy makers to communicate with the public library service as a whole and opportunities for local innovation to be translated into national programmes which attract public funding may be lost.

**9.** Fragmentation of this kind impedes the spread of good practice between authorities. Within local authorities, libraries are frequently part of a much larger department. Innovative authorities recognise the role libraries can play in the wider corporate agenda but in other authorities they can be overlooked and undervalued.

**10.** The Audit Commission Report, *Building Better Library Services*, May 2002, points to a decline in library visits and book loans. It notes a tendency amongst libraries to focus on current users rather than non-users, and patterns of opening hours which do not match the needs of would-be users.

**11.** Libraries also face intense competition in recruiting and retaining staff. Graduate librarians are attracted by private sector salaries. There has been little turnover of the workforce at senior level, promotion opportunities are limited and there is an urgent need to develop a new generation of library leaders.

### Libraries' Modern Mission

**12.** Libraries need a modern mission. They need constantly to renew and communicate their purpose to the communities they serve. Their modern mission should be based on:

- Evolution: building on libraries' traditional core skills in promoting reading, informal learning and self-help
- Public value: focusing on areas where public intervention will deliver the largest benefits to society including support for adult literacy and pre-school learning
- Distinctiveness: building on libraries' open, neutral and self-help culture. They should not duplicate the efforts of other public and private sector providers but complement them through partnership working
- Local interpretations of national programmes: developing national programmes which will raise the profile of the public library service as a whole but which are sufficiently flexible to be adapted to local needs.

**13.** The following three areas of activity meet these criteria and should be at the heart of libraries' modern mission:

- The promotion of reading and informal learning
- Access to digital skills and services including e-government
- Measures to tackle social exclusion, build community identity and develop citizenship.

### Books, Learning and Reading

**14.** Some libraries can be proud of the range and comprehensiveness of their book stock. But, the Audit Commission Report noted that only 59% of users find the book they come to borrow or use, an under-supply in some types of book particularly those of appeal to younger readers, and a reduction in book buying. The report also notes that stock could be managed more effectively in one-third of the authorities inspected.

**15.** This matters because reading is ever more critical in a knowledge-driven society. Most

<!-- PAGE: 8 -->

web pages are text based. People cannot be active or informed citizens unless they can read. Reading is a pre-requisite for almost all cultural and social activities.

**16.** Innovative libraries recognise this and are integrating reading and learning strategies. Reader development strategies have become far more widespread and sophisticated. The emergence of organisations such as The Reading Agency is helping libraries create economies of scale through the development of national programmes, such as the Summer Reading Challenge.

**17.** Public libraries provide a learning network that supports formal education but also extends far beyond it. Reading, literacy and learning are inextricably linked. The self-motivated learning which libraries promote is central to the creation of a lifelong learning culture in which people expect and want to learn throughout their lifetime.

**18.** Research has demonstrated the importance of early learning activities in supporting early cognitive development. The Sure Start programme, which provides co-ordinated and integrated support to young families and their children in disadvantaged areas, has set a target for its projects, which aims to 'increase the use of libraries with parents by young children'. The challenge to libraries is to make this early years provision part of a national early years strategy.

**19.** Many library services are developing closer relationships with school age children to support the work of schools. This is providing a vital complementary learning service, which can be developed further by:

- Working with local schools to provide a planned programme of reader development to enrich and enhance the curriculum
- Forging stronger partnerships with schools in the poorest areas
- Creating a national network of homework clubs -- either physical or online
- Using the national Summer Reading Challenge to help children to continue to learn during the summer vacation and so help minimise the 'summer learning dip'
- Developing a national programme for working with children in care and young offenders institutions.

**20.** As participation rates in further and higher education climb so will the demand from students for study space and support materials. Public libraries can play a critical role as study centres for people engaged in distance learning programmes, including those offered by learndirect, where libraries provide both access to equipment and staff trained in learner support, and for students returning home in university vacations.

**21.** Libraries also have a vital role to play in supporting adults with basic literacy problems. Seven million adults in England have levels of attainment in reading and writing lower than that expected for children aged eleven. The Government's Skills for Life strategy aims to improve the literacy, language and numeracy skills of 1.5 million adults by 2007. Libraries are ideally placed to recognise and support people who might benefit from tuition.

**22.** DCMS and DfES, working with Resource, the National Learning and Skills Council and the National Literacy Trust, will continue to explore ways in which libraries can support adult basic skills provision.

<!-- PAGE: 9 -->

### Digital Citizenship

**23.** Lottery funding from the New Opportunities Fund has enabled almost all public libraries in England to establish UK online learning centres by the end of December 2002, as well as providing library staff with computer literacy and learner support skills. A related £50 million programme is creating online content. The People's Network in public libraries has a vital role to play in delivering the Government's commitment to universal access to the internet and the provision of e-government services.

**24.** Resource has hosted wide-ranging discussions with library authorities on how The People's Network should develop. Ideas emerging include:

- Communities online: public libraries could offer to create, host and manage websites for local community groups
- Culture Online: Culture Online will create new online content and interactive services. Libraries have a role in providing access and in generating new content
- National content: Resource could act as a central agent brokering national online content agreements on behalf of the public library service
- Alliances with broadcasters: libraries could be an important physical point of contact for people learning through broadcasters' online services
- Information: Resource will consider the scope for a national service to answer queries online building on similar services already offered by some library authorities.

**25.** Resource is developing plans for the future services to be provided through libraries. These plans will address the need for central development of national services and support for delivery of local services.

### Community and Civic Values

**26.** Libraries are public anchors for neighbourhoods and communities. For the majority of the population, libraries are acknowledged as safe, welcoming, neutral spaces open to all in the community. For libraries to continue to play this role in civic life they have to remain relevant to the needs of the communities they serve.

**27.** Libraries face a number of pressing challenges: renewing the building stock and reaching non-users while continuing to meet the needs of existing users. Well used and attractive library buildings draw people to town centres and so contribute to economic activity while providing people with personal space which is an alternative to shopping and commercial entertainment. Some new library buildings have been a result of successful Private Finance Initiatives. Elsewhere authorities have used imaginative design principles to modernise and improve ease of access to services. There are valuable lessons to be learned from these initiatives, which have unlocked new sources of funding. DCMS and Resource propose to work together to disseminate good practice from these.

**28.** Libraries need to re-double their efforts to reach non-users. One route to non-users is through collaboration with other public services, for example by co-locating public libraries with other services such as education, social services, health or leisure services.

**29.** Library authorities need to survey and review the needs of the communities they serve,

<!-- PAGE: 10 -->

focusing particularly on the needs of the excluded.

### Delivering Change

**30.** Framework for the Future is seeking to develop a new partnership for delivery between central and local government. Local authorities must retain their statutory duty to provide a comprehensive and efficient library service, taking account of local needs and circumstances. The role of central government is to guide, support and set the standard for that service.

**31.** Delivery of this new strategic framework will require:

- Greater recognition by central and local government of the role public libraries can play in the delivery of key public service priorities
- A strong central capacity to speak for the public library service, to champion innovation and to spread good practice. Resource is the strategic body empowered to advise government and the library sector on the long-term development of museums, archives and libraries
- A strengthened regional capacity to support local service development and help libraries to build cross-sectoral partnerships
- Simpler and streamlined arrangements for setting standards, planning and inspecting services in order to drive continuous improvement in public library services
- A new relationship with the business community.

**32.** DCMS will lead action in all these areas with Resource and the library community. Resource will publish an action plan in spring 2003 setting out how it will implement this new strategic framework.

<!-- PAGE: 11 -->

> Imagine a place through which every newborn baby is welcomed into the community with a gift of books to help start a lifelong journey of learning...
>
> Imagine a place you can walk into, without anyone asking who you are or why you're there, that is warm, clean, safe and welcoming...
>
> This is not a shop but it offers people as much choice as a modern bookstore...
>
> Here you can get advice about careers or look for a job, find out about your local council, consult an encyclopaedia, read a national newspaper or borrow a recording of the latest music...
>
> This is not a college but it's a place where you can learn to use a computer, access the internet and discover new worlds of knowledge...
>
> And if you cannot get to these places, because you live in a remote rural area or have difficulty leaving your home, a mobile service will come to you.
>
> And much of this is free at the point of delivery.
>
> There are places like this all over the country: public libraries.
>
> *All of the above are examples drawn from what libraries are doing right now.*"""

def update_exec_summary():
    text = FILE_PATH.read_text(encoding="utf-8")
    pattern = r"<!-- PAGE: 6 -->.*?<!-- PAGE: 12 -->"
    new_text = re.sub(pattern, f"{EXECUTIVE_SUMMARY}\n\n<!-- PAGE: 12 -->", text, flags=re.DOTALL)
    FILE_PATH.write_text(new_text, encoding="utf-8")
    print("Executive summary updated successfully.")

if __name__ == "__main__":
    update_exec_summary()
