# ZPT API Documentation

**Version:** 1.0.0  
**Last Updated:** June 2024  
**Category:** Knowledge Navigation APIs  
**Authors:** ZPT Development Team  

## Overview

The ZPT API provides programmatic access to knowledge navigation capabilities using the Zoom-Pan-Tilt paradigm. This RESTful API enables applications to dynamically select and retrieve optimal knowledge subsets based on query requirements.

## Quick Start

### Installation

```bash
npm install zpt-client
# or
pip install zpt-python-client
```

### Basic Usage

```javascript
const ZPT = require('zpt-client');

const client = new ZPT.Client({
  endpoint: 'https://api.zpt.example.com',
  apiKey: 'your-api-key'
});

// Create a navigation view
const view = await client.createNavigationView({
  query: "What are machine learning applications?",
  zoom: ZPT.ZoomLevel.COMMUNITY,
  pan: ZPT.PanDomain.TOPIC,
  tilt: ZPT.TiltProjection.EMBEDDING
});

// Get selected corpuscles
const results = await view.getSelectedCorpuscles();
```

## API Reference

### Authentication

All API requests require authentication using an API key:

```http
Authorization: Bearer YOUR_API_KEY
```

### Endpoints

#### POST /navigation/views

Creates a new navigation view.

**Request Body:**
```json
{
  "query": "string",
  "zoomLevel": "EntityLevel|UnitLevel|TextLevel|CommunityLevel|CorpusLevel",
  "panDomain": "TopicDomain|EntityDomain|TemporalDomain|GeospatialDomain",
  "tiltProjection": "EmbeddingProjection|KeywordProjection|GraphProjection|TemporalProjection"
}
```

**Response:**
```json
{
  "id": "view-uuid",
  "status": "created",
  "optimizationScore": 0.85,
  "selectedCorpuscles": [
    {
      "id": "corpuscle-1",
      "title": "Machine Learning Overview",
      "relevanceScore": 0.92
    }
  ]
}
```

#### GET /navigation/views/{id}

Retrieves an existing navigation view.

#### PUT /navigation/views/{id}/navigate

Updates navigation parameters for an existing view.

#### DELETE /navigation/views/{id}

Deletes a navigation view.

### Navigation Parameters

#### Zoom Levels

| Level | Order | Description | Use Case |
|-------|-------|-------------|----------|
| EntityLevel | 1 | Individual entities, facts | Specific lookup |
| UnitLevel | 2 | Semantic events, summaries | Contextual details |
| TextLevel | 3 | Complete documents | Full content |
| CommunityLevel | 4 | High-level insights | Overview exploration |
| CorpusLevel | 5 | Collection metadata | System understanding |

#### Pan Domains

- **TopicDomain**: Subject-based filtering
- **EntityDomain**: Entity-centered scope
- **TemporalDomain**: Time-based boundaries
- **GeospatialDomain**: Geographic scope

#### Tilt Projections

- **EmbeddingProjection**: Vector similarity access
- **KeywordProjection**: Term-based matching
- **GraphProjection**: Structural connectivity
- **TemporalProjection**: Time-ordered access

## Error Handling

The API returns standard HTTP status codes:

- `200` - Success
- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (invalid API key)
- `404` - Not Found (view doesn't exist)
- `429` - Rate Limited
- `500` - Internal Server Error

Error responses include detailed information:

```json
{
  "error": {
    "code": "INVALID_ZOOM_LEVEL",
    "message": "Zoom level must be one of: EntityLevel, UnitLevel, TextLevel, CommunityLevel, CorpusLevel",
    "details": {
      "provided": "InvalidLevel",
      "valid_options": ["EntityLevel", "UnitLevel", "TextLevel", "CommunityLevel", "CorpusLevel"]
    }
  }
}
```

## Rate Limiting

API requests are limited to:
- 1000 requests per hour per API key
- 10 concurrent navigation views per API key

## Examples

### Academic Research Workflow

```javascript
// Start with broad exploration
const overview = await client.createNavigationView({
  query: "neural networks in healthcare",
  zoom: ZPT.ZoomLevel.COMMUNITY,
  pan: ZPT.PanDomain.TOPIC,
  tilt: ZPT.TiltProjection.KEYWORD
});

// Zoom in for details
const detailed = await overview.navigate({
  zoom: ZPT.ZoomLevel.TEXT,
  tilt: ZPT.TiltProjection.EMBEDDING
});
```

### Legal Document Discovery

```javascript
const legalSearch = await client.createNavigationView({
  query: "privacy rights in digital age",
  zoom: ZPT.ZoomLevel.UNIT,
  pan: ZPT.PanDomain.TEMPORAL,
  tilt: ZPT.TiltProjection.GRAPH
});
```

## Support

For technical support, contact: support@zpt.example.com  
Documentation: https://docs.zpt.example.com  
GitHub: https://github.com/zpt-project/api-client