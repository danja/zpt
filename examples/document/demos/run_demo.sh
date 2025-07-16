#!/bin/bash

# ZPT Document Navigation Demo Runner
# This script demonstrates the ZPT document navigation system

echo "=============================================="
echo "  ZPT Document Navigation System Demo"
echo "=============================================="
echo ""

# Check if we're in the right directory
if [ ! -d "corpus" ] || [ ! -d "schemas" ] || [ ! -d "navigation" ]; then
    echo "Error: Please run this script from the examples/document/ directory"
    echo "Expected directory structure:"
    echo "  - corpus/          (sample documents)"
    echo "  - schemas/         (ZPT schemas)"
    echo "  - navigation/      (navigation examples)" 
    echo "  - demos/           (demonstration scripts)"
    exit 1
fi

echo "✅ Found required directories"
echo ""

# Count documents in corpus
doc_count=$(find corpus -name "*.json" | wc -l)
md_count=$(find corpus -name "*.md" | wc -l)

echo "📚 Document Corpus:"
echo "   - $md_count document files (.md)"
echo "   - $doc_count metadata files (.json)"
echo ""

# List available schemas
echo "📋 ZPT Schemas:"
if [ -f "schemas/document-zpt-schema.ttl" ]; then
    echo "   ✅ RDF/OWL schema (document-zpt-schema.ttl)"
fi
if [ -f "schemas/document-metadata-schema.json" ]; then
    echo "   ✅ JSON schema (document-metadata-schema.json)"
fi
echo ""

# List navigation examples
echo "🧭 Navigation Examples:"
if [ -f "navigation/pan-domain-examples.ttl" ]; then
    echo "   ✅ Pan domain examples (pan-domain-examples.ttl)"
fi
if [ -f "navigation/tilt-projection-examples.ttl" ]; then
    echo "   ✅ Tilt projection examples (tilt-projection-examples.ttl)"
fi
if [ -f "navigation/query-to-zpt-mapping.json" ]; then
    echo "   ✅ Query mapping examples (query-to-zpt-mapping.json)"
fi
echo ""

# Check for demo scripts
echo "🎮 Available Demos:"
if [ -f "demos/zpt_document_navigator.py" ]; then
    echo "   ✅ Python Navigator (zpt_document_navigator.py)"
fi
if [ -f "demos/web_interface.html" ]; then
    echo "   ✅ Web Interface (web_interface.html)"
fi
echo ""

# Menu for user interaction
while true; do
    echo "Choose a demo to run:"
    echo "  1) Show sample documents"
    echo "  2) Display ZPT schema overview"
    echo "  3) Run Python navigation demo"
    echo "  4) Open web interface"
    echo "  5) View navigation examples"
    echo "  6) Show document metadata"
    echo "  7) Exit"
    echo ""
    read -p "Enter your choice (1-7): " choice

    case $choice in
        1)
            echo ""
            echo "📄 Sample Documents:"
            echo "===================="
            for file in corpus/*.md; do
                if [ -f "$file" ]; then
                    title=$(head -1 "$file" | sed 's/^# //')
                    echo "   - $title"
                    echo "     File: $(basename "$file")"
                    echo ""
                fi
            done
            ;;
        2)
            echo ""
            echo "📋 ZPT Schema Overview:"
            echo "======================="
            echo ""
            echo "🔍 Zoom Levels (Abstraction):"
            echo "   1. EntityLevel     - Individual entities, facts, citations"
            echo "   2. UnitLevel       - Sections, paragraphs, abstracts" 
            echo "   3. TextLevel       - Complete documents"
            echo "   4. CommunityLevel  - Document clusters, topic summaries"
            echo "   5. CorpusLevel     - Entire collection overview"
            echo ""
            echo "🔄 Pan Domains (Scope):"
            echo "   - Academic Domain    - Research papers and studies"
            echo "   - Technical Domain   - API docs and technical content"
            echo "   - News Domain        - Current events and journalism"
            echo "   - Policy Domain      - Legal and regulatory documents"
            echo "   - Healthcare Domain  - Medical and health content"
            echo "   - AI Technology      - AI and machine learning focus"
            echo ""
            echo "📐 Tilt Projections (Representation):"
            echo "   - KeywordProjection    - Term-based matching"
            echo "   - EmbeddingProjection  - Semantic similarity"
            echo "   - GraphProjection      - Citation networks"
            echo "   - TemporalProjection   - Time-based ordering"
            echo ""
            ;;
        3)
            echo ""
            echo "🐍 Running Python Navigation Demo..."
            echo "===================================="
            if [ -f "demos/zpt_document_navigator.py" ]; then
                if command -v python3 &> /dev/null; then
                    cd demos
                    python3 zpt_document_navigator.py
                    cd ..
                else
                    echo "Error: Python 3 not found. Please install Python 3 to run this demo."
                fi
            else
                echo "Error: Python demo script not found."
            fi
            ;;
        4)
            echo ""
            echo "🌐 Opening Web Interface..."
            echo "=========================="
            if [ -f "demos/web_interface.html" ]; then
                if command -v xdg-open &> /dev/null; then
                    xdg-open "demos/web_interface.html"
                elif command -v open &> /dev/null; then
                    open "demos/web_interface.html"
                else
                    echo "Please open the following file in your web browser:"
                    echo "$(pwd)/demos/web_interface.html"
                fi
                echo "✅ Web interface should now be open in your browser"
            else
                echo "Error: Web interface file not found."
            fi
            ;;
        5)
            echo ""
            echo "🧭 Navigation Examples:"
            echo "======================"
            if [ -f "navigation/query-to-zpt-mapping.json" ]; then
                echo ""
                echo "Sample Query Mappings:"
                echo "---------------------"
                # Extract some example queries using jq if available, otherwise use grep
                if command -v jq &> /dev/null; then
                    jq -r '.queryToZptMapping.examples[] | "Query: \(.naturalLanguageQuery)\nZoom: \(.zptMapping.zoom.level)\nPan: \(.zptMapping.pan.domains[0].domain)\nTilt: \(.zptMapping.tilt.projection)\n"' navigation/query-to-zpt-mapping.json | head -20
                else
                    echo "Example queries from the mapping file:"
                    grep -o '"naturalLanguageQuery": "[^"]*"' navigation/query-to-zpt-mapping.json | sed 's/"naturalLanguageQuery": "//g' | sed 's/"$//g' | head -5
                fi
            else
                echo "Navigation mapping file not found."
            fi
            ;;
        6)
            echo ""
            echo "📊 Document Metadata Examples:"
            echo "=============================="
            for file in corpus/*.json; do
                if [ -f "$file" ]; then
                    echo ""
                    echo "$(basename "$file"):"
                    echo "-------------------"
                    if command -v jq &> /dev/null; then
                        jq -r '"Title: " + .title, "Type: " + .documentType, "Published: " + .publishedDate, "Keywords: " + (.keywords | join(", "))' "$file"
                    else
                        echo "Document: $(basename "$file")"
                        grep -o '"title": "[^"]*"' "$file" | sed 's/"title": "//g' | sed 's/"$//g'
                    fi
                fi
            done
            ;;
        7)
            echo ""
            echo "👋 Thank you for exploring the ZPT Document Navigation System!"
            echo ""
            echo "To learn more:"
            echo "  - Read the README.md in the parent directory"
            echo "  - Explore the schema files in schemas/"
            echo "  - Try the navigation examples in navigation/"
            echo "  - Examine the sample documents in corpus/"
            echo ""
            break
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 7."
            ;;
    esac
    echo ""
    read -p "Press Enter to continue..."
    echo ""
done