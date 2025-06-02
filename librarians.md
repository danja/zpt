## ZPT for Librarians

Imagine you're exploring a vast library using a special camera. You can **zoom** in to read individual words or zoom out to see entire sections. You can **pan** left and right to explore different topics - from science to literature to history. You can **tilt** the camera to change how you see the information - perhaps through colored filters that highlight keywords, or special lenses that show connections between books.

The ZPT (Zoom-Pan-Tilt) ontology brings this camera metaphor to digital knowledge exploration. It provides a structured way to describe how people and computer systems can navigate through complex information spaces by adjusting three key dimensions:

### The Three Dimensions

**🔍 Zoom - Level of Detail**
Just like adjusting a camera's zoom, this controls how much detail you see:
- Zoom out: See broad summaries and overviews of entire topics
- Zoom in: Focus on specific facts, entities, or detailed text passages
- Examples: Individual person's name → biographical summary → full biography → entire historical period

**🔄 Pan - Domain of Interest**  
Like panning a camera across a landscape, this controls what subject areas you're looking at:
- Narrow pan: Focus tightly on one specific topic (e.g., "machine learning")
- Wide pan: Explore broadly across related topics (e.g., "artificial intelligence, computer science, automation")
- Examples: Single research paper → related papers → entire research field → interdisciplinary connections

**📐 Tilt - Information Perspective**
Like tilting a camera to change the viewing angle, this controls how information is presented:
- Different "filters" reveal different aspects of the same information
- Examples: Keyword-based view → similarity-based view → network-based view → chronological view

### Why This Matters

Traditional search gives you a fixed list of results. ZPT navigation adapts to give you exactly the right information at exactly the right level of detail for your current needs. Whether you're a student doing initial research (wide pan, zoomed out) or an expert seeking specific details (narrow pan, zoomed in), the system adjusts automatically.

## Technical Overview

ZPT extends the [Ragno ontology](http://purl.org/stuff/ragno/) for heterogeneous knowledge graphs with dynamic navigation capabilities. It integrates with standard vocabularies including SKOS (for concept organization), PROV-O (for tracking navigation history), and Dublin Core (for metadata).

### Key Concepts

#### Navigation View (`zpt:NavigationView`)
Represents a specific "snapshot" of what someone is looking at in the knowledge space. Every navigation view has three states:
- **Zoom State**: What level of abstraction is active
- **Pan State**: What domain boundaries are in focus  
- **Tilt State**: What representation method is being used

#### Navigable Corpuscles (`zpt:NavigableCorpuscle`)
Enhanced versions of Ragno's "corpuscles" (knowledge collections) that include metadata for optimal selection during navigation. The system dynamically chooses which corpuscles to present based on the current zoom-pan-tilt configuration.

#### Navigation Sessions (`zpt:NavigationSession`)
Complete workflows that track how someone moves through the knowledge space over time, creating a breadcrumb trail for both human review and system learning.

### Integration Points

**With Ragno**: ZPT zoom levels map directly to Ragno's element hierarchy (Entity → Unit → TextElement → CommunityElement → Corpus)

**With SKOS**: Navigation domains use SKOS collections, and zoom levels form SKOS concept hierarchies

**With PROV-O**: All navigation actions are tracked as provenance activities, enabling replay and analysis

## Use Cases

1. **Academic Research**: Start with broad topic exploration, progressively narrow focus as understanding develops
2. **Technical Documentation**: Navigate from system overview to specific API details based on user expertise
3. **News Analysis**: Zoom from headline summaries to detailed reporting to source documents
4. **Legal Discovery**: Pan across case types while maintaining consistent detail level for comparative analysis

## Implementation Notes

The ontology supports both human-driven navigation (through interfaces) and autonomous agent navigation (through API integration). Optimization scores help the system learn which corpuscle selections work best for different types of queries and users.

Navigation state is fully serializable, enabling bookmarking, sharing, and reproducible research workflows.

## Future Extensions

- Multi-agent collaborative navigation
- Temporal navigation (time-based zoom/pan)
- Uncertainty-aware navigation for incomplete knowledge graphs
- Cross-linguistic navigation with automatic translation tilts