#!/usr/bin/env python3
"""
ZPT Document Navigator - Demonstration Script

This script demonstrates practical usage of the ZPT navigation system for documents.
It shows how to:
1. Parse natural language queries
2. Map queries to ZPT parameters (zoom, pan, tilt)
3. Select appropriate documents from the corpus
4. Present results with navigation context

Author: ZPT Examples
Date: 2024-06-02
"""

import json
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ZPTConfiguration:
    """Configuration for ZPT navigation parameters"""
    zoom_level: str
    pan_domains: List[str]
    tilt_projection: str
    confidence: float
    reasoning: str

@dataclass 
class NavigationResult:
    """Result of a navigation query"""
    query: str
    zpt_config: ZPTConfiguration
    selected_documents: List[str]
    optimization_score: float
    execution_time_ms: float

class DocumentCorpus:
    """Manages the document corpus and metadata"""
    
    def __init__(self, corpus_path: str = "corpus/"):
        self.corpus_path = corpus_path
        self.documents = {}
        self.load_documents()
    
    def load_documents(self):
        """Load document metadata from JSON files"""
        document_files = [
            "academic_paper_1.json",
            "academic_paper_2.json", 
            "technical_doc_1.json",
            "news_article_1.json",
            "policy_document_1.json"
        ]
        
        for filename in document_files:
            try:
                with open(f"{self.corpus_path}{filename}", 'r') as f:
                    doc_data = json.load(f)
                    self.documents[doc_data['id']] = doc_data
                logger.info(f"Loaded document: {doc_data['id']}")
            except FileNotFoundError:
                logger.warning(f"Document file not found: {filename}")
    
    def get_document(self, doc_id: str) -> Optional[Dict]:
        """Get document metadata by ID"""
        return self.documents.get(doc_id)
    
    def get_all_documents(self) -> Dict:
        """Get all documents in the corpus"""
        return self.documents

class QueryAnalyzer:
    """Analyzes natural language queries and extracts intent"""
    
    def __init__(self):
        self.domain_keywords = {
            'ai': ['AI', 'artificial intelligence', 'machine learning', 'neural networks'],
            'healthcare': ['healthcare', 'medical', 'diagnosis', 'patient', 'clinical'],
            'sustainability': ['green', 'sustainable', 'energy', 'environment', 'carbon'],
            'privacy': ['privacy', 'data protection', 'GDPR', 'regulation', 'policy'],
            'technical': ['API', 'documentation', 'code', 'programming', 'system']
        }
        
        self.temporal_keywords = {
            'recent': ['recent', 'latest', 'new', 'current', 'this year', '2024'],
            'historical': ['historical', 'past', 'evolution', 'development'],
            'specific': ['Q1', 'spring', 'january', 'march', 'april', 'june']
        }
        
        self.zoom_keywords = {
            'entity': ['facts', 'names', 'numbers', 'citations', 'specific'],
            'unit': ['section', 'paragraph', 'details', 'examples'],
            'text': ['full text', 'complete', 'entire document', 'full paper'],
            'community': ['summary', 'overview', 'introduction', 'developments'],
            'corpus': ['all documents', 'entire collection', 'complete corpus']
        }
    
    def analyze_query(self, query: str) -> Dict:
        """Analyze query and extract navigation intent"""
        query_lower = query.lower()
        
        # Detect domains
        detected_domains = []
        for domain, keywords in self.domain_keywords.items():
            if any(keyword.lower() in query_lower for keyword in keywords):
                detected_domains.append(domain)
        
        # Detect temporal aspects
        temporal_aspects = []
        for aspect, keywords in self.temporal_keywords.items():
            if any(keyword.lower() in query_lower for keyword in keywords):
                temporal_aspects.append(aspect)
        
        # Detect zoom level intent
        zoom_intent = 'community'  # default
        max_score = 0
        for level, keywords in self.zoom_keywords.items():
            score = sum(1 for keyword in keywords if keyword.lower() in query_lower)
            if score > max_score:
                max_score = score
                zoom_intent = level
        
        # Determine query type
        query_type = self._classify_query_type(query_lower)
        
        return {
            'domains': detected_domains,
            'temporal': temporal_aspects,
            'zoom_intent': zoom_intent,
            'query_type': query_type,
            'complexity': self._assess_complexity(query)
        }
    
    def _classify_query_type(self, query: str) -> str:
        """Classify the type of query"""
        if any(word in query for word in ['how', 'use', 'create', 'implement']):
            return 'technical_how_to'
        elif any(word in query for word in ['what', 'latest', 'developments', 'new']):
            return 'current_events_exploration'
        elif any(word in query for word in ['find', 'research', 'papers', 'studies']):
            return 'research_lookup'
        elif any(word in query for word in ['summary', 'overview', 'quick']):
            return 'summary_request'
        elif any(word in query for word in ['regulation', 'policy', 'law', 'act']):
            return 'policy_lookup'
        else:
            return 'topic_exploration'
    
    def _assess_complexity(self, query: str) -> str:
        """Assess query complexity based on various factors"""
        word_count = len(query.split())
        technical_terms = sum(1 for term in ['API', 'algorithm', 'framework', 'architecture'] 
                             if term in query)
        
        if word_count > 15 or technical_terms > 2:
            return 'expert'
        elif word_count > 8 or technical_terms > 0:
            return 'intermediate'
        else:
            return 'beginner'

class ZPTMapper:
    """Maps query analysis to ZPT navigation parameters"""
    
    def __init__(self):
        self.zoom_mapping = {
            'entity': 'EntityLevel',
            'unit': 'UnitLevel', 
            'text': 'TextLevel',
            'community': 'CommunityLevel',
            'corpus': 'CorpusLevel'
        }
        
        self.pan_mapping = {
            'ai': 'doc:AIDomain',
            'healthcare': 'doc:HealthcareDomain',
            'sustainability': 'doc:SustainabilityDomain',
            'privacy': 'doc:PrivacyPolicyDomain',
            'technical': 'doc:TechnicalDomain'
        }
        
        self.tilt_mapping = {
            'technical_how_to': 'KeywordProjection',
            'current_events_exploration': 'TemporalProjection',
            'research_lookup': 'EmbeddingProjection',
            'summary_request': 'TemporalProjection',
            'policy_lookup': 'KeywordProjection',
            'topic_exploration': 'EmbeddingProjection'
        }
    
    def map_to_zpt(self, query_analysis: Dict) -> ZPTConfiguration:
        """Map query analysis to ZPT configuration"""
        
        # Map zoom level
        zoom_level = self.zoom_mapping.get(query_analysis['zoom_intent'], 'CommunityLevel')
        
        # Map pan domains
        pan_domains = []
        for domain in query_analysis['domains']:
            if domain in self.pan_mapping:
                pan_domains.append(self.pan_mapping[domain])
        
        # Add temporal domains if detected
        if 'recent' in query_analysis['temporal']:
            pan_domains.append('doc:Recent2024Domain')
        
        # Default to global if no specific domains detected
        if not pan_domains:
            pan_domains = ['doc:GlobalDomain']
        
        # Map tilt projection
        tilt_projection = self.tilt_mapping.get(
            query_analysis['query_type'], 
            'EmbeddingProjection'
        )
        
        # Calculate confidence based on specificity of mapping
        confidence = self._calculate_confidence(query_analysis, pan_domains, zoom_level)
        
        # Generate reasoning
        reasoning = self._generate_reasoning(query_analysis, zoom_level, pan_domains, tilt_projection)
        
        return ZPTConfiguration(
            zoom_level=zoom_level,
            pan_domains=pan_domains,
            tilt_projection=tilt_projection,
            confidence=confidence,
            reasoning=reasoning
        )
    
    def _calculate_confidence(self, analysis: Dict, pan_domains: List[str], zoom_level: str) -> float:
        """Calculate confidence score for the mapping"""
        base_confidence = 0.7
        
        # Boost confidence for specific domain matches
        if len(analysis['domains']) > 0:
            base_confidence += 0.1
        
        # Boost for clear zoom intent
        if analysis['zoom_intent'] != 'community':
            base_confidence += 0.1
        
        # Boost for clear query type
        if analysis['query_type'] != 'topic_exploration':
            base_confidence += 0.05
        
        return min(base_confidence, 1.0)
    
    def _generate_reasoning(self, analysis: Dict, zoom: str, pan: List[str], tilt: str) -> str:
        """Generate human-readable reasoning for the mapping"""
        reasons = []
        
        # Zoom reasoning
        if zoom == 'CommunityLevel':
            reasons.append("Community level selected for overview/summary request")
        elif zoom == 'TextLevel':
            reasons.append("Text level selected for complete document access")
        elif zoom == 'UnitLevel':
            reasons.append("Unit level selected for specific sections/details")
        
        # Pan reasoning
        if len(analysis['domains']) > 0:
            reasons.append(f"Domains detected: {', '.join(analysis['domains'])}")
        
        # Tilt reasoning
        if tilt == 'KeywordProjection':
            reasons.append("Keyword projection for precise terminology matching")
        elif tilt == 'EmbeddingProjection':
            reasons.append("Embedding projection for semantic similarity")
        elif tilt == 'TemporalProjection':
            reasons.append("Temporal projection for time-based relevance")
        
        return "; ".join(reasons)

class DocumentSelector:
    """Selects documents based on ZPT configuration"""
    
    def __init__(self, corpus: DocumentCorpus):
        self.corpus = corpus
    
    def select_documents(self, zpt_config: ZPTConfiguration) -> Tuple[List[str], float]:
        """Select documents matching the ZPT configuration"""
        
        documents = self.corpus.get_all_documents()
        scored_docs = []
        
        for doc_id, doc_data in documents.items():
            score = self._calculate_document_score(doc_data, zpt_config)
            if score > 0.3:  # Minimum relevance threshold
                scored_docs.append((doc_id, score))
        
        # Sort by score and return top results
        scored_docs.sort(key=lambda x: x[1], reverse=True)
        selected_docs = [doc_id for doc_id, score in scored_docs[:5]]  # Top 5
        avg_score = sum(score for _, score in scored_docs[:5]) / len(scored_docs[:5]) if scored_docs else 0
        
        return selected_docs, avg_score
    
    def _calculate_document_score(self, doc_data: Dict, zpt_config: ZPTConfiguration) -> float:
        """Calculate relevance score for a document"""
        score = 0.0
        
        # Pan domain scoring
        pan_score = self._score_pan_domains(doc_data, zpt_config.pan_domains)
        score += pan_score * 0.4
        
        # Zoom level scoring  
        zoom_score = self._score_zoom_level(doc_data, zpt_config.zoom_level)
        score += zoom_score * 0.3
        
        # Tilt projection scoring
        tilt_score = self._score_tilt_projection(doc_data, zpt_config.tilt_projection)
        score += tilt_score * 0.3
        
        return min(score, 1.0)
    
    def _score_pan_domains(self, doc_data: Dict, pan_domains: List[str]) -> float:
        """Score document against pan domains"""
        if not pan_domains:
            return 0.5
        
        zpt_mapping = doc_data.get('zptMapping', {})
        pan_data = zpt_mapping.get('panDomains', {})
        topic_domains = pan_data.get('topicDomains', [])
        
        max_score = 0.0
        for domain_info in topic_domains:
            domain_name = f"doc:{domain_info['domain'].title()}Domain"
            if domain_name in pan_domains:
                max_score = max(max_score, domain_info.get('coverage', 0.5))
        
        return max_score
    
    def _score_zoom_level(self, doc_data: Dict, zoom_level: str) -> float:
        """Score document against zoom level requirements"""
        # For this demo, assume all documents work at all zoom levels
        # In practice, this would check document structure and granularity
        return 0.8
    
    def _score_tilt_projection(self, doc_data: Dict, tilt_projection: str) -> float:
        """Score document against tilt projection effectiveness"""
        zpt_mapping = doc_data.get('zptMapping', {})
        tilt_data = zpt_mapping.get('tiltProjections', {})
        
        projection_map = {
            'KeywordProjection': 'keywordProjection',
            'EmbeddingProjection': 'embeddingProjection',
            'GraphProjection': 'graphProjection',
            'TemporalProjection': 'temporalProjection'
        }
        
        projection_key = projection_map.get(tilt_projection)
        if projection_key and projection_key in tilt_data:
            return tilt_data[projection_key].get('effectiveness', 0.5)
        
        return 0.5

class ZPTDocumentNavigator:
    """Main navigator class that orchestrates the ZPT navigation process"""
    
    def __init__(self, corpus_path: str = "corpus/"):
        self.corpus = DocumentCorpus(corpus_path)
        self.query_analyzer = QueryAnalyzer()
        self.zpt_mapper = ZPTMapper()
        self.document_selector = DocumentSelector(self.corpus)
    
    def navigate(self, query: str) -> NavigationResult:
        """Perform ZPT navigation for a query"""
        start_time = datetime.now()
        
        logger.info(f"Processing query: {query}")
        
        # Step 1: Analyze query
        query_analysis = self.query_analyzer.analyze_query(query)
        logger.info(f"Query analysis: {query_analysis}")
        
        # Step 2: Map to ZPT parameters
        zpt_config = self.zpt_mapper.map_to_zpt(query_analysis)
        logger.info(f"ZPT configuration: {zpt_config}")
        
        # Step 3: Select documents
        selected_docs, avg_score = self.document_selector.select_documents(zpt_config)
        logger.info(f"Selected documents: {selected_docs}")
        
        # Calculate execution time
        execution_time = (datetime.now() - start_time).total_seconds() * 1000
        
        return NavigationResult(
            query=query,
            zpt_config=zpt_config,
            selected_documents=selected_docs,
            optimization_score=avg_score,
            execution_time_ms=execution_time
        )
    
    def explain_result(self, result: NavigationResult) -> str:
        """Generate human-readable explanation of the navigation result"""
        explanation = []
        explanation.append(f"Query: '{result.query}'")
        explanation.append(f"")
        explanation.append(f"ZPT Configuration:")
        explanation.append(f"  Zoom Level: {result.zpt_config.zoom_level}")
        explanation.append(f"  Pan Domains: {', '.join(result.zpt_config.pan_domains)}")
        explanation.append(f"  Tilt Projection: {result.zpt_config.tilt_projection}")
        explanation.append(f"  Confidence: {result.zpt_config.confidence:.2f}")
        explanation.append(f"  Reasoning: {result.zpt_config.reasoning}")
        explanation.append(f"")
        explanation.append(f"Selected Documents ({len(result.selected_documents)}):")
        
        for doc_id in result.selected_documents:
            doc = self.corpus.get_document(doc_id)
            if doc:
                explanation.append(f"  - {doc['title']} ({doc['documentType']})")
        
        explanation.append(f"")
        explanation.append(f"Optimization Score: {result.optimization_score:.2f}")
        explanation.append(f"Execution Time: {result.execution_time_ms:.1f}ms")
        
        return "\n".join(explanation)

def main():
    """Demonstration of the ZPT Document Navigator"""
    
    print("ZPT Document Navigator - Demonstration")
    print("=" * 50)
    
    # Initialize navigator
    navigator = ZPTDocumentNavigator()
    
    # Example queries
    demo_queries = [
        "Find recent research papers on neural network attention mechanisms",
        "What are the latest developments in AI for healthcare?", 
        "How do I use the ZPT API to create navigation views?",
        "Show me European regulations on digital privacy for AI systems",
        "What research is being done on sustainable computing?",
        "Give me a quick summary of what's new in AI this year"
    ]
    
    print(f"Loaded {len(navigator.corpus.get_all_documents())} documents")
    print()
    
    # Process each query
    for i, query in enumerate(demo_queries, 1):
        print(f"Example {i}:")
        print("-" * 30)
        
        try:
            result = navigator.navigate(query)
            print(navigator.explain_result(result))
        except Exception as e:
            print(f"Error processing query: {e}")
        
        print()
        if i < len(demo_queries):
            input("Press Enter to continue to next example...")
            print()

if __name__ == "__main__":
    main()