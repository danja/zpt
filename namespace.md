# ZPT Namespace Document

**Namespace URI:** http://purl.org/stuff/zpt/  
**Preferred Namespace Prefix:** zpt  
**Date:** 2025-06-02  
**Current Version:** 0.1.0  
**Editor:** Danny Ayers

## Abstract

The ZPT (Zoom-Pan-Tilt) vocabulary provides terms for describing knowledge navigation systems that use camera metaphors to control information access. The vocabulary extends the Ragno ontology for heterogeneous knowledge graphs with dynamic navigation capabilities across three dimensions: zoom (abstraction level), pan (domain scope), and tilt (representation method).

## Status of this Document

This document is a working draft. It may be updated, replaced or made obsolete by other documents at any time.

## Table of Contents

1. [Introduction](#introduction)
2. [Namespace and Conventions](#namespace-and-conventions)
3. [ZPT Class Hierarchy Tree](#zpt-class-hierarchy-tree)
4. [Classes](#classes)
5. [Properties](#properties)
6. [Individuals](#individuals)
7. [Examples](#examples)
8. [References](#references)

## Introduction

Knowledge navigation in large, heterogeneous information spaces requires sophisticated mechanisms for controlling what information is presented to users and at what level of detail. The ZPT vocabulary addresses this need by providing a framework based on three orthogonal dimensions inspired by camera control:

- **Zoom**: Controls the level of abstraction, from specific entities to broad overviews
- **Pan**: Controls the domain or topical scope of information under consideration  
- **Tilt**: Controls the method of information representation and access

The vocabulary is designed to work with the Ragno ontology for describing heterogeneous knowledge graphs, extending it with navigation-specific metadata and state management capabilities.

## Namespace and Conventions

The ZPT vocabulary is identified by the namespace URI:

    http://purl.org/stuff/zpt/

It is recommended that the prefix `zpt` be used in conjunction with this namespace URI.

This document uses the following namespace prefixes:

```
@prefix zpt: <http://purl.org/stuff/zpt/> .
@prefix ragno: <http://purl.org/stuff/ragno/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
```

## ZPT Class Hierarchy Tree

```
ZPT Knowledge Navigation Ontology
│
├── External Vocabularies
│   ├── prov:Entity
│   ├── prov:Activity  
│   ├── prov:Agent
│   ├── skos:Concept
│   ├── skos:Collection
│   ├── ragno:Element
│   └── ragno:Corpuscle
│
├── ZPT Navigation Core
│   ├── zpt:NavigationView ← prov:Entity
│   ├── zpt:NavigationSession ← prov:Activity
│   ├── zpt:NavigationAgent ← prov:Agent
│   ├── zpt:NavigationDimension ← skos:Concept
│   ├── zpt:NavigableCorpuscle ← ragno:Corpuscle
│   └── zpt:NavigableElement ← ragno:Element
│
├── ZPT Dimensions
│   ├── zpt:ZoomLevel ← zpt:NavigationDimension
│   ├── zpt:PanDomain ← skos:Collection + zpt:NavigationDimension
│   └── zpt:TiltProjection ← zpt:NavigationDimension
│
├── ZPT States
│   ├── zpt:ZoomState ← prov:Entity
│   ├── zpt:PanState ← prov:Entity
│   └── zpt:TiltState ← prov:Entity
│
├── Zoom Levels (instances of zpt:ZoomLevel)
│   ├── zpt:EntityLevel (order: 1, maps to ragno:Entity)
│   ├── zpt:UnitLevel (order: 2, maps to ragno:Unit)
│   ├── zpt:TextLevel (order: 3, maps to ragno:TextElement)
│   ├── zpt:CommunityLevel (order: 4, maps to ragno:CommunityElement)
│   └── zpt:CorpusLevel (order: 5, maps to ragno:Corpus)
│
├── Pan Domains (instances of zpt:PanDomain)
│   ├── zpt:TopicDomain (thematic scope)
│   ├── zpt:EntityDomain (entity-centered scope)
│   ├── zpt:TemporalDomain (time-based scope)
│   └── zpt:GeospatialDomain (geographic scope)
│
└── Tilt Projections (instances of zpt:TiltProjection)
    ├── zpt:EmbeddingProjection (vector similarity)
    ├── zpt:KeywordProjection (keyword matching)
    ├── zpt:GraphProjection (graph traversal)
    └── zpt:TemporalProjection (time-based view)
```

### Key Relationships

#### Inheritance (rdfs:subClassOf)
- All ZPT core classes inherit from external vocabularies
- ZPT dimensions inherit from NavigationDimension
- States inherit from prov:Entity for provenance tracking

#### Composition (has/with properties)
```
NavigationView
├── hasZoomState → ZoomState
│   └── atZoomLevel → ZoomLevel
├── hasPanState → PanState  
│   └── withPanDomain → PanDomain
└── hasTiltState → TiltState
    └── withTiltProjection → TiltProjection
```

#### Selection (navigation properties)
```
NavigationView
├── selectedCorpuscle → NavigableCorpuscle
├── candidateCorpuscle → NavigableCorpuscle
├── navigatedBy → NavigationAgent
└── partOfSession → NavigationSession
```

### Abstraction Hierarchy

**Zoom Levels** (increasing abstraction):
```
1. EntityLevel     [most specific - individual entities]
2. UnitLevel       [semantic events and summaries]  
3. TextLevel       [full text documents]
4. CommunityLevel  [high-level insights]
5. CorpusLevel     [most abstract - entire knowledge base]
```

## Classes

### Core Navigation Classes

#### zpt:NavigationView
**URI:** http://purl.org/stuff/zpt/NavigationView  
**Label:** Navigation View  
**Subclass of:** prov:Entity  
**Definition:** A specific viewport into a knowledge space defined by zoom, pan, and tilt parameters.  
**Usage Note:** Represents the current state of knowledge navigation, combining abstraction level, domain scope, and representation method. Each navigation view captures a particular configuration of the three ZPT dimensions at a specific point in time.

#### zpt:NavigationSession  
**URI:** http://purl.org/stuff/zpt/NavigationSession  
**Label:** Navigation Session  
**Subclass of:** prov:Activity  
**Definition:** A temporal sequence of navigation actions by an agent.  
**Usage Note:** Represents a complete navigation workflow with associated provenance. Sessions track the evolution of navigation views over time and can be used for analysis, replay, and learning.

#### zpt:NavigationAgent
**URI:** http://purl.org/stuff/zpt/NavigationAgent  
**Label:** Navigation Agent  
**Subclass of:** prov:Agent  
**Definition:** An entity capable of performing knowledge navigation.  
**Usage Note:** May represent human users, software agents, or autonomous systems that navigate knowledge spaces using ZPT operations.

#### zpt:NavigationDimension
**URI:** http://purl.org/stuff/zpt/NavigationDimension  
**Label:** Navigation Dimension  
**Subclass of:** skos:Concept  
**Definition:** Base class for the three dimensions of ZPT navigation.  
**Usage Note:** Abstract class that serves as the parent for zoom levels, pan domains, and tilt projections.

### State Classes

#### zpt:ZoomState
**URI:** http://purl.org/stuff/zpt/ZoomState  
**Label:** Zoom State  
**Subclass of:** prov:Entity  
**Definition:** The current zoom configuration for a navigation view.  
**Usage Note:** Captures the specific abstraction parameters active in a navigation session, including the selected zoom level and any associated parameters.

#### zpt:PanState
**URI:** http://purl.org/stuff/zpt/PanState  
**Label:** Pan State  
**Subclass of:** prov:Entity  
**Definition:** The current domain focus for a navigation view.  
**Usage Note:** Captures the specific domain boundaries active in a navigation session, defining what topics or entities are included in the current scope.

#### zpt:TiltState
**URI:** http://purl.org/stuff/zpt/TiltState  
**Label:** Tilt State  
**Subclass of:** prov:Entity  
**Definition:** The current representation method for a navigation view.  
**Usage Note:** Captures the specific projection parameters active in a navigation session, determining how information is accessed and presented.

### Dimension Classes

#### zpt:ZoomLevel
**URI:** http://purl.org/stuff/zpt/ZoomLevel  
**Label:** Zoom Level  
**Subclass of:** zpt:NavigationDimension  
**Definition:** Represents the level of abstraction in knowledge representation.  
**Usage Note:** A position on the abstraction hierarchy from detailed text to high-level summaries. Zoom levels typically correspond to different types of elements in the underlying knowledge graph.

#### zpt:PanDomain
**URI:** http://purl.org/stuff/zpt/PanDomain  
**Label:** Pan Domain  
**Subclass of:** skos:Collection, zpt:NavigationDimension  
**Definition:** Defines the conceptual boundaries of information under consideration.  
**Usage Note:** A thematic or topical scope that constrains the knowledge space being navigated. Can be defined by subject matter, entities, temporal periods, or geographic regions.

#### zpt:TiltProjection
**URI:** http://purl.org/stuff/zpt/TiltProjection  
**Label:** Tilt Projection  
**Subclass of:** zpt:NavigationDimension  
**Definition:** Defines how information is represented and accessed.  
**Usage Note:** A method for projecting knowledge into specific representational forms, such as vector embeddings, keyword indices, or graph structures.

### Ragno Integration Classes

#### zpt:NavigableCorpuscle
**URI:** http://purl.org/stuff/zpt/NavigableCorpuscle  
**Label:** Navigable Corpuscle  
**Subclass of:** ragno:Corpuscle  
**Definition:** A Ragno corpuscle enhanced with ZPT navigation metadata.  
**Usage Note:** A knowledge collection optimized for dynamic navigation with zoom-pan-tilt parameters. Includes optimization scores and positioning metadata for efficient selection during navigation.

#### zpt:NavigableElement
**URI:** http://purl.org/stuff/zpt/NavigableElement  
**Label:** Navigable Element  
**Subclass of:** ragno:Element  
**Definition:** A Ragno element with navigation positioning metadata.  
**Usage Note:** A knowledge element that can be positioned within ZPT navigation space and selected based on current navigation parameters.

## Properties

### Navigation State Properties

#### zpt:hasZoomState
**URI:** http://purl.org/stuff/zpt/hasZoomState  
**Label:** has zoom state  
**Domain:** zpt:NavigationView  
**Range:** zpt:ZoomState  
**Definition:** Links a navigation view to its current zoom configuration.  
**Usage Note:** Functional property ensuring each navigation view has exactly one zoom state at any given time.

#### zpt:hasPanState
**URI:** http://purl.org/stuff/zpt/hasPanState  
**Label:** has pan state  
**Domain:** zpt:NavigationView  
**Range:** zpt:PanState  
**Definition:** Links a navigation view to its current pan configuration.  
**Usage Note:** Functional property ensuring each navigation view has exactly one pan state at any given time.

#### zpt:hasTiltState
**URI:** http://purl.org/stuff/zpt/hasTiltState  
**Label:** has tilt state  
**Domain:** zpt:NavigationView  
**Range:** zpt:TiltState  
**Definition:** Links a navigation view to its current tilt configuration.  
**Usage Note:** Functional property ensuring each navigation view has exactly one tilt state at any given time.

### State Configuration Properties

#### zpt:atZoomLevel
**URI:** http://purl.org/stuff/zpt/atZoomLevel  
**Label:** at zoom level  
**Domain:** zpt:ZoomState  
**Range:** zpt:ZoomLevel  
**Definition:** Specifies the zoom level for a zoom state.  
**Usage Note:** Links the current zoom state to a specific level in the abstraction hierarchy.

#### zpt:withPanDomain
**URI:** http://purl.org/stuff/zpt/withPanDomain  
**Label:** with pan domain  
**Domain:** zpt:PanState  
**Range:** zpt:PanDomain  
**Definition:** Specifies the domain scope for a pan state.  
**Usage Note:** Links the current pan state to specific domain boundaries or topical constraints.

#### zpt:withTiltProjection
**URI:** http://purl.org/stuff/zpt/withTiltProjection  
**Label:** with tilt projection  
**Domain:** zpt:TiltState  
**Range:** zpt:TiltProjection  
**Definition:** Specifies the projection method for a tilt state.  
**Usage Note:** Links the current tilt state to a specific information representation method.

### Selection Properties

#### zpt:selectedCorpuscle
**URI:** http://purl.org/stuff/zpt/selectedCorpuscle  
**Label:** selected corpuscle  
**Domain:** zpt:NavigationView  
**Range:** zpt:NavigableCorpuscle  
**Definition:** Links a navigation view to corpuscles selected for the current ZPT configuration.  
**Usage Note:** Identifies the specific knowledge collections chosen by the optimization algorithm for the current navigation state.

#### zpt:candidateCorpuscle
**URI:** http://purl.org/stuff/zpt/candidateCorpuscle  
**Label:** candidate corpuscle  
**Domain:** zpt:NavigationView  
**Range:** zpt:NavigableCorpuscle  
**Definition:** Links a navigation view to corpuscles considered but not selected.  
**Usage Note:** Maintains information about alternative selections for analysis and potential fallback options.

### Optimization Properties

#### zpt:optimizationScore
**URI:** http://purl.org/stuff/zpt/optimizationScore  
**Label:** optimization score  
**Domain:** zpt:NavigableCorpuscle  
**Range:** xsd:float  
**Definition:** Overall fitness score for corpuscle selection in current navigation context.  
**Usage Note:** Composite score combining zoom relevance, pan coverage, and tilt effectiveness for ranking purposes.

#### zpt:zoomRelevance
**URI:** http://purl.org/stuff/zpt/zoomRelevance  
**Label:** zoom relevance  
**Domain:** zpt:NavigableCorpuscle  
**Range:** xsd:float  
**Definition:** Relevance score for the zoom dimension.  
**Usage Note:** Measures how well the corpuscle matches the required abstraction level (0.0 to 1.0).

#### zpt:panCoverage
**URI:** http://purl.org/stuff/zpt/panCoverage  
**Label:** pan coverage  
**Domain:** zpt:NavigableCorpuscle  
**Range:** xsd:float  
**Definition:** Coverage score for the pan dimension.  
**Usage Note:** Measures how well the corpuscle covers the specified domain scope (0.0 to 1.0).

#### zpt:tiltEffectiveness
**URI:** http://purl.org/stuff/zpt/tiltEffectiveness  
**Label:** tilt effectiveness  
**Domain:** zpt:NavigableCorpuscle  
**Range:** xsd:float  
**Definition:** Effectiveness score for the tilt dimension.  
**Usage Note:** Measures how well the corpuscle works with the specified projection method (0.0 to 1.0).

### Abstraction Properties

#### zpt:abstractionOrder
**URI:** http://purl.org/stuff/zpt/abstractionOrder  
**Label:** abstraction order  
**Domain:** zpt:ZoomLevel  
**Range:** xsd:integer  
**Definition:** Numeric ordering of abstraction levels.  
**Usage Note:** Lower numbers indicate more specific detail (1=most specific), higher numbers indicate greater abstraction. Functional property ensuring consistent ordering.

#### zpt:correspondsToRagno
**URI:** http://purl.org/stuff/zpt/correspondsToRagno  
**Label:** corresponds to ragno  
**Domain:** zpt:ZoomLevel  
**Range:** owl:Class  
**Definition:** Maps zoom levels to corresponding Ragno element types.  
**Usage Note:** Establishes the relationship between ZPT abstraction levels and the underlying Ragno knowledge graph structure.

### Process Properties

#### zpt:navigatedBy
**URI:** http://purl.org/stuff/zpt/navigatedBy  
**Label:** navigated by  
**Subproperty of:** prov:wasAssociatedWith  
**Domain:** zpt:NavigationView  
**Range:** zpt:NavigationAgent  
**Definition:** Links a navigation view to the agent performing navigation.  
**Usage Note:** Establishes provenance relationship between navigation actions and responsible agents.

#### zpt:partOfSession
**URI:** http://purl.org/stuff/zpt/partOfSession  
**Label:** part of session  
**Subproperty of:** prov:wasGeneratedBy  
**Domain:** zpt:NavigationView  
**Range:** zpt:NavigationSession  
**Definition:** Links a navigation view to its containing session.  
**Usage Note:** Groups related navigation views into coherent workflows for analysis and replay.

#### zpt:previousView
**URI:** http://purl.org/stuff/zpt/previousView  
**Label:** previous view  
**Subproperty of:** prov:wasDerivedFrom  
**Domain:** zpt:NavigationView  
**Range:** zpt:NavigationView  
**Definition:** Links to the previous navigation view in a sequence.  
**Usage Note:** Creates navigation trails for understanding user behavior and enabling undo operations.

### Query Integration Properties

#### zpt:answersQuery
**URI:** http://purl.org/stuff/zpt/answersQuery  
**Label:** answers query  
**Domain:** zpt:NavigationView  
**Range:** rdfs:Literal  
**Definition:** The natural language query that this navigation view addresses.  
**Usage Note:** Links navigation states to their originating information needs for evaluation and learning.

#### zpt:queryComplexity
**URI:** http://purl.org/stuff/zpt/queryComplexity  
**Label:** query complexity  
**Domain:** zpt:NavigationView  
**Range:** xsd:string  
**Definition:** Classification of query complexity.  
**Usage Note:** Expected values include "simple", "multi-hop", "exploratory", "comparative". Used for optimization strategy selection.

### Temporal Properties

#### zpt:navigationTimestamp
**URI:** http://purl.org/stuff/zpt/navigationTimestamp  
**Label:** navigation timestamp  
**Subproperty of:** dcterms:created  
**Domain:** zpt:NavigationView  
**Range:** xsd:dateTime  
**Definition:** Timestamp when the navigation view was created.  
**Usage Note:** Enables temporal analysis of navigation patterns and session reconstruction.

#### zpt:sessionDuration
**URI:** http://purl.org/stuff/zpt/sessionDuration  
**Label:** session duration  
**Domain:** zpt:NavigationSession  
**Range:** xsd:duration  
**Definition:** Total duration of the navigation session.  
**Usage Note:** Used for performance analysis and user experience optimization.

## Individuals

### Predefined Zoom Levels

#### zpt:EntityLevel
**URI:** http://purl.org/stuff/zpt/EntityLevel  
**Type:** zpt:ZoomLevel  
**Label:** Entity Level  
**Definition:** Focus on individual named entities and their immediate properties.  
**Abstraction Order:** 1  
**Corresponds to:** ragno:Entity

#### zpt:UnitLevel
**URI:** http://purl.org/stuff/zpt/UnitLevel  
**Type:** zpt:ZoomLevel  
**Label:** Unit Level  
**Definition:** Focus on independent semantic events and local summaries.  
**Abstraction Order:** 2  
**Corresponds to:** ragno:Unit

#### zpt:TextLevel
**URI:** http://purl.org/stuff/zpt/TextLevel  
**Type:** zpt:ZoomLevel  
**Label:** Text Level  
**Definition:** Focus on complete text documents with full detail.  
**Abstraction Order:** 3  
**Corresponds to:** ragno:TextElement

#### zpt:CommunityLevel
**URI:** http://purl.org/stuff/zpt/CommunityLevel  
**Type:** zpt:ZoomLevel  
**Label:** Community Level  
**Definition:** Focus on high-level insights and community summaries.  
**Abstraction Order:** 4  
**Corresponds to:** ragno:CommunityElement

#### zpt:CorpusLevel
**URI:** http://purl.org/stuff/zpt/CorpusLevel  
**Type:** zpt:ZoomLevel  
**Label:** Corpus Level  
**Definition:** Focus on complete knowledge base structure and metadata.  
**Abstraction Order:** 5  
**Corresponds to:** ragno:Corpus

### Predefined Tilt Projections

#### zpt:EmbeddingProjection
**URI:** http://purl.org/stuff/zpt/EmbeddingProjection  
**Type:** zpt:TiltProjection  
**Label:** Embedding Projection  
**Definition:** Information access through vector similarity in embedding space.

#### zpt:KeywordProjection
**URI:** http://purl.org/stuff/zpt/KeywordProjection  
**Type:** zpt:TiltProjection  
**Label:** Keyword Projection  
**Definition:** Information access through keyword matching and indexing.

#### zpt:GraphProjection
**URI:** http://purl.org/stuff/zpt/GraphProjection  
**Type:** zpt:TiltProjection  
**Label:** Graph Projection  
**Definition:** Information access through graph structure and connectivity.

#### zpt:TemporalProjection
**URI:** http://purl.org/stuff/zpt/TemporalProjection  
**Type:** zpt:TiltProjection  
**Label:** Temporal Projection  
**Definition:** Information access organized by temporal relationships.

### Predefined Pan Domains

#### zpt:TopicDomain
**URI:** http://purl.org/stuff/zpt/TopicDomain  
**Type:** zpt:PanDomain  
**Label:** Topic Domain  
**Definition:** Domain defined by subject matter or thematic content.

#### zpt:EntityDomain
**URI:** http://purl.org/stuff/zpt/EntityDomain  
**Type:** zpt:PanDomain  
**Label:** Entity Domain  
**Definition:** Domain defined by specific entities and their relationships.

#### zpt:TemporalDomain
**URI:** http://purl.org/stuff/zpt/TemporalDomain  
**Type:** zpt:PanDomain  
**Label:** Temporal Domain  
**Definition:** Domain defined by temporal boundaries or periods.

#### zpt:GeospatialDomain
**URI:** http://purl.org/stuff/zpt/GeospatialDomain  
**Type:** zpt:PanDomain  
**Label:** Geospatial Domain  
**Definition:** Domain defined by geographic or spatial boundaries.

## Examples

### Basic Navigation View

```turtle
ex:myNavigationView a zpt:NavigationView ;
    zpt:hasZoomState ex:zoomState1 ;
    zpt:hasPanState ex:panState1 ;
    zpt:hasTiltState ex:tiltState1 ;
    zpt:answersQuery "What are the main applications of machine learning?" ;
    zpt:queryComplexity "exploratory" ;
    zpt:navigationTimestamp "2025-06-02T14:30:00Z"^^xsd:dateTime .

ex:zoomState1 a zpt:ZoomState ;
    zpt:atZoomLevel zpt:CommunityLevel .

ex:panState1 a zpt:PanState ;
    zpt:withPanDomain ex:aiTopicDomain .

ex:tiltState1 a zpt:TiltState ;
    zpt:withTiltProjection zpt:EmbeddingProjection .
```

### Navigation Session with Multiple Views

```turtle
ex:researchSession a zpt:NavigationSession ;
    zpt:sessionDuration "PT45M"^^xsd:duration ;
    prov:startedAtTime "2025-06-02T14:00:00Z"^^xsd:dateTime ;
    prov:endedAtTime "2025-06-02T14:45:00Z"^^xsd:dateTime .

ex:view1 a zpt:NavigationView ;
    zpt:partOfSession ex:researchSession ;
    zpt:navigatedBy ex:researcher1 .

ex:view2 a zpt:NavigationView ;
    zpt:partOfSession ex:researchSession ;
    zpt:previousView ex:view1 ;
    zpt:navigatedBy ex:researcher1 .
```

### Navigable Corpuscle with Optimization Scores

```turtle
ex:mlCorpuscle a zpt:NavigableCorpuscle ;
    skos:prefLabel "Machine Learning Knowledge Collection" ;
    zpt:optimizationScore 0.85 ;
    zpt:zoomRelevance 0.9 ;
    zpt:panCoverage 0.8 ;
    zpt:tiltEffectiveness 0.85 .

ex:myNavigationView zpt:selectedCorpuscle ex:mlCorpuscle .
```

## References

- **Ragno Ontology**: http://purl.org/stuff/ragno/
- **SKOS Simple Knowledge Organization System**: https://www.w3.org/2004/02/skos/
- **PROV-O: The PROV Ontology**: https://www.w3.org/TR/prov-o/
- **Dublin Core Terms**: https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- **OWL 2 Web Ontology Language**: https://www.w3.org/TR/owl2-overview/

---

*This document was generated on 2025-06-02 and describes version 0.1.0 of the ZPT vocabulary.*