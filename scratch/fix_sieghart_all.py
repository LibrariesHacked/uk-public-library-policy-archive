from pathlib import Path
import re

path = Path('archive/reports/independent-library-report-for-england-2014/report.md')
content = path.read_text(encoding='utf-8')
newline = '\r\n' if '\r\n' in content else '\n'
norm = content.replace('\r\n', '\n')

# 1. Page 5: 3 Recommendations as genuine numbered list
t_recs = """Our conclusions are clear, concise and practical. We make three major recommendations:

**1.** The provision of a national digital resource for libraries, to be delivered in partnership with local authorities
**2.** The setting up of a task and finish force, led by local government, in partnership with other bodies involved in the library sector, to provide a strategic framework for England, and to help in implementing the following
**3.** The task force, to work with local authorities, to help them improve, revitalise and if necessary, change their local library service, while encouraging, appropriate to each library, increased community involvement"""

r_recs = """Our conclusions are clear, concise and practical. We make three major recommendations:

1. The provision of a national digital resource for libraries, to be delivered in partnership with local authorities
2. The setting up of a task and finish force, led by local government, in partnership with other bodies involved in the library sector, to provide a strategic framework for England, and to help in implementing the following
3. The task force, to work with local authorities, to help them improve, revitalise and if necessary, change their local library service, while encouraging, appropriate to each library, increased community involvement"""

assert t_recs in norm, "Recommendations target not found"
norm = norm.replace(t_recs, r_recs, 1)

# 2. Heading: 'For the taskforce' under '## Actions'
t_tf_head = """- To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term

For the taskforce

- To support the creation of a national digital library network"""

r_tf_head = """- To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term

### For the taskforce

- To support the creation of a national digital library network"""

assert t_tf_head in norm, "For the taskforce target not found"
norm = norm.replace(t_tf_head, r_tf_head, 1)

# 3. Action panels with underlined subheadings in blockquotes

# 3a. Digital library network (line 135)
t_act1 = """## Digital library network

ACTIONS

Central government

- To make available funding to enable local authorities to extend WiFi access, computer facilities and workforce training for all public libraries in England
- To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term

Taskforce

- To support the creation of a national digital library network, to enable:
  - Better partnership working with other agencies and online partners
  - Seamless access for the public to quality digital resources
  - Free access to e-books
- To support local authorities in their roll out of WiFi and provision of computer facilities
- To develop an agreed e-lending solution
- To develop a master brand for public libraries in England and a national promotional campaign"""

r_act1 = """## Digital library network

> ### ACTIONS
>
> <u>Central government</u>
>
> - To make available funding to enable local authorities to extend WiFi access, computer facilities and workforce training for all public libraries in England
> - To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term
>
> <u>Taskforce</u>
>
> - To support the creation of a national digital library network, to enable:
>   - Better partnership working with other agencies and online partners
>   - Seamless access for the public to quality digital resources
>   - Free access to e-books
> - To support local authorities in their roll out of WiFi and provision of computer facilities
> - To develop an agreed e-lending solution
> - To develop a master brand for public libraries in England and a national promotional campaign"""

assert t_act1 in norm, "Action 1 target not found"
norm = norm.replace(t_act1, r_act1, 1)

# 3b. Library taskforce (line 180)
t_act2 = """## Library taskforce

ACTION

Central and local government

Jointly establish a library taskforce, led by councils, in partnership with others interested in the sector: to provide leadership; to implement the recommendations and to help reinvigorate the public library service in England"""

r_act2 = """## Library taskforce

> ### ACTION
>
> <u>Central and local government</u>
>
> - Jointly establish a library taskforce, led by councils, in partnership with others interested in the sector: to provide leadership; to implement the recommendations and to help reinvigorate the public library service in England"""

assert t_act2 in norm, "Action 2 target not found"
norm = norm.replace(t_act2, r_act2, 1)

# 3c. Wider government initiatives
t_act3 = """## Wider government initiatives

ACTION

Central government

- There should be greater cross government recognition and support for libraries"""

r_act3 = """## Wider government initiatives

> ### ACTION
>
> <u>Central government</u>
>
> - There should be greater cross government recognition and support for libraries"""

assert t_act3 in norm, "Action 3 target not found"
norm = norm.replace(t_act3, r_act3, 1)

# 3d. E-lending
t_act4 = """## E-lending

ACTIONS

Central government

- To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term

Taskforce

- To develop an agreed e-lending solution"""

r_act4 = """## E-lending

> ### ACTIONS
>
> <u>Central government</u>
>
> - To seek to secure changes in European and UK copyright law to enable the Public Lending Right to include remote e-loans in its next legislative term
>
> <u>Taskforce</u>
>
> - To develop an agreed e-lending solution"""

assert t_act4 in norm, "Action 4 target not found"
norm = norm.replace(t_act4, r_act4, 1)

# 3e. Professional development
t_act5 = """## Professional development

ACTION

- Taskforce
- To encourage and develop the library workforce and especially new recruits and graduates"""

r_act5 = """## Professional development

> ### ACTION
>
> <u>Taskforce</u>
>
> - To encourage and develop the library workforce and especially new recruits and graduates"""

assert t_act5 in norm, "Action 5 target not found"
norm = norm.replace(t_act5, r_act5, 1)

# 3f. Volunteers and community-led libraries
t_act6 = """## Volunteers and community-led libraries

ACTION

Taskforce

To develop sector-led best practice guidelines to help local authorities when working with volunteers and community-led libraries"""

r_act6 = """## Volunteers and community-led libraries

> ### ACTION
>
> <u>Taskforce</u>
>
> - To develop sector-led best practice guidelines to help local authorities when working with volunteers and community-led libraries"""

assert t_act6 in norm, "Action 6 target not found"
norm = norm.replace(t_act6, r_act6, 1)

# 3g. Role of local government
t_act7 = """## Role of local government

ACTION

Local government

- Through the taskforce, to develop a culture of vigorous mutual support among local authorities through the sharing of good practice/resources and to seize the opportunities for even greater collaboration
- Through the taskforce, to consider all available options for the delivery of their library service
- Through the taskforce, to encourage more community involvement in the management of libraries through a variety of models"""

r_act7 = """## Role of local government

> ### ACTION
>
> <u>Local government</u>
>
> - Through the taskforce, to develop a culture of vigorous mutual support among local authorities through the sharing of good practice/resources and to seize the opportunities for even greater collaboration
> - Through the taskforce, to consider all available options for the delivery of their library service
> - Through the taskforce, to encourage more community involvement in the management of libraries through a variety of models"""

assert t_act7 in norm, "Action 7 target not found"
norm = norm.replace(t_act7, r_act7, 1)

# 4. Case study headings
case_studies = [
    ("City of York", "### Case Study: City of York"),
    ("Suffolk", "### Case Study: Suffolk"),
    ("Northamptonshire", "### Case Study: Northamptonshire"),
    ("Newcastle upon Tyne", "### Case Study: Newcastle upon Tyne"),
    ("Arts Council: Libraries Grants for the arts", "### Case Study: Arts Council: Libraries Grants for the Arts"),
    ("Devon", "### Case Study: Devon"),
    ("Universal Offers", "### Case Study: Universal Offers"),
    ("Enterprising libraries", "### Case Study: Enterprising Libraries"),
    ("Access to Research initiative", "### Case Study: Access to Research Initiative"),
    ("Citizens Advice Bureau", "### Case Study: Citizens Advice Bureau"),
    ("Learn My Way", "### Case Study: Learn My Way"),
    ("Cambridgeshire Learning and Skills", "### Case Study: Cambridgeshire Learning and Skills"),
]

for orig, heading in case_studies:
    # Target is exact standalone line
    target_cs = f"\n\n{orig}\n\n"
    repl_cs = f"\n\n{heading}\n\n"
    assert target_cs in norm, f"Case study '{orig}' target not found"
    norm = norm.replace(target_cs, repl_cs, 1)
    print(f"Applied heading for case study: {orig}")

if newline == '\r\n':
    final = norm.replace('\n', '\r\n')
else:
    final = norm

path.write_text(final, encoding='utf-8')
print("Successfully applied all recommendations, headings, action panels, and case study updates to the Sieghart report!")
