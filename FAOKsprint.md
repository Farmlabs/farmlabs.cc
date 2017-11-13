# Farmlabs.cc Dev Sprint 2017-11

## Open Sessions (General Meeting and Discussion)

### Diogo Morais (Creative Commons PT)

* the concept of multipliers (powerful stakeholders);
* Problem-oriented approach;

### João Afonso Henriques ( biovivos.pt)

* price-range on solutions;
* Agricultura Sintrópica (food forest)

### Yoad David Luxembourg (DAR / Farm Labs)

* resistance to adoption of new technology
* who is the repository for?
* how to package the content for different groups?

 ### Hernani Dias

* The importance of bringing Scientific Validation Methods to the Equation
* The importance of communities and the values be hound food production

### João Afonso Henriques

* The business and rigorous investment
* Participation yes! no extra costs.

### Joana Soares

* Plagues, Climate Change against Industrial Traditional Practices
* Resistance to change on local communities


## Existing solutions / References

### Wiki

* free-form documentation
* content links (hypertext)
* usually too chaotic (especially for novice users)
 
### Dozuki

* step by step documentation platform
* used by iFixit and Open Source Ecology
* projects > components > steps

### Public Lab

* mix of Wiki and CMS
* Questions / Tools / Research Notes
* experiment results / process documentation
* well documented [data model](https://github.com/publiclab/plots2/blob/master/doc/DATA_MODEL.md)

### Knol

* created by Google as an alternative to Wikipedia
* main concept: a knol (page) is a "unit of knowledge"
* strong authorship (same subject can have different knols, one per author)

### Stack Exchange

* Q+A model (one question -> one page of possible answers and discussion)
* strong community dynamics (points / moderation)

### Semantic Web

* graph-structured data (facts, relations, properties, ...)
* machine readable
* database interlinking
* examples
1. [Wikibase](http://wikiba.se) used by [Wikidata](https://www.wikidata.org)
2. [DBpedia](http://dbpedia.org)
3. [YAGO](http://yago-knowledge.org)
4. [Semantic MediaWiki](https://www.semantic-mediawiki.org) used by [Gardenology](http://www.gardenology.org)

## Current Work: Farmlabs Open Knowledge Platform

### Goal

An open platform for Open Agriculture knowledge creation, deployment and exchange.

### Target Users

Developers / Solution Developers ( Agro Geeks?)
Education Professionals
Recreational Farmer (Hobbyist, Urban or not)
Subsistence Farmer
Comercial Farmer (Small or Large Scale Explorations)
Coops


### Data Model
https://docs.google.com/spreadsheets/d/1dQRYaHwiaZeEd50jtiyathRS_gWHWroU8A9voK2xf0A/edit#gid=0 to test data model

The Farmlabs Open Knowledge data model has the following data types: `Challenge`, `Experiment`, `Resource` and `Media`.

A `Resource` represents a unit of Open Knowledge in the database. It has a unique `id`, a `name`, a  `description`, a `type`, a `license`and one or more `Media`items.
This unit can also be a combination of other resources(units).

Other fields / descriptors should be added in an evolutive way (p.ex: user profile, preferable implementation scales, proprietary substitute products). This would help the process of selecting resources to be used in the processes of experimentation, test and implementation to be held on local Farm Labs.

A `Media` item represents a data element (image, pdf, video, dataset, code repository, design file, etc.) which can be internal (saved within the platform) or a link to an external item.  A `Media` item has a unique `id`, a `name`, a `type` and a `url`that  points to the storage location.

An `Experiment`holds data about an ongoing research activity within the scope of the platform. It holds a chronological list of `Media` items.

A `Challenge` tracks the formulation and refinement/discussion of a domain problem faced by community members that might be solved by open collaborative research and the use of Open Knowledge resources. A `Challenge`has a unique `id`, a `name`, a `description`, and a list of `Comment` items.  

ToDo/Ideas/Open Questions:

Add a `Comment`data type that can be attached to Challenges, Experiments and Resources to allow for community feedback.
Add a `User` data type to track member data. Piggyback on an existing identity platform to avoid burdening the users with yet another account password  (e.g. use email token login like sandstorm)
Add a way to track member engagement around Challenges and maturity/quality of Resources and Experiments;
Metaphors and analogies with Agriculture and Farming might improve User Experience.

## Interface

frontend at: https://github.com/Farmlabs/farmlabs.cc

## Closing Remarks

This development session was aimed at defining what we've been assuming as a foundational tool - The Farmlabs Open Agriculture Knowledge Platform (FAOK). 

As a Farmlab will need its tools, its missions and its community we cannot not just assume that these will form out of a declaration of intentions.
The FAOK is the enabler, it will have to help the community to set the premises and choose the set of resources that will be used, tested and developed in their own version of a Farm Lab.

This team engagement on a development sprint is the corollary of the team work we've asynchronously doing throughout the last two years.
The proposal was very well received and perceived inside the Open Source, Open Hardware and Fabrication communities and some Agricultural Communities begin to demonstrate some curiosity by assuming interest on following the processes related to our proposal.
This allowed us to augment the focus of this event by including remote participations which helped us shape this first sketch we are now proposing.

#### 1- Publics, Users and implementation strategies for the Farmlabs Network and the Open Knowledge Platform:

* The Farmlabs Network should independently bind and share knowledge between different agricultural communities, types of agriculture, geographical contexts;
* This Open Knowledge Platform cannot by definition solve all the problems that arise from this global intention of the network, nevertheless, it can act as a foundational agent and consequently be structured to start gathering knowledge that will, for example, help overcome the challenges imposed by a). In this sense the tool will have to be capable of gradually receiving more contributions from a less digital literate public which can perfectly mean the average educated farmer. In this sense it should motivate this participation.

#### 2- Data Structure as the starting point:
* A lot was discussed but one idea was stated more than once: 
* A professional Farmer will only engage on something that he trusts will help him find the solution for his problems, and he is far from being able to trust a solution that looks aimed at amateurs, or geeky solutions that he can't understand, even if we feel this is an unfair appreciation. Agriculture is an overwhelming activity, full of uncertainties and natural variables.
* Our strategy proposal is based on the possibility of proving concepts. The team felt that the external participations were rich in challenges that we feel might be overcome by a structure such as a local commons managed Farmlab. In this sense, we divided the platform in three Knowledge Units: Challenges, Tools and Experiments. Farm Labs will use the Experiments to figure if the Open Tools are up for the Challenges of each community. The repository is just a documentation platform that will enable relations between this three stages of Agricultural Knowledge formation.

#### 3- The Main outcomes of the Development Sprint are on Github:
* Documentation relating to the process, interviews and participations;
* A Data Structure first proposal;
* UI first sketches;
* A preliminary version of an API ready to receive your first contribuitions, to help us map OpenAg tools
* A list of Issues (open for participation!)
* ...


## Next Challenge: Moving into the Field

#### Online Call for developers and designers;
#### Open Call for "Content Farmers";
#### Donations and Contacts form on farmlabs.org

also,
find local influencers/mediators
e.g coops
engage with "multipliers" (children and teenagers usually)

## Possible partners:

[Montenoso](http://montenoso.net)
[Latamuda/LabRural](http://latamuda.com/latamuda-arte-contemporaneo/proyectos/labrural)
[Alg-a Lab](http://www.lab.alg-a.org/en/)
Refarm the City (http://refarmthecity.org)
Algarve Farm Lab
CoHabitat.net (https://cohabitat.net/) 
ADXTUR (Aldeias do Xisto)
FabLab de Penela / FarmLab


