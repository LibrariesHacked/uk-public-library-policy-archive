import re
from pathlib import Path

report_path = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")
content = report_path.read_text(encoding="utf-8")

# Normalize CRLF to LF
content = content.replace("\r\n", "\n")

def safe_replace(text, old, new, desc=""):
    assert old in text, f"FAILED TO FIND TARGET for {desc}!\nSnippet:\n{old[:100]}..."
    count = text.count(old)
    assert count == 1, f"TARGET APPEARS {count} TIMES for {desc}!"
    return text.replace(old, new)

# 1. Page breaks at paragraph boundaries
# Page 6 -> 7
old_p6_p7 = """whether for <!-- PAGE: 7 --> pleasure, information or learning."""
new_p6_p7 = """whether for pleasure, information or learning.

<!-- PAGE: 7 -->"""
content = safe_replace(content, old_p6_p7, new_p6_p7, "Page 6->7")

# Page 7 -> 8: Restore full text of 15 and place PAGE: 8 before paragraph 15
old_p7_p8 = """**15.** This matters because reading is ever more critical in a knowledge-driven society. Most <!-- PAGE: 8 --> web pages are text based. People cannot be active or informed citizens unless they can read. Reading is a pre-requisite for almost all cultural and social activities."""
new_p7_p8 = """<!-- PAGE: 8 -->

**15.** This matters because reading is ever more important in modern life. The rise of the internet has not displaced reading since most web pages are text based. People cannot be active or informed citizens unless they can read. Reading is a pre-requisite for almost all cultural and social activities."""
content = safe_replace(content, old_p7_p8, new_p7_p8, "Page 7->8")

# Page 9 -> 10: Place PAGE: 10 between paragraph 29 and Delivering Change
old_p9_p10 = """**29.** Library authorities need to survey and review the needs of the communities they serve, <!-- PAGE: 10 --> focusing particularly on the needs of the excluded."""
new_p9_p10 = """**29.** Library authorities need to survey and review the needs of the communities they serve, focusing particularly on the needs of the excluded.

<!-- PAGE: 10 -->"""
content = safe_replace(content, old_p9_p10, new_p9_p10, "Page 9->10")

# Page 15 -> 16: Place PAGE: 16 between paragraph 2.5 and paragraph 2.6
old_p15_p16 = """run a wide <!-- PAGE: 16 --> range of programmes"""
new_p15_p16 = """run a wide range of programmes"""
content = safe_replace(content, old_p15_p16, new_p15_p16, "Page 15->16 inline")

old_p25_end = """They are increasingly vital service centres for a host of information-related needs.

**2.6** Finally,"""
new_p25_end = """They are increasingly vital service centres for a host of information-related needs.

<!-- PAGE: 16 -->

**2.6** Finally,"""
content = safe_replace(content, old_p25_end, new_p25_end, "Page 15->16 boundary")

# 2. Section 4: Bookstart, heading, paragraph 4.7, images on page 25
old_sec4_p25 = """<!-- PAGE: 25 -->

Bookstart, launched by Booktrust through private sponsorship, was first piloted in Birmingham in 1992 on the principle that it is never too early to introduce children to books. Simple packs were put together to be distributed by health visitors when they make their 7 -- 9 month check on a baby's health. They include a free picture book, a place mat with nursery rhymes, book lists for babies and an invitation to join the local library.

Ten years from its launch, Bookstart has developed into a national programme and academic research shows that Bookstart babies are more confident readers when they start school. Families that had a Bookstart pack are far more likely to take their children to the library, name reading as one of their most enjoyable activities and finish a book once it has been started. At the age of five Bookstart children are far more likely to join in with stories, ask questions about them and relate a story to their own lives.

How libraries are making a unique contribution to the reading nation

**4.7** Libraries do not just provide a store of books: they help people experience and enjoy the pleasure of reading. In recent years there has been an important shift in how libraries view and plan their work with reading. As well as its importance as a tool for learning, they have recognised its creative, imaginative role in people's lives. Reader development strategies have become far more widespread, encouraging people to start reading, whether young or old; helping emerging readers to find more interesting material, whether that be teenagers or adult first time readers; connecting people with similar interests to one another through book groups and Mayor of Royal Borough of Windsor and Maidenhead with parents and babies at Bookstart launch. Courtesy of Royal Borough of Windsor and Maidenhead Library Service.

reading events. Increasingly libraries are developing outreach strategies reaching out to disaffected groups and demonstrating the motivational power of reading.

Promoting reading for pleasure. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.

<!-- PAGE: 26 -->"""

new_sec4_p25 = """<!-- PAGE: 25 -->

> ### Case Study: Bookstart
>
> Bookstart, launched by Booktrust through private sponsorship, was first piloted in Birmingham in 1992 on the principle that it is never too early to introduce children to books. Simple packs were put together to be distributed by health visitors when they make their 7 -- 9 month check on a baby's health. They include a free picture book, a place mat with nursery rhymes, book lists for babies and an invitation to join the local library.
>
> Ten years from its launch, Bookstart has developed into a national programme and academic research shows that Bookstart babies are more confident readers when they start school. Families that had a Bookstart pack are far more likely to take their children to the library, name reading as one of their most enjoyable activities and finish a book once it has been started. At the age of five Bookstart children are far more likely to join in with stories, ask questions about them and relate a story to their own lives.
>
> > ![Mayor of Royal Borough of Windsor and Maidenhead with parents and babies at Bookstart launch](assets/figure-025a.jpg)
>
> *Mayor of Royal Borough of Windsor and Maidenhead with parents and babies at Bookstart launch. Courtesy of Royal Borough of Windsor and Maidenhead Library Service.*

### How libraries are making a unique contribution to the reading nation

**4.7** Libraries do not just provide a store of books: they help people experience and enjoy the pleasure of reading. In recent years there has been an important shift in how libraries view and plan their work with reading. As well as its importance as a tool for learning, they have recognised its creative, imaginative role in people's lives. Reader development strategies have become far more widespread, encouraging people to start reading, whether young or old; helping emerging readers to find more interesting material, whether that be teenagers or adult first time readers; connecting people with similar interests to one another through book groups and reading events. Increasingly libraries are developing outreach strategies reaching out to disaffected groups and demonstrating the motivational power of reading.

![Promoting reading for pleasure](assets/figure-025b.jpg)

*Promoting reading for pleasure. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.*

<!-- PAGE: 26 -->"""
content = safe_replace(content, old_sec4_p25, new_sec4_p25, "Section 4 Page 25")

# 3. Section 4: HM Prison Service, Northamptonshire, Chatterbooks, Liverpool Libraries (p. 26-28)
old_sec4_p26_p28 = """<!-- PAGE: 26 -->

All prisons managed by HM Prison Service offer a library service provided by the public library authority. Even the most progressive regimes leave prisoners with a large amount of unoccupied time. As a consequence, reading can be an important leisure activity in prison, especially so when there is an adequate library service to support that need. The Big Book Share is a partnership between Nottingham City Libraries and Information Service, The Reading Agency, HM Prison Nottingham, Marks & Spencer plc's Community Division, East Midlands Arts and 23 children's publishers. Librarians run fortnightly sessions at the prison to help prisoners choose books and support children reading. Prisoners develop reading skills as they read with their children on visits or record a tape of stories for their children to listen to at home.

**4.8** Libraries' approach to reader development is becoming increasingly sophisticated. Library authorities are working together to create new structures enabling programmes to be delivered both regionally and nationally. The Summer Reading Challenge is one example. Until four years ago each library authority developed its own summer reading programme. This is now a national programme, co-ordinated through The Reading Agency (TRA), creating economies of scale and allowing libraries to market their services far more effectively. Another good example occurred in 2002 when The Reading Agency co-ordinated the library contribution to Splash Extra, a government programme of diversionary summer activities for young people at risk of offending. TRA worked with ten English library authorities to deliver its Splash Extra programme, in partnership with local Youth Offending Teams and youth services, which consisted of a varied and largely successful programme of reading- related multimedia arts activities throughout the summer. These reached 2,500 young people within the designated target groups, the majority of whom have never previously set foot in a library, and for whom the world of words, books and reading was unknown, alien or hostile territory.

In 2001 Northamptonshire Libraries and Information Service ran a Bookstart programme for babies; a summer reading challenge to encourage school age children to read six books over the holidays; a summer bookbus to visit play schemes and literacy schools; a story festival which involved 7,000 children; online workshops for budding writers; new internet based tools people can use to find new books that might interest them and a variety of local reading clubs.

<!-- PAGE: 27 -->

**4.9** Increasingly ICT is being used to support reader development. Whichbook.net, launched by Opening the Book, allows readers to select works of fiction tailored to their particular interests and preferences. New training programmes are developing. Branching Out, a collaboration between library authorities and Regional Arts Boards, provides regional programmes of activity to promote literature development. Their Reading Futures, a pilot programme funded through the DCMS/Wolfson programme has created a quality framework for planning young people's reading services. In addition, libraries are investing in research to understand better the needs of readers and the impact their reading is having on future attainment.

Chatterbooks is a national network of reading groups for 4-12 year olds, sponsored by Orange, in partnership with the public library network and was brokered by independent library development agency Launchpad. Chatterbooks aims to inspire young people to read more adventurously and develop confidence in talking about and choosing books. Orange has funded the work needed to create the network, for staff training, as well as a best practice handbook. Orange also funds the provision of high quality reading materials for all children participating in the scheme. Seventy library authorities now participate in Chatterbooks. Orange's feedback on the scheme is highly favourable. It combines corporate profile at the highest level with grassroots activity in all kinds of communities, including some very deprived ones. It also offers Orange staff the chance to get involved as volunteers.

**4.10** The case studies in this section illustrate just some of the different approaches libraries are taking to promote reading to new audiences. Development agencies -- such as The Reading Agency and Opening the Book -- have already played a critical role in changing the way that libraries think and in promoting reader development. Promoting reading in a society is not the job of libraries alone. Best selling authors including the Children's Laureates have done much to make reading accessible and exciting in the past few years. Literary prizes -- Booker, Whitbread, Orange, Carnegie -- promote reading powerfully.

Liverpool Libraries and Information Services have worked with excluded black youngsters in Edge Hill and housebound readers to provide them with more choice. It is one of thirty-three authorities involved in the Branching Out project that brings together libraries with publishers and booksellers to promote new literature. It is one of the authorities that took part in promotions organised around the Orange prize.

<!-- PAGE: 28 -->

The Novel Route is a scheme involving American Express, West Sussex and Brighton Libraries. Arts & Business South East was a crucial partner in the early stages of this project, brokering the arrangement between American Express and the library services. The project has been developed as part of the rollout of Books & Business into the South East, looking at how library/business partnerships could develop in a regional setting, with a focus on creative reading.

A reader development worker leads the lunchtime reading sessions for staff at AMEX's offices in Burgess Hill and Brighton and the local libraries supply the books. The involvement of a reader development worker has meant that groups at both offices can share experiences and also raise the profile of the library. Library staff are involved and develop new skills needed to work in a non-library environment. American Express has provided support, through office space and allowing staff time to attend. The company also intend to fund an end of project event that will bring together employees, librarians and local teachers to celebrate the project and provide a chance to discuss, in convivial surroundings, potential opportunities for future working.

Public libraries and learning"""

new_sec4_p26_p28 = """<!-- PAGE: 26 -->

> ### Case Study: HM Prison Service and The Big Book Share
>
> All prisons managed by HM Prison Service offer a library service provided by the public library authority. Even the most progressive regimes leave prisoners with a large amount of unoccupied time. As a consequence, reading can be an important leisure activity in prison, especially so when there is an adequate library service to support that need. The Big Book Share is a partnership between Nottingham City Libraries and Information Service, The Reading Agency, HM Prison Nottingham, Marks & Spencer plc's Community Division, East Midlands Arts and 23 children's publishers. Librarians run fortnightly sessions at the prison to help prisoners choose books and support children reading. Prisoners develop reading skills as they read with their children on visits or record a tape of stories for their children to listen to at home.

**4.8** Libraries' approach to reader development is becoming increasingly sophisticated. Library authorities are working together to create new structures enabling programmes to be delivered both regionally and nationally. The Summer Reading Challenge is one example. Until four years ago each library authority developed its own summer reading programme. This is now a national programme, co-ordinated through The Reading Agency (TRA), creating economies of scale and allowing libraries to market their services far more effectively. Another good example occurred in 2002 when The Reading Agency co-ordinated the library contribution to Splash Extra, a government programme of diversionary summer activities for young people at risk of offending. TRA worked with ten English library authorities to deliver its Splash Extra programme, in partnership with local Youth Offending Teams and youth services, which consisted of a varied and largely successful programme of reading- related multimedia arts activities throughout the summer. These reached 2,500 young people within the designated target groups, the majority of whom have never previously set foot in a library, and for whom the world of words, books and reading was unknown, alien or hostile territory.

> ### Case Study: Northamptonshire Libraries
>
> In 2001 Northamptonshire Libraries and Information Service ran a Bookstart programme for babies; a summer reading challenge to encourage school age children to read six books over the holidays; a summer bookbus to visit play schemes and literacy schools; a story festival which involved 7,000 children; online workshops for budding writers; new internet based tools people can use to find new books that might interest them and a variety of local reading clubs.

<!-- PAGE: 27 -->

**4.9** Increasingly ICT is being used to support reader development. Whichbook.net, launched by Opening the Book, allows readers to select works of fiction tailored to their particular interests and preferences. New training programmes are developing. Branching Out, a collaboration between library authorities and Regional Arts Boards, provides regional programmes of activity to promote literature development. Their Reading Futures, a pilot programme funded through the DCMS/Wolfson programme has created a quality framework for planning young people's reading services. In addition, libraries are investing in research to understand better the needs of readers and the impact their reading is having on future attainment.

> ### Case Study: Chatterbooks
>
> Chatterbooks is a national network of reading groups for 4-12 year olds, sponsored by Orange, in partnership with the public library network and was brokered by independent library development agency Launchpad. Chatterbooks aims to inspire young people to read more adventurously and develop confidence in talking about and choosing books. Orange has funded the work needed to create the network, for staff training, as well as a best practice handbook. Orange also funds the provision of high quality reading materials for all children participating in the scheme. Seventy library authorities now participate in Chatterbooks. Orange's feedback on the scheme is highly favourable. It combines corporate profile at the highest level with grassroots activity in all kinds of communities, including some very deprived ones. It also offers Orange staff the chance to get involved as volunteers.

**4.10** The case studies in this section illustrate just some of the different approaches libraries are taking to promote reading to new audiences. Development agencies -- such as The Reading Agency and Opening the Book -- have already played a critical role in changing the way that libraries think and in promoting reader development. Promoting reading in a society is not the job of libraries alone. Best selling authors including the Children's Laureates have done much to make reading accessible and exciting in the past few years. Literary prizes -- Booker, Whitbread, Orange, Carnegie -- promote reading powerfully.

> ### Case Study: Liverpool Libraries and Information Services
>
> Liverpool Libraries and Information Services have worked with excluded black youngsters in Edge Hill and housebound readers to provide them with more choice. It is one of thirty-three authorities involved in the Branching Out project that brings together libraries with publishers and booksellers to promote new literature. It is one of the authorities that took part in promotions organised around the Orange prize.

<!-- PAGE: 28 -->

> ### Case Study: The Novel Route (American Express, West Sussex & Brighton)
>
> The Novel Route is a scheme involving American Express, West Sussex and Brighton Libraries. Arts & Business South East was a crucial partner in the early stages of this project, brokering the arrangement between American Express and the library services. The project has been developed as part of the rollout of Books & Business into the South East, looking at how library/business partnerships could develop in a regional setting, with a focus on creative reading.
>
> A reader development worker leads the lunchtime reading sessions for staff at AMEX's offices in Burgess Hill and Brighton and the local libraries supply the books. The involvement of a reader development worker has meant that groups at both offices can share experiences and also raise the profile of the library. Library staff are involved and develop new skills needed to work in a non-library environment. American Express has provided support, through office space and allowing staff time to attend. The company also intend to fund an end of project event that will bring together employees, librarians and local teachers to celebrate the project and provide a chance to discuss, in convivial surroundings, potential opportunities for future working.

### Public libraries and learning"""
content = safe_replace(content, old_sec4_p26_p28, new_sec4_p26_p28, "Section 4 Page 26-28")

# 4. Section 4: Learning culture, Libraries' role, March Library (p. 29)
old_sec4_p29 = """<!-- PAGE: 29 -->

Learning culture Learning has to become a habit and a culture, rather than an obligation and imposition.

Learning has to start before and extend well beyond school and college.

Learners have to be able to access learning in manageable, flexible packages, suited to their needs as well as being able to enrol on terms and courses.

People with poor experience of formal education need extra encouragement and small steps to get back on the ladder of learning.

Cambridgeshire, March library is not a college of further education: but it offers a wide range of In courses, the local college has integrated its learning opportunities in March with the learndirect centre of the library. Nor is it a school: but children use it for out of hours study. March library also works closely with tutors working with children excluded from school to provide them with a place to work. The redesigned library is an example of how learning can be made an integral yet informal part of a library service. The new library, opened two years ago, makes this offer to local people: \"whatever you want to learn and however you want to learn, whether at home or in a group, we can make it happen for you\".

Anyone who wants to learn, no matter what the subject, can talk to a personal learning adviser who will recommend the best approach. Learners can study on their own at a bank of computers, go on a course, sign up for distance learning or simply take away a book. The library runs accredited courses from British Computer Society (ECDL) and OCR (New CLAIT) in addition to learndirect .

Libraries' role Libraries provide an unthreatening environment for self-motivated learning, in which people can pursue their hobbies and interests without necessarily engaging in formal courses. Libraries promote learning as exploration and self-development.

Libraries are one of the few places where young and old, school children, college students and adult learners can all participate in learning.

Libraries allow informal, individual learning, clubs and communities for learning (such as local history) as well as providing a range of short evening and daytime courses.

Libraries are \"learning start up\" organisations, they should excel at helping people get started with learning, whether those are children or adults returning to learn. Libraries should provide the foundations for a learning culture.

Learners at March Library. Courtesy of Cambridgeshire County Council Libraries and Information Service."""

new_sec4_p29 = """<!-- PAGE: 29 -->

### Learning culture

- Learning has to become a habit and a culture, rather than an obligation and imposition.
- Learning has to start before and extend well beyond school and college.
- Learners have to be able to access learning in manageable, flexible packages, suited to their needs as well as being able to enrol on terms and courses.
- People with poor experience of formal education need extra encouragement and small steps to get back on the ladder of learning.

### Libraries' role

Libraries provide an unthreatening environment for self-motivated learning, in which people can pursue their hobbies and interests without necessarily engaging in formal courses. Libraries promote learning as exploration and self-development.

Libraries are one of the few places where young and old, school children, college students and adult learners can all participate in learning.

Libraries allow informal, individual learning, clubs and communities for learning (such as local history) as well as providing a range of short evening and daytime courses.

Libraries are \"learning start up\" organisations, they should excel at helping people get started with learning, whether those are children or adults returning to learn. Libraries should provide the foundations for a learning culture.

> ### Case Study: March Library, Cambridgeshire
>
> In Cambridgeshire, March library is not a college of further education: but it offers a wide range of courses, the local college has integrated its learning opportunities in March with the learndirect centre of the library. Nor is it a school: but children use it for out of hours study. March library also works closely with tutors working with children excluded from school to provide them with a place to work. The redesigned library is an example of how learning can be made an integral yet informal part of a library service. The new library, opened two years ago, makes this offer to local people: \"whatever you want to learn and however you want to learn, whether at home or in a group, we can make it happen for you\".
>
> Anyone who wants to learn, no matter what the subject, can talk to a personal learning adviser who will recommend the best approach. Learners can study on their own at a bank of computers, go on a course, sign up for distance learning or simply take away a book. The library runs accredited courses from British Computer Society (ECDL) and OCR (New CLAIT) in addition to learndirect.
>
> > ![Learners at March Library](assets/figure-029.jpg)
>
> *Learners at March Library. Courtesy of Cambridgeshire County Council Libraries and Information Service.*"""
content = safe_replace(content, old_sec4_p29, new_sec4_p29, "Section 4 Page 29")

# 5. Section 4: Peterlee, Stockton, Birmingham, Bedfordshire, Boox on the Move, Supporting older students, Adult Basic Skills Sunderland, Conclusions, Barnet (p. 30-33)
old_sec4_p30_p33 = """### Supporting early learning

**4.15** Research has demonstrated the importance of early learning activities in supporting early cognitive development. Increasingly the role of libraries is being acknowledged and addressed in early years service provision. The Sure Start programme which provides co-ordinated and integrated support to young children and their families in disadvantaged areas is encouraging closer links with public libraries. Sure Start has included a target for each project, which aims to 'increase the use of libraries with parents by young children in Sure Start areas'. Involvement in Sure Start has enabled libraries to increase their early years provision -- in the past two years over one hundred and thirty early years library posts have been created.

Peterlee Sure Start is working with libraries to improve educational attainments with its 'Read and Play Club'. Peterlee Sure Start's research found that only 6.9% of the pre-school children in the district were gaining access to library services (i.e. having borrowed in the last twelve months). 'Fun' learning materials such as books, videos and toys are provided in the Sure Start Read and Play Clubs. Each child in a Sure Start area has a personalised 'Book Worm' library card. The Sure Start Programme works in tandem with the County Library Service. In six weeks they increased active library membership in children of 0-4 by 100%.

**4.16** The challenge to libraries is to make this a core activity clearly identifying it as an element of the national early years strategy.

Supporting pupils and students Stockton on Tees' community libraries all house a dedicated homework resource collection, including PCs offering access to the internet and CDs. Homework help sessions are run by trained staff.

**4.17** Many library services are developing closer relationships with school age children to support and complement the work of schools. Hertfordshire library service was one of the first in the country to create homework clubs, which have been running for five years. Page Moss Library in Huyton works with social services to create services for children excluded from school to encourage them to learn in informal ways.

**4.18** Libraries are currently discovering the key role they have to play in delivering Connexions, the Government's new support service for all young people aged 13-19 in England. The programme offers support to young people delivered through access to information and through the personal support offered by a trained personal adviser. Libraries are recognising their role in both of these functions.

Birmingham Central Library now hosts a Connexions information point. This is the centre of a strong local library strategy for supporting Connexions, which will establish a Connexions team within the library and work closely with Behavioural Support Services who will use referral to the library as an educational extension of their service provision.

<!-- PAGE: 31 -->

Bedfordshire Libraries' Homework Centres are open two evenings a week and are staffed by a Homework Centre Organiser, supported by library staff. The target age group for the Centres' users is 8 -- 13 year olds, although any child needing help with homework is welcome. Each centre is in a library and has a dedicated study area, offers access to stock and a bank of PCs linked to the internet, CDs, word processing and other packages. The Homework Centre staff encourage children to use the most effective resources -- whether books or ICT or helping each other. The first two Homework Centres, launched in 2001, have proved so successful that they are now funded permanently. Two more Homework Centres have opened recently.

**4.19** School Library Services support learning for around three-quarters of school children in England. These services are frequently managed by the public library service and act as a crucial bridging agent between schools and public libraries. Their knowledge of the curriculum can enrich libraries' homework support provision. Frequently they forge partnerships to enable public libraries to work more effectively in supporting literacy and developing reading and increasingly they are providing links at local level between public library ICT learning networks and school ICT provision.

**4.20** Libraries can provide a vital alternative but complementary learning service to support school age children. In the next decade this should involve the library service in:

- Working with local schools in conjunction with Schools Library Services and the School Library Association to provide a planned programme of reader development to enrich and enhance the curriculum
- Forging stronger partnerships with schools in the poorest areas to encourage children from these schools to use libraries
- Creating a national network of homework clubs with every library authority offering a service of some kind to every secondary school in their area. This could take the form of a physical club or access through the library to online resources such as Channel 4's Homework High service
- Using the national Summer Reading Challenge to help children to continue to learn in the long school holidays and so help minimise the 'summer learning dip' which means that the first weeks of autumn term are often taken up with remedial work. This might initially focus on the transition from primary to secondary school. Every child leaving primary school could be invited to the library Summer Reading Challenge
- Developing a national programme for working with children in care and young offenders institutions.

**4.21** Taken together these initiatives could provide a powerful entitlement for school children, which will serve to enhance and support formal educational provision.

<!-- PAGE: 32 -->

Boox on the Move, a partnership between Leeds Library and Information Services and Barnardo's, supports the information needs of young people in care. Aimed at 13-16 year olds the scheme is about creating a positive reading culture. Originally aimed at meeting sexual health information needs the project has been broadened to cover all aspects of a young person's life.

Supporting older students

**4.22** One of the most far-reaching strategies to put libraries at the heart of learning has been pursued by a partnership between the public, college and university library services of Sunderland. These libraries have joined forces to create The Libraries Access Sunderland Scheme (LASH). LASH links public, college and university libraries, which gives users access to all facilities. The public libraries now offer one hundred and thirty drop in courses run in conjunction with the City of Sunderland College. Libraries across the city play an important role in delivering outreach work and promoting learning.

**4.23** As participation rates in further and higher education climb so will the demand from students for study space and support materials. Public libraries could play a critical role as study centres for people engaged in distance learning programmes, for example those run by learndirect. The success of the LASH initiative suggests it should be learned from and adapted to other cities developing learning strategies.

Adult basic skills Sunderland's library service plays a critical role in the city's strategy for developing adult basic learning. About 43,000 of Sunderland's population of 289,500 are estimated to have literacy levels below the national average. Hendon library was one of the first in the country to create a short intensive basic skills course for adults, ran in partnership with the City of Sunderland College. In Hetton, an area hit by mining closures, a multi-purpose centre will open in 2003: it will comprise a library, Electronic Village Hall, Learning Centre, GP surgeries, housing offices, home care services, sports facilities, Job Linkage, community rooms and café, multi-purpose rooms for social and training opportunities and an Information service.

**4.24** The Government's Skills for Life strategy aims to improve the literacy, language and numeracy skills of 1.5 million adults by 2007. Libraries have demonstrated that they can play a vital role in this programme of adult literacy in a range of ways. They are ideally placed to recognise people who might benefit from tuition and encourage them to find out more, they can incorporate tuition into other services, and the library provides an informal environment for courses.

**4.25** DCMS and DfES working with Resource and the National Learning and Skills Council and the National Literacy Trust, will continue to explore ways in which libraries can support adult basic skills provision.

<!-- PAGE: 33 -->

### Conclusions

**4.26** Promoting reading and informal learning are core library activities. Libraries need to build on these successes to help create a culture of lifelong learning for all. To do that the library service needs to:"""

new_sec4_p30_p33 = """### Supporting early learning

**4.15** Research has demonstrated the importance of early learning activities in supporting early cognitive development. Increasingly the role of libraries is being acknowledged and addressed in early years service provision. The Sure Start programme which provides co-ordinated and integrated support to young children and their families in disadvantaged areas is encouraging closer links with public libraries. Sure Start has included a target for each project, which aims to 'increase the use of libraries with parents by young children in Sure Start areas'. Involvement in Sure Start has enabled libraries to increase their early years provision -- in the past two years over one hundred and thirty early years library posts have been created.

> ### Case Study: Peterlee Sure Start
>
> Peterlee Sure Start is working with libraries to improve educational attainments with its 'Read and Play Club'. Peterlee Sure Start's research found that only 6.9% of the pre-school children in the district were gaining access to library services (i.e. having borrowed in the last twelve months). 'Fun' learning materials such as books, videos and toys are provided in the Sure Start Read and Play Clubs. Each child in a Sure Start area has a personalised 'Book Worm' library card. The Sure Start Programme works in tandem with the County Library Service. In six weeks they increased active library membership in children of 0-4 by 100%.

**4.16** The challenge to libraries is to make this a core activity clearly identifying it as an element of the national early years strategy.

### Supporting pupils and students

> ### Case Study: Stockton on Tees Community Libraries
>
> Stockton on Tees' community libraries all house a dedicated homework resource collection, including PCs offering access to the internet and CDs. Homework help sessions are run by trained staff.

**4.17** Many library services are developing closer relationships with school age children to support and complement the work of schools. Hertfordshire library service was one of the first in the country to create homework clubs, which have been running for five years. Page Moss Library in Huyton works with social services to create services for children excluded from school to encourage them to learn in informal ways.

**4.18** Libraries are currently discovering the key role they have to play in delivering Connexions, the Government's new support service for all young people aged 13-19 in England. The programme offers support to young people delivered through access to information and through the personal support offered by a trained personal adviser. Libraries are recognising their role in both of these functions.

> ### Case Study: Birmingham Central Library Connexions
>
> Birmingham Central Library now hosts a Connexions information point. This is the centre of a strong local library strategy for supporting Connexions, which will establish a Connexions team within the library and work closely with Behavioural Support Services who will use referral to the library as an educational extension of their service provision.

<!-- PAGE: 31 -->

> ### Case Study: Bedfordshire Libraries' Homework Centres
>
> Bedfordshire Libraries' Homework Centres are open two evenings a week and are staffed by a Homework Centre Organiser, supported by library staff. The target age group for the Centres' users is 8 -- 13 year olds, although any child needing help with homework is welcome. Each centre is in a library and has a dedicated study area, offers access to stock and a bank of PCs linked to the internet, CDs, word processing and other packages. The Homework Centre staff encourage children to use the most effective resources -- whether books or ICT or helping each other. The first two Homework Centres, launched in 2001, have proved so successful that they are now funded permanently. Two more Homework Centres have opened recently.

**4.19** School Library Services support learning for around three-quarters of school children in England. These services are frequently managed by the public library service and act as a crucial bridging agent between schools and public libraries. Their knowledge of the curriculum can enrich libraries' homework support provision. Frequently they forge partnerships to enable public libraries to work more effectively in supporting literacy and developing reading and increasingly they are providing links at local level between public library ICT learning networks and school ICT provision.

**4.20** Libraries can provide a vital alternative but complementary learning service to support school age children. In the next decade this should involve the library service in:

- Working with local schools in conjunction with Schools Library Services and the School Library Association to provide a planned programme of reader development to enrich and enhance the curriculum
- Forging stronger partnerships with schools in the poorest areas to encourage children from these schools to use libraries
- Creating a national network of homework clubs with every library authority offering a service of some kind to every secondary school in their area. This could take the form of a physical club or access through the library to online resources such as Channel 4's Homework High service
- Using the national Summer Reading Challenge to help children to continue to learn in the long school holidays and so help minimise the 'summer learning dip' which means that the first weeks of autumn term are often taken up with remedial work. This might initially focus on the transition from primary to secondary school. Every child leaving primary school could be invited to the library Summer Reading Challenge
- Developing a national programme for working with children in care and young offenders institutions.

**4.21** Taken together these initiatives could provide a powerful entitlement for school children, which will serve to enhance and support formal educational provision.

<!-- PAGE: 32 -->

> ### Case Study: Boox on the Move
>
> Boox on the Move, a partnership between Leeds Library and Information Services and Barnardo's, supports the information needs of young people in care. Aimed at 13-16 year olds the scheme is about creating a positive reading culture. Originally aimed at meeting sexual health information needs the project has been broadened to cover all aspects of a young person's life.

### Supporting older students

**4.22** One of the most far-reaching strategies to put libraries at the heart of learning has been pursued by a partnership between the public, college and university library services of Sunderland. These libraries have joined forces to create The Libraries Access Sunderland Scheme (LASH). LASH links public, college and university libraries, which gives users access to all facilities. The public libraries now offer one hundred and thirty drop in courses run in conjunction with the City of Sunderland College. Libraries across the city play an important role in delivering outreach work and promoting learning.

**4.23** As participation rates in further and higher education climb so will the demand from students for study space and support materials. Public libraries could play a critical role as study centres for people engaged in distance learning programmes, for example those run by learndirect. The success of the LASH initiative suggests it should be learned from and adapted to other cities developing learning strategies.

> ### Case Study: Adult Basic Skills in Sunderland
>
> Sunderland's library service plays a critical role in the city's strategy for developing adult basic learning. About 43,000 of Sunderland's population of 289,500 are estimated to have literacy levels below the national average. Hendon library was one of the first in the country to create a short intensive basic skills course for adults, ran in partnership with the City of Sunderland College. In Hetton, an area hit by mining closures, a multi-purpose centre will open in 2003: it will comprise a library, Electronic Village Hall, Learning Centre, GP surgeries, housing offices, home care services, sports facilities, Job Linkage, community rooms and café, multi-purpose rooms for social and training opportunities and an Information service.

**4.24** The Government's Skills for Life strategy aims to improve the literacy, language and numeracy skills of 1.5 million adults by 2007. Libraries have demonstrated that they can play a vital role in this programme of adult literacy in a range of ways. They are ideally placed to recognise people who might benefit from tuition and encourage them to find out more, they can incorporate tuition into other services, and the library provides an informal environment for courses.

**4.25** DCMS and DfES working with Resource and the National Learning and Skills Council and the National Literacy Trust, will continue to explore ways in which libraries can support adult basic skills provision.

<!-- PAGE: 33 -->

### Conclusions

**4.26** Promoting reading and informal learning are core library activities. Libraries need to build on these successes to help create a culture of lifelong learning for all. To do that the library service needs to:"""
content = safe_replace(content, old_sec4_p30_p33, new_sec4_p30_p33, "Section 4 Page 30-33")

report_path.write_text(content, encoding="utf-8")
print("SUCCESSFULLY APPLIED ALL FIXES WITH ASSERTION VERIFICATION!")
