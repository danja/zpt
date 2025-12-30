# ZPT Class Hierarchy Tree

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
│   ├── zpt:MicroLevel (order: 1, maps to ragno:Attribute)
│   ├── zpt:EntityLevel (order: 2, maps to ragno:Entity)
│   ├── zpt:TextLevel (order: 3, maps to ragno:TextElement)
│   ├── zpt:UnitLevel (order: 4, maps to ragno:Unit)
│   ├── zpt:CommunityLevel (order: 5, maps to ragno:CommunityElement)
│   └── zpt:CorpusLevel (order: 6, maps to ragno:Corpus)
│
├── Pan Domains (instances of zpt:PanDomain)
│   ├── zpt:TopicDomain (thematic scope)
│   ├── zpt:EntityDomain (entity-centered scope)
│   ├── zpt:TemporalDomain (time-based scope)
│   ├── zpt:GeospatialDomain (geographic scope)
│   └── zpt:CorpuscleDomain (corpuscle scope)
│
└── Tilt Projections (instances of zpt:TiltProjection)
    ├── zpt:EmbeddingProjection (vector similarity)
    ├── zpt:KeywordProjection (keyword matching)
    ├── zpt:GraphProjection (graph traversal)
    ├── zpt:TemporalProjection (time-based view)
    └── zpt:MemoryProjection (memory lens)
```

## Key Relationships

### Inheritance (rdfs:subClassOf)
- All ZPT core classes inherit from external vocabularies
- ZPT dimensions inherit from NavigationDimension
- States inherit from prov:Entity for provenance tracking

### Composition (has/with properties)
```
NavigationView
├── hasZoomState → ZoomState
│   └── atZoomLevel → ZoomLevel
├── hasPanState → PanState  
│   └── withPanDomain → PanDomain
└── hasTiltState → TiltState
    └── withTiltProjection → TiltProjection
```

### Selection (navigation properties)
```
NavigationView
├── selectedCorpuscle → NavigableCorpuscle
├── candidateCorpuscle → NavigableCorpuscle
├── navigatedBy → NavigationAgent
└── partOfSession → NavigationSession
```

## Abstraction Hierarchy

**Zoom Levels** (increasing abstraction):
```
1. MicroLevel      [attributes and fine-grained components]
2. EntityLevel     [individual entities]
3. TextLevel       [full text documents]
4. UnitLevel       [semantic events and summaries]
5. CommunityLevel  [high-level insights]
6. CorpusLevel     [most abstract - entire knowledge base]
```
