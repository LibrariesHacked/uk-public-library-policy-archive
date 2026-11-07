import re
from pathlib import Path

report_path = Path("archive/reports/dcms-framework-for-the-future-2003/report.md")
content = report_path.read_text(encoding="utf-8")

# 1. Fix split sentences across page boundaries by making the page marker inline
# Page 6 -> 7
content = content.replace(
    "whether for\n<!-- PAGE: 7 -->\npleasure, information or learning.",
    "whether for <!-- PAGE: 7 --> pleasure, information or learning."
)
# Page 7 -> 8
content = content.replace(
    "Most\n<!-- PAGE: 8 -->\nweb pages are text based.",
    "Most <!-- PAGE: 8 --> web pages are text based."
)
# Page 9 -> 10
content = content.replace(
    "the communities they serve,\n<!-- PAGE: 10 -->\nfocusing particularly on the needs of the excluded.",
    "the communities they serve, <!-- PAGE: 10 --> focusing particularly on the needs of the excluded."
)
# Page 15 -> 16
content = content.replace(
    "run a wide\n<!-- PAGE: 16 -->\nrange of programmes",
    "run a wide <!-- PAGE: 16 --> range of programmes"
)

# 2. Fix Section 2: Norfolk & Norwich case study (p. 18) and Building Better Library Services (p. 20)
# Norfolk & Norwich
old_norfolk = """The Norfolk & Norwich Millennium Library is largely open plan with books for loan and for reference stored together for ease of access. Study spaces and computers are spread throughout the building. There are dedicated areas for children, local history and business information, as well as a special express service in the lobby to allow people to browse and borrow popular items through a self-service check out. This area, which is open until 10.30pm each night, allows people to choose from an array of classic and best-selling paperbacks, arranged in bookshop style displays as well as use computers for e-mail and short enquiries. Staff were encouraged to play a role in redesigning the library and new training programmes for customer care and information technology were introduced. Staff now work in largely self-directed and self-managing teams taking responsibility for different aspects of the service.

Library users at the Norfolk & Norwich Millennium Library. Courtesy of Norfolk Library and Information Service. Photographer: Jacqueline Wyatt Photography."""

new_norfolk = """> ### Case Study: Norfolk & Norwich Millennium Library
>
> The Norfolk & Norwich Millennium Library is largely open plan with books for loan and for reference stored together for ease of access. Study spaces and computers are spread throughout the building. There are dedicated areas for children, local history and business information, as well as a special express service in the lobby to allow people to browse and borrow popular items through a self-service check out. This area, which is open until 10.30pm each night, allows people to choose from an array of classic and best-selling paperbacks, arranged in bookshop style displays as well as use computers for e-mail and short enquiries. Staff were encouraged to play a role in redesigning the library and new training programmes for customer care and information technology were introduced. Staff now work in largely self-directed and self-managing teams taking responsibility for different aspects of the service.
>
> > ![Library users at the Norfolk & Norwich Millennium Library](assets/figure-018.jpg)
>
> *Library users at the Norfolk & Norwich Millennium Library. Courtesy of Norfolk Library and Information Service. Photographer: Jacqueline Wyatt Photography.*"""

content = content.replace(old_norfolk, new_norfolk)

# Building Better Library Services (p. 20)
old_bbls = """Building Better Library Services -- Audit Commission, May 2002 Library services need to direct their resources at delivering the services that local people want, in particular:

- Providing the books and information services that people want and need
- Maximising accessibility by opening at times that suit local people, making better use of joint-use facilities, and using the internet to provide access to their services to people at home
- Making services easy and pleasant to use -- in particular looking at what attracts people to bookshops
- Building awareness among non-users of the services they have on offer."""

new_bbls = """> ### Building Better Library Services -- Audit Commission, May 2002
>
> Library services need to direct their resources at delivering the services that local people want, in particular:
>
> - Providing the books and information services that people want and need
> - Maximising accessibility by opening at times that suit local people, making better use of joint-use facilities, and using the internet to provide access to their services to people at home
> - Making services easy and pleasant to use -- in particular looking at what attracts people to bookshops
> - Building awareness among non-users of the services they have on offer."""

content = content.replace(old_bbls, new_bbls)

# 3. Fix Section 3 heading and Idea Store case study (p. 21)
old_sec3 = """## Libraries' Modern Mission

3 > ### Case Study: Idea Stores in Tower Hamlets
>
> The London Borough of Tower Hamlets council wants to create a network of Idea Stores to replace traditional library buildings. The aim is to create an innovative and welcoming environment in which people can learn, browse and relax. Idea Stores combine public library services with adult education courses, community information, cafes and meeting spaces in accessible, high-footfall retail locations.
>
> The first Idea Store opened at Bow in 2002. It is open 7 days a week, including evenings. Visitor numbers and book loans have increased substantially compared with the libraries it replaced, with strong uptake among young people and local ethnic minority communities.
>
> > ![Prototype Idea Store at Bow](assets/figure-021.jpg)
>
> *Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*"""

new_sec3 = """## 3 Libraries' Modern Mission

> ### Case Study: Idea Stores in Tower Hamlets
>
> The London Borough of Tower Hamlets council wants to create a new kind of library: the Idea Store. The authority embarked on the radical overhaul after it found only 15% of Tower Hamlets residents were regular users of its libraries. Yet the unmet need for lifelong learning was huge: 24% of residents needed help with basic skills.
>
> The first Idea Store opened in 2002. It is open 7 days a week for 71 hours. In the foyer people can study, read or have lunch in a large café. Across the hall a bank of internet computers is in constant use. Staff at the library are drawn from adult education and libraries: they form a single, integrated team and wear the same T-shirts. The first, prototype Idea Store is partly a refurbished library, which is a century old. But the bright colours and modern furniture give the place the feel of a record shop or internet café. Visitor figures have trebled, and issues are up by 65% and rising.
>
> Idea Stores are a modern reinterpretation of what a library can be. Around the core stock of books and information, the staff are helping people to learn, search for jobs, access public services or simply to enjoy themselves. In the course of the next few years the Idea Stores brand will be rolled out across the whole authority in a network of purpose-built buildings, in time replacing all the current library building stock.
>
> > ![Prototype Idea Store at Bow](assets/figure-021.jpg)
>
> *Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*"""

content = content.replace(old_sec3, new_sec3)

# Fix Page 23 image embed (interior photo of Idea Store)
old_p23_img = "Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.\n\n<!-- PAGE: 24 -->"
new_p23_img = """![Prototype Idea Store at Bow interior](assets/figure-023.jpg)

*Prototype Idea Store at Bow. Courtesy of London Borough of Tower Hamlets.*

<!-- PAGE: 24 -->"""
content = content.replace(old_p23_img, new_p23_img)

# 4. Fix Section 4: Missing subheadings, case studies, paragraph 4.7 merged caption, March Library, etc.
# Check Doc page 25: Bookstart, heading, paragraph 4.7
old_p25_area = """### The importance of reading

**4.2** In modern life reading is becoming more important than ever. Reading stimulates the imagination and develops creativity. It helps develop independence in learning. Reading draws the reader into a continual journey linking related interests.

**4.3** The rise of the internet has not displaced reading. Most web pages are text based. It has encouraged more people to read.

According to consumer surveys the amount of time spent reading has risen. Fifty-two per cent of adults read books to relax or relieve stress, 27% as a form of escapism and 24% as a chance to use the imagination. Two-thirds of adults and over a half of children read books to find things out.

**4.4** The value of reading, however, stretches far beyond the benefits to the individual. It brings social benefits. It is hard for people to be active citizens unless they can read newspapers and government publications. It is hard for people to be informed consumers, unless they can read guarantees, warranties and small print. It is hard for people to enter into contracts and trade unless they can read legal documents. Most cultural activities are enhanced by reading, from visiting the theatre to reading a CD sleeve or a football programme. Reading gives people access to shared conversations and communities and it promotes family bonding. The phrase \"Did you read…?\" is one of our most commonplace conversational openings.

**4.5** Being unable to read cuts people off: from their own potential and the society around them. Being unable to read in an increasingly text rich culture can lead to social exclusion, with profound consequences socially and economically. More than seven million adults in England are estimated to have literacy problems. Innovative library authorities are integrating reading and learning strategies recognising that the informal self-motivated learning they promote is central to creating the learning habit in society.

**4.6** Thus public libraries' mission to promote the skills, and even more importantly, the appetite, for reading is vital.

<!-- PAGE: 25 -->

Bookstart, launched by Booktrust through private sponsorship, was first piloted in Birmingham in 1992 on the principle that it is never too early to introduce children to books. Simple packs were put together to be distributed by health visitors when they make their 7 -- 9 month check on a baby's health. They include a free picture book, a place mat with nursery rhymes, book lists for babies and an invitation to join the local library.

Ten years from its launch, Bookstart has developed into a national programme and academic research shows that Bookstart babies are more confident readers when they start school. Families that had a Bookstart pack are far more likely to take their children to the library, name reading as one of their most enjoyable activities and finish a book once it has been started. At the age of five Bookstart children are far more likely to join in with stories, ask questions about them and relate a story to their own lives.

**4.7** Libraries do not just provide a store of books: they help people experience and enjoy the pleasure of reading. In recent years there has been an important shift in how libraries view and plan their work with reading. As well as its importance as a tool for learning, they have recognised its creative, imaginative role in people's lives. Reader development strategies have become far more widespread, encouraging people to start reading, whether young or old; helping emerging readers to find more interesting material, whether that be teenagers or adult first time readers; connecting people with similar interests to one another through book groups and Mayor of Royal Borough of Windsor and Maidenhead with parents and babies at Bookstart launch. Courtesy of Royal Borough of Windsor and Maidenhead Library Service.

reading events. Increasingly libraries are developing outreach strategies reaching out to disaffected groups and demonstrating the motivational power of reading.

Promoting reading for pleasure. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.

<!-- PAGE: 26 -->"""

new_p25_area = """### The importance of reading

**4.2** In modern life reading is becoming more important than ever. Reading stimulates the imagination and develops creativity. It helps develop independence in learning. Reading draws the reader into a continual journey linking related interests.

**4.3** The rise of the internet has not displaced reading. Most web pages are text based. It has encouraged more people to read.

According to consumer surveys the amount of time spent reading has risen. Fifty-two per cent of adults read books to relax or relieve stress, 27% as a form of escapism and 24% as a chance to use the imagination. Two-thirds of adults and over a half of children read books to find things out.

**4.4** The value of reading, however, stretches far beyond the benefits to the individual. It brings social benefits. It is hard for people to be active citizens unless they can read newspapers and government publications. It is hard for people to be informed consumers, unless they can read guarantees, warranties and small print. It is hard for people to enter into contracts and trade unless they can read legal documents. Most cultural activities are enhanced by reading, from visiting the theatre to reading a CD sleeve or a football programme. Reading gives people access to shared conversations and communities and it promotes family bonding. The phrase \"Did you read…?\" is one of our most commonplace conversational openings.

**4.5** Being unable to read cuts people off: from their own potential and the society around them. Being unable to read in an increasingly text rich culture can lead to social exclusion, with profound consequences socially and economically. More than seven million adults in England are estimated to have literacy problems. Innovative library authorities are integrating reading and learning strategies recognising that the informal self-motivated learning they promote is central to creating the learning habit in society.

**4.6** Thus public libraries' mission to promote the skills, and even more importantly, the appetite, for reading is vital.

<!-- PAGE: 25 -->

> ### Case Study: Bookstart
>
> Bookstart, launched by Booktrust through private sponsorship, was first piloted in Birmingham in 1992 on the principle that it is never too early to introduce children to books. Simple packs were put together to be distributed by health visitors when they make their 7 -- 9 month check on a baby's health. They include a free picture book, a place mat with nursery rhymes, book lists for babies and an invitation to join the local library.
>
> Ten years from its launch, Bookstart has developed into a national programme and academic research shows that Bookstart babies are more confident readers when they start school. Families that had a Bookstart pack are far more likely to take their children to the library, name reading as one of their most enjoyable activities and finish a book once it has been started. At the age of five Bookstart children are far more likely to join in with stories, ask questions about them and relate a story to their own lives.
>
> > ![Bookstart Launch](assets/figure-025a.jpg)
>
> *Mayor of Royal Borough of Windsor and Maidenhead with parents and babies at Bookstart launch. Courtesy of Royal Borough of Windsor and Maidenhead Library Service.*

### How libraries are making a unique contribution to the reading nation

**4.7** Libraries do not just provide a store of books: they help people experience and enjoy the pleasure of reading. In recent years there has been an important shift in how libraries view and plan their work with reading. As well as its importance as a tool for learning, they have recognised its creative, imaginative role in people's lives. Reader development strategies have become far more widespread, encouraging people to start reading, whether young or old; helping emerging readers to find more interesting material, whether that be teenagers or adult first time readers; connecting people with similar interests to one another through book groups and reading events. Increasingly libraries are developing outreach strategies reaching out to disaffected groups and demonstrating the motivational power of reading.

![Promoting reading for pleasure](assets/figure-025b.jpg)

*Promoting reading for pleasure. Courtesy of London Borough of Sutton Library, Heritage and Registration Services.*

<!-- PAGE: 26 -->"""

content = content.replace(old_p25_area, new_p25_area)

# Doc page 26 & 27: Case studies for HM Prison Service, Northamptonshire, Chatterbooks, Liverpool Libraries
old_p26_p27 = """<!-- PAGE: 26 -->

All prisons managed by HM Prison Service offer a library service provided by the public library authority. Even the most progressive regimes leave prisoners with a large amount of unoccupied time. As a consequence, reading can be an important leisure activity in prison, especially so when there is an adequate library service to support that need. The Big Book Share is a partnership between Nottingham City Libraries and Information Service, The Reading Agency, HM Prison Nottingham, Marks & Spencer plc's Community Division, East Midlands Arts and 23 children's publishers. Librarians run fortnightly sessions at the prison to help prisoners choose books and support children reading. Prisoners develop reading skills as they read with their children on visits or record a tape of stories for their children to listen to at home.

**4.8** Libraries' approach to reader development is becoming increasingly sophisticated. Library authorities are working together to create new structures enabling programmes to be delivered both regionally and nationally. The Summer Reading Challenge is one example. Until four years ago each library authority developed its own summer reading programme. This is now a national programme, co-ordinated through The Reading Agency (TRA), creating economies of scale and allowing libraries to market their services far more effectively. Another good example occurred in 2002 when The Reading Agency co-ordinated the library contribution to Splash Extra, a government programme of diversionary summer activities for young people at risk of offending. TRA worked with ten English library authorities to deliver its Splash Extra programme, in partnership with local Youth Offending Teams and youth services, which consisted of a varied and largely successful programme of reading-related multimedia arts activities throughout the summer. These reached 2,500 young people within the designated target groups, the majority of whom have never previously set foot in a library, and for whom the world of words, books and reading was unknown, alien or hostile territory.

In 2001 Northamptonshire Libraries and Information Service ran a Bookstart programme for babies; a summer reading challenge to encourage school age children to read six books over the holidays; a summer bookbus to visit play schemes and literacy schools; a story festival which involved 7,000 children; online workshops for budding writers; new internet based tools people can use to find new books that might interest them and a variety of local reading clubs.

<!-- PAGE: 27 -->

**4.9** Increasingly ICT is being used to support reader development. Whichbook.net, launched by Opening the Book, allows readers to select works of fiction tailored to their particular interests and preferences. New training programmes are developing. Branching Out, a collaboration between library authorities and Regional Arts Boards, provides regional programmes of activity to promote literature development. Their Reading Futures, a pilot programme funded through the DCMS/Wolfson programme has created a quality framework for planning young people's reading services. In addition, libraries are investing in research to understand better the needs of readers and the impact their reading is having on future attainment.

Chatterbooks is a national network of reading groups for 4-12 year olds, sponsored by Orange, in partnership with the public library network and was brokered by independent library development agency Launchpad. Chatterbooks aims to inspire young people to read more adventurously and develop confidence in talking about and choosing books. Orange has funded the work needed to create the network, for staff training, as well as a best practice handbook. Orange also funds the provision of high quality reading materials for all children participating in the scheme. Seventy library authorities now participate in Chatterbooks. Orange's feedback on the scheme is highly favourable. It combines corporate profile at the highest level with grassroots activity in all kinds of communities, including some very deprived ones. It also offers Orange staff the chance to get involved as volunteers.

**4.10** The case studies in this section illustrate just some of the different approaches libraries are taking to promoting books and reading. Libraries need to build on these successes. To achieve this, DCMS and Resource will explore:

Liverpool Libraries and Information Services works with adult basic skills tutors to introduce students who are reluctant readers to libraries. The library service has commissioned and published short, fast-moving, easy to read, thrillers written by a popular local author. The success of this initiative is demonstrated by the high loan rates of these books and that this has encouraged emerging readers to try other books."""

new_p26_p27 = """<!-- PAGE: 26 -->

> ### Case Study: HM Prison Service and The Big Book Share
>
> All prisons managed by HM Prison Service offer a library service provided by the public library authority. Even the most progressive regimes leave prisoners with a large amount of unoccupied time. As a consequence, reading can be an important leisure activity in prison, especially so when there is an adequate library service to support that need. The Big Book Share is a partnership between Nottingham City Libraries and Information Service, The Reading Agency, HM Prison Nottingham, Marks & Spencer plc's Community Division, East Midlands Arts and 23 children's publishers. Librarians run fortnightly sessions at the prison to help prisoners choose books and support children reading. Prisoners develop reading skills as they read with their children on visits or record a tape of stories for their children to listen to at home.

**4.8** Libraries' approach to reader development is becoming increasingly sophisticated. Library authorities are working together to create new structures enabling programmes to be delivered both regionally and nationally. The Summer Reading Challenge is one example. Until four years ago each library authority developed its own summer reading programme. This is now a national programme, co-ordinated through The Reading Agency (TRA), creating economies of scale and allowing libraries to market their services far more effectively. Another good example occurred in 2002 when The Reading Agency co-ordinated the library contribution to Splash Extra, a government programme of diversionary summer activities for young people at risk of offending. TRA worked with ten English library authorities to deliver its Splash Extra programme, in partnership with local Youth Offending Teams and youth services, which consisted of a varied and largely successful programme of reading-related multimedia arts activities throughout the summer. These reached 2,500 young people within the designated target groups, the majority of whom have never previously set foot in a library, and for whom the world of words, books and reading was unknown, alien or hostile territory.

> ### Case Study: Northamptonshire Libraries
>
> In 2001 Northamptonshire Libraries and Information Service ran a Bookstart programme for babies; a summer reading challenge to encourage school age children to read six books over the holidays; a summer bookbus to visit play schemes and literacy schools; a story festival which involved 7,000 children; online workshops for budding writers; new internet based tools people can use to find new books that might interest them and a variety of local reading clubs.

<!-- PAGE: 27 -->

**4.9** Increasingly ICT is being used to support reader development. Whichbook.net, launched by Opening the Book, allows readers to select works of fiction tailored to their particular interests and preferences. New training programmes are developing. Branching Out, a collaboration between library authorities and Regional Arts Boards, provides regional programmes of activity to promote literature development. Their Reading Futures, a pilot programme funded through the DCMS/Wolfson programme has created a quality framework for planning young people's reading services. In addition, libraries are investing in research to understand better the needs of readers and the impact their reading is having on future attainment.

> ### Case Study: Chatterbooks
>
> Chatterbooks is a national network of reading groups for 4-12 year olds, sponsored by Orange, in partnership with the public library network and was brokered by independent library development agency Launchpad. Chatterbooks aims to inspire young people to read more adventurously and develop confidence in talking about and choosing books. Orange has funded the work needed to create the network, for staff training, as well as a best practice handbook. Orange also funds the provision of high quality reading materials for all children participating in the scheme. Seventy library authorities now participate in Chatterbooks. Orange's feedback on the scheme is highly favourable. It combines corporate profile at the highest level with grassroots activity in all kinds of communities, including some very deprived ones. It also offers Orange staff the chance to get involved as volunteers.

**4.10** The case studies in this section illustrate just some of the different approaches libraries are taking to promoting books and reading. Libraries need to build on these successes. To achieve this, DCMS and Resource will explore:

> ### Case Study: Liverpool Libraries and Information Services
>
> Liverpool Libraries and Information Services works with adult basic skills tutors to introduce students who are reluctant readers to libraries. The library service has commissioned and published short, fast-moving, easy to read, thrillers written by a popular local author. The success of this initiative is demonstrated by the high loan rates of these books and that this has encouraged emerging readers to try other books."""

content = content.replace(old_p26_p27, new_p26_p27)

# Doc page 29: Learning culture, Libraries' role, March Library case study with photo
old_p29 = """<!-- PAGE: 29 -->

Learning culture Learning has to become a habit and a culture, rather than an obligation and imposition.

Learning has to start before and extend well beyond school and college.

Learners have to be able to access learning in manageable, flexible packages, suited to their needs as well as being able to enrol on terms and courses.

People with poor experience of formal education need extra encouragement and small steps to get back on the ladder of learning.

Libraries' role Libraries provide an unthreatening environment for self-motivated learning, in which people can pursue their hobbies and interests without necessarily engaging in formal courses. Libraries promote learning as exploration and self-development.

Libraries are one of the few places where young and old, school children, college students and adult learners can all participate in learning.

Libraries allow informal, individual learning, clubs and communities for learning (such as local history) as well as providing a range of short evening and daytime courses.

Libraries are \"learning start up\" organisations, they should excel at helping people get started with learning, whether those are children or adults returning to learn. Libraries should provide the foundations for a learning culture.

Learners at March Library. Courtesy of Cambridgeshire County Council Libraries and Information Service."""

new_p29 = """<!-- PAGE: 29 -->

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

content = content.replace(old_p29, new_p29)

# Doc page 30, 31, 32, 33: Peterlee, Stockton, Birmingham, Bedfordshire, Boox on the Move, Supporting older students, Adult Basic Skills Sunderland, Barnet
old_p30_to_p33 = """<!-- PAGE: 30 -->

**4.14** Libraries are an important network for lifelong, curiosity driven learning. Extensive consultation suggests the public library service should focus its activities on three main areas:

- Supporting early learning
- Supporting pupils and students
- Supporting older students.

### Supporting early learning

**4.15** Research has demonstrated the importance of early learning activities in supporting early cognitive development. Increasingly the role of libraries is being acknowledged and addressed in early years service provision. The Sure Start programme which provides co-ordinated and integrated support to young children and their families in disadvantaged areas is encouraging closer links with public libraries. Sure Start has included a target for each project, which aims to \"increase the use of libraries with parents by young children in Sure Start areas\". Involvement in Sure Start has enabled libraries to increase their early years provision -- in the past two years over one hundred and thirty early years library posts have been created.

Peterlee Sure Start is working with libraries to improve educational attainments with its \"Read and Play Club\". Peterlee Sure Start's research found that only 6.9% of the pre-school children in the district were gaining access to library services (i.e. having borrowed in the last twelve months). \"Fun\" learning materials such as books, videos and toys are provided in the Sure Start Read and Play Clubs. Each child in a Sure Start area has a personalised \"Book Worm\" library card. The Sure Start Programme works in tandem with the County Library Service. In six weeks they increased active library membership in children of 0-4 by 100%.

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
- Using the national Summer Reading Challenge to help children to continue to learn in the long school holidays and so help minimise the \"summer learning dip\" which means that the first weeks of autumn term are often taken up with remedial work. This might initially focus on the transition from primary to secondary school. Every child leaving primary school could be invited to the library Summer Reading Challenge
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

**4.26** Promoting reading and informal learning are core library activities. Libraries need to build on these successes to help create a culture of lifelong learning for all. To do that the library service needs to:"""

new_p30_to_p33 = """<!-- PAGE: 30 -->

**4.14** Libraries are an important network for lifelong, curiosity driven learning. Extensive consultation suggests the public library service should focus its activities on three main areas:

- Supporting early learning
- Supporting pupils and students
- Supporting older students.

### Supporting early learning

**4.15** Research has demonstrated the importance of early learning activities in supporting early cognitive development. Increasingly the role of libraries is being acknowledged and addressed in early years service provision. The Sure Start programme which provides co-ordinated and integrated support to young children and their families in disadvantaged areas is encouraging closer links with public libraries. Sure Start has included a target for each project, which aims to \"increase the use of libraries with parents by young children in Sure Start areas\". Involvement in Sure Start has enabled libraries to increase their early years provision -- in the past two years over one hundred and thirty early years library posts have been created.

> ### Case Study: Peterlee Sure Start
>
> Peterlee Sure Start is working with libraries to improve educational attainments with its \"Read and Play Club\". Peterlee Sure Start's research found that only 6.9% of the pre-school children in the district were gaining access to library services (i.e. having borrowed in the last twelve months). \"Fun\" learning materials such as books, videos and toys are provided in the Sure Start Read and Play Clubs. Each child in a Sure Start area has a personalised \"Book Worm\" library card. The Sure Start Programme works in tandem with the County Library Service. In six weeks they increased active library membership in children of 0-4 by 100%.

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
- Using the national Summer Reading Challenge to help children to continue to learn in the long school holidays and so help minimise the \"summer learning dip\" which means that the first weeks of autumn term are often taken up with remedial work. This might initially focus on the transition from primary to secondary school. Every child leaving primary school could be invited to the library Summer Reading Challenge
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

content = content.replace(old_p30_to_p33, new_p30_to_p33)

# Add Barnet photo at end of section 4 (page 33)
old_p33_end = """- Build up the capacity of the Reading Agency to expand reader development programmes and to broker national and regional partnerships for the delivery of learning through libraries.

<!-- PAGE: 34 -->"""

new_p33_end = """- Build up the capacity of the Reading Agency to expand reader development programmes and to broker national and regional partnerships for the delivery of learning through libraries.

![Supporting Lifelong Learning](assets/figure-033.jpg)

*Supporting Lifelong Learning. Courtesy of London Borough of Barnet Library Service.*

<!-- PAGE: 34 -->"""

content = content.replace(old_p33_end, new_p33_end)

# Add Stockton photo at start of Chapter 5 (page 34)
old_p34_start = """<!-- PAGE: 34 -->

## 5 Digital Citizenship

**5.1** Over the past five years"""

new_p34_start = """<!-- PAGE: 34 -->

## 5 Digital Citizenship

![Open Technology and UK online Centre, Stockton Central Library](assets/figure-034.jpg)

*Open Technology and UK online Centre, Stockton Central Library. Courtesy Stockton on Tees Borough Council, photographer Peter Mernagh Film & Photography.*

**5.1** Over the past five years"""

content = content.replace(old_p34_start, new_p34_start)

# Add North Yorkshire photo at end of page 40
old_p40_img = "Extending services to all areas of the local community. Courtesy of North Yorkshire County Council."
new_p40_img = """![Extending services to all areas of the local community](assets/figure-040.jpg)

*Extending services to all areas of the local community. Courtesy of North Yorkshire County Council.*"""
content = content.replace(old_p40_img, new_p40_img)

# 5. Format Appendix A (Glossary) as structured definition list
old_appendix_a = content[content.find("## Appendix A -- Glossary"):content.find("<!-- PAGE: 55 -->")]

new_appendix_a = """## Appendix A -- Glossary

- **Advisory Council on Libraries (ACL)** — The statutory body set up under the Public Libraries and Museums Act 1964 to advise the Secretary of State for Culture, Media and Sport on public libraries.
- **Annual Library Plans (ALPs)** — Introduced by DCMS in 1998. English library authorities, through their ALPs, provide DCMS with an overview of their service, details of forward attainment and assessment on the meeting of previously set targets. The planning system will change and ALPs will be streamlined from 2003 onwards.
- **Beacon Libraries** — The ODPM's Beacon Scheme is intended to encourage good practice amongst local authorities and to disseminate that practice across all authorities. One of the themes in the 2002/03 Beacon \"round\" was \"Libraries as a Community Resource\". After a rigorous assessment process, eight authorities emerged as Library Beacons.
- **Booktrust** — The national charity for books and reading in the UK. Bookstart is a national scheme, run by Booktrust, offering free books to every new child and advice to every parent.
- **The Chartered Institute of Library and Information Professionals (CILIP)** — The leading professional body for librarians and information managers in the UK, with members in all sectors private, voluntary and public, including public libraries. CILIP was formed by a merger of the Library Association and the Institute of Information Scientists in April 2002.
- **Culture Online** — A DCMS funded initiative with the aim to increase access to the arts and culture by creating a 'digital bridge' between learners and the resources of the arts and cultural sectors. COL will be delivered through 20-40 exciting new online or interactive projects created in partnership with a range of cultural and commercial organisations, between 2002 and 2004.
- **The Department for Culture, Media and Sport (DCMS)** — Has the statutory responsibility to superintend the delivery of the English public library service by local library authorities and promote its development. The Secretary of State for Culture, Media and Sport has a statutory duty under the Public Libraries and Museums Act 1964 to ensure that public library authorities in England provide a 'comprehensive and efficient' library service. The Scottish Office, the Welsh Office and Department of Culture, Arts and Leisure Northern Ireland Executive are responsible for policies affecting the library services in Scotland, Wales and Northern Ireland, respectively.
- **DCMS/Wolfson Public Libraries Challenge Fund** — A partnership between DCMS and The Wolfson Foundation to enhance the facilities and services provided by public libraries in England. The Fund ran annually between 1997 and 2002 and has provided over £13 million funding for 139 public library based projects.
- **The Department for Education and Skills (DfES)** — Established with the purpose of creating opportunity, releasing potential and achieving excellence for all. The Department delivers on a range of education issues through working closely with other government departments and cross-departmental bodies.
- **Learndirect/University for industry (Ufi)** — Ufi Limited was created in 1998 to bring about the government's vision of a 'university for industry'. Learndirect is Ufi's network of online learning and information services, which was rolled out nation-wide across England, Wales and Northern Ireland from 25 October 2000 following a successful national pilot.

<!-- PAGE: 53 -->

- **Learning and Skills Council (LSC)** — Established in April 2001, The Learning and Skills Council is responsible for funding and planning education and training for all over 16 year olds in England. The LSC works with partners, employers, learning providers, community groups and individuals to develop and implement strategies that meet the Government's aims set out in the 'Learning to Succeed' White Paper.
- **London Libraries Development Agency (LLDA)** — Created to develop and realise a co-ordinated strategic vision for all library and information services across London.
- **National Literacy Trust** — Founded in 1993, is an independent charity concerned with raising literacy standards for all age groups throughout the UK.
- **North East Museums, Libraries and Archives Council (NEMLAC)** — The regional development agency for museums, libraries and archives in North East England. It aims to facilitate sector development across the region through strategic leadership, advocacy, advice, exemplar projects and service delivery.
- **Opening the Book Ltd** — An independent company that pioneers a new approach to promoting literature from the reader's point of view. Opening the Book creates resources for readers and provides training and consultancy services to all the professions who work with readers -- librarians, booksellers, publishers, arts organisations and government departments.
- **The People's Network** — A £120 million lottery funded initiative, through the New Opportunities Fund (NOF), to set up Information and Communication Technologies (ICT) centres (£100m) in every UK public library by the end of 2002 and to train library staff (£20m) in ICT skills and learner support. In England NOF funded libraries automatically qualify for UK online centre status.
- **Public Library Service** — The public library service in England is run by 149 separate library authorities operating through 3,500 service points, including mobile services. Under the Public Libraries and Museums Act 1964 local authorities have a statutory obligation to provide a 'comprehensive and efficient' library service. Public libraries are funded through a combination of council tax revenue and the Revenue Support Grant from the Office of the Deputy Prime Minister.
- **Public Library Standards** — The monitoring arm of DCMS's public libraries planning and monitoring framework. The standards took effect from April 2001 with a three-year phase-in period and they help to define library authorities' statutory obligation to provide a library service that is 'comprehensive and efficient'. The standards are a suite of targets across a basket of core activities. Since their introduction, library authorities have notified DCMS of their performance against each of the standards through their annual library plan. With the introduction of Framework for the Future, the standards will be reviewed to make sure that they fully reflect the new strategy and do not impose an unreasonable administrative burden on local authorities to deliver quality services to meet local needs.
- **The Reading Agency (TRA)** — A library development agency working in new ways with both adult and young people's librarians to inspire a reading nation. The Reading Agency was formed by a merger of Launchpad, The Reading Partnership and Well Worth Reading in July 2002.

<!-- PAGE: 54 -->

- **Resource: The Council for Museums, Archives and Libraries** — The strategic body empowered to advise government and the library sector on the long-term development of museums, archives and libraries. Resource was created by the merger of the Museums and Galleries Commission and the Library and Information Council in April 2000. Resource is primarily funded by the DCMS. As a Non-Departmental Public Body, Resource is managed by its Board of Councillors, who are ultimately accountable to the DCMS for all of Resource's operations.
- **School Library Services** — Central services provided by local authorities to support school library provision. They provide a range of services including loan collections, collection management advice and support, and training for teachers and librarians. The Scottish Office, the Welsh Office and Department of Culture Arts and Leisure Northern Ireland Executive are responsible for policies affecting the school library services in Scotland, Wales and Northern Ireland, respectively.
- **South East Museum, Library & Archive Council (SEMLAC)** — The new regional development agency for the museum, library and archive sector in the South East.
- **Society of Chief Librarians (SCL)** — The professional association with the aim to advance the interests and influences of libraries by representing the views and interests of Chief Librarians in England and Wales.
- **Sure Start** — A cornerstone of the Government's drive to tackle poverty and social exclusion. The aim is to improve the well-being and life opportunities of young children aged 0-3 yrs through better health, childcare and educational opportunities. It does this by setting up local neighbourhood programmes, concentrated in localities where a high proportion of children are living in poverty and social exclusion, to deliver a range of services across education and health and family support.
- **UK online** — The overarching programme linking the Government's various Information Age initiatives and was launched by the Prime Minister in September 2000. The establishment of 6000 UK online centres in England by the end of 2002 is a major part of the programme and public libraries will form around a half of the UK online centre network thanks to The People's Network programme.

"""

content = content[:content.find("## Appendix A -- Glossary")] + new_appendix_a + content[content.find("<!-- PAGE: 55 -->"):]

# 6. Format Appendix B (Acknowledgments) as a clean structured list with bold names, roles, and organisations
old_appendix_b = content[content.find("## Appendix B -- Acknowledgments"):content.find("<!-- PAGE: 60 -->")]

new_appendix_b = """## Appendix B -- Acknowledgments

In July 2002 the Department for Culture, Media and Sport set up a project stakeholder group with the following terms of reference 'to guide the DCMS in the development of a new strategic framework for the public library service'. Membership of the group is set out below:

- **Alex Stewart (Chair)** — Director, Museums, Galleries, Libraries & Heritage Group, Department for Culture, Media and Sport
- **Chris Batt** — Director, Libraries and Information Society Team, Resource: The Council for Museums, Archives and Libraries
- **Tony Belmega** — Assistant Director, Policy and Development and Head of Adult Learning, Learning and Skills Council
- **Margaret Bennett** — Head of Lifelong Learning and Technologies, Department for Education and Skills
- **Jon Boagey** — Head of Information Services, National Youth Agency
- **Lyn Brown** — Chair of Cultural Services Executive, Local Government Association
- **John Hicks** — Chairman, Advisory Council on Libraries
- **Julie Hill** — Senior Project Officer, Local Government Association
- **Bill Macnaught** — Head of Cultural Development, Gateshead Council
- **Bob McKee** — Chief Executive, CILIP
- **Martin Molloy** — Director of Libraries and Heritage, Derbyshire County Council
- **Miranda McKearney** — Director, The Reading Agency
- **Neil McClelland** — Director, National Literacy Trust
- **Graham Walker** — Director of the Central Strategy Unit, Office of the e-Envoy
- **Alan Wells** — Director, The Basic Skills Agency
- **Janet Evans** — Head of Museums, Libraries and Archives Division, Department for Culture, Media and Sport
- **Mandy Barrie** — Head of Libraries and ICT Development Branch, Department for Culture, Media and Sport
- **Peter Beauchamp** — Chief Library Adviser, Department for Culture, Media and Sport
- **Roger Stratton-Smith** — Head of Local Government Team, Libraries, Local Regional and International Division, Department for Culture, Media and Sport
- **Alex Petrovic (Secretary)** — Policy Adviser, Libraries and ICT Development Branch, Department for Culture, Media and Sport

<!-- PAGE: 56 -->

The Department for Culture, Media and Sport would like to thank the members of the Advisory Council on Libraries (ACL) for their advice and guidance. Membership of the ACL is set out below:

- **John Hicks (Chairman)** — Chairman, Advisory Council on Libraries
- **Chris Batt** — Director, Libraries and Information Society Team, Resource: The Council for Museums, Archives and Libraries
- **Keith Crawshaw** — Head of Leisure Services, Sheffield City Council
- **David Ball** — Associate Head of Academic Services, Bournemouth University
- **Rob Froud** — County Librarian, Somerset County Council
- **Graham Bulpitt** — Director, Learning Centre and University Librarian, Sheffield Hallam University
- **Shelagh Levett** — Head of Arts, Library and Museum Services, Bournemouth Borough Council
- **Bob McKee** — Chief Executive, CILIP
- **Martin Molloy** — Director of Libraries and Heritage, Derbyshire County Council
- **Guenever Pachent** — Assistant Director (Libraries and Heritage), Suffolk County Council
- **David Ruse** — Assistant Director, Lifetime Learning, Westminster City Council
- **Brian Stevenson** — Commissioning Inspector, Audit Commission
- **Rob Warburton** — Assistant Head of Cultural Services, Kirklees Metropolitan District Council

The Department for Culture, Media and Sport would also like to thank the following people for their assistance in the development of the new strategic framework for public libraries:

- **David Anderson** — Director of Learning and Interpretation, Victoria and Albert Museum
- **Brian Ashley** — Assistant Director (Libraries, Information and Museums), Nottingham City Council
- **Andrea Barker** — Head of Cultural Services, Stockton on Tees Borough Council
- **Micheline Beaulieu** — Head, Department of Information Studies, The University of Sheffield
- **Greg Birdseye** — Associate Director, Public Services Research, Audit Commission
- **Catherine Blanshard** — Head of Library and Information Service, Leeds City Council
- **Eric Bohl** — Corporate Director (Customer Services), London Borough of Tower Hamlets

<!-- PAGE: 57 -->

- **Steve Bundred** — Chief Executive, London Borough of Camden
- **Tim Coates** — Independent Consultant
- **Sheila Corrall** — Director of Academic Services, The University of Southampton
- **Hilary Cottam** — Director -- Learning and Public Services, The Design Council
- **Margaret Croucher** — Research Programme Manager, Resource: The Council for Museums, Archives and Libraries
- **Kate Davenport** — Head of Libraries, Bristol City Council
- **Ray De Graff** — ICT Strategy Officer, North Yorkshire County Council
- **Jonathan Douglas** — Adviser for Youth and School Libraries, CILIP
- **Shiraz Durrani** — Strategy and Commissioning Officer, Merton Libraries, London Borough of Merton
- **Diana Edmonds** — Managing Director, Instant Library Ltd
- **Judith Elkin** — Dean of Faculty, Computing, Information and English, University of Central England
- **Annie Everall** — Service Manager, Young People & Policy Development, Derbyshire Libraries and Heritage Department
- **Ian Everall** — Black Country ICT Co-ordinator, Black Country Consortium
- **Pat Flynn** — Head of Library and Information Services, Leicester City Council
- **Tom Forrest** — Director, Opening the Book
- **Kathleen Frenchman** — Liaison Officer, Libraries for Life for Londoners
- **Fred Garnett** — Head of Community Programmes, BECTA (British Educational Communications and Technology Agency)
- **Sue Greenfield** — Divisional Librarian, Hampshire County Council
- **Viv Griffiths** — Board Member, Resource: The Council for Museums, Archives and Libraries
- **Jane Hall** — Head of Libraries, Arts and Information, Sunderland Metropolitan District Council
- **Kevin Harris** — Information Manager, Community Development Foundation
- **Ruth Harrison** — Project Manager, The Reading Agency
- **David Haynes** — Head of CILIP Consultancy Services, CILIP

<!-- PAGE: 58 -->

- **Debbie Hicks** — Policy and Strategy, The Reading Agency
- **Jennifer Holland** — Head of Libraries and Information, Norfolk County Council
- **Mike Hosking** — Head of Libraries and Information Services, Cambridgeshire County Council
- **Natasha Innocent** — Reader Development Project Manager, London Libraries Development Agency
- **Ian M. Johnson** — Head of the School of Information and Media, The Robert Gordon University, Aberdeen
- **Pam Jones** — Learning Resource Manager, Knowsley Library Service
- **Brian King** — Strategic Policy Advisor, Audit Commission Inspection Service
- **Trevor Knight** — Executive Head of Library, Heritage and Registration Services, London Borough of Sutton
- **David Lindley** — Sales and Marketing Director, Books for Students
- **Joyce Little** — Head of Libraries and Information Services, Liverpool City Council
- **Brian Loader** — Director, Community Informatics Research & Applications Unit (CIRA), University of Teesside
- **Lindsay Mackie** — Director, Diana, Princess of Wales Memorial Award for Young People
- **Peter Marchant** — Head of Libraries, Knowsley Metropolitan Borough Council
- **Roger McMaster** — County Manager for Suffolk Libraries and Heritage, Suffolk County Council
- **Norma Monks** — Assistant Director of Culture, Leisure and Sport, Blackburn with Darwen Borough Council
- **David Murray** — Director, London Libraries Development Agency
- **Julia Newton** — Head of Libraries and Information Service, London Borough of Lewisham
- **Janet O'Hehir** — Lending Time Project Director, CSV
- **John Pateman** — Head of Libraries and Heritage Services, London Borough of Merton
- **Jenny Poad** — Library Services Manager, Bedfordshire County Council
- **David Potts** — Senior Network Adviser, Resource: The Council for Museums, Archives and Libraries

<!-- PAGE: 59 -->

- **John Readman** — Head of Libraries, Archives and Arts, London Borough of Lambeth
- **Geoff Smith** — Head of Cooperation and Partnerships, The British Library
- **Rachel Smith** — Senior Policy Adviser, Central Strategy Unit, Office of the e-Envoy
- **Bjarne Stenquist** — Consultant
- **Paul Sternberg** — Education Editor, Interactive, Channel 4
- **Mark Taylor** — Library & Information Services Manager, Royal Borough of Windsor and Maidenhead
- **John Turner** — Service Manager, Nottingham Central Library
- **June Turner** — Reader Development Coordinator for Essex Libraries, Essex County Council
- **Pam Usher** — Head of Cultural Services, London Borough of Barnet
- **Bob Usherwood** — Professor of Librarianship, Department of Information Studies, The University of Sheffield
- **Rachel van Riel** — Director, Opening the Book
- **John Vincent** — Networker, The Network -- tackling social exclusion in libraries, museums, archives and galleries
- **Robert Walters** — Principal Librarian, Support Services, Bradford City Metropolitan Council
- **Heather Wills** — Idea Store Programme Director, London Borough of Tower Hamlets
- **Ken Worpole** — Independent Writer and Policy Consultant
- **Eric Wright** — County Libraries and Information Officer, Northamptonshire County Council
- **Chris Yapp** — Client Principal, HP Global Services

"""

content = content[:content.find("## Appendix B -- Acknowledgments")] + new_appendix_b + content[content.find("<!-- PAGE: 60 -->"):]

report_path.write_text(content, encoding="utf-8")
print("Successfully updated report.md with all fixes!")
