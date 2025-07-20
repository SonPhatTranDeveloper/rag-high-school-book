# RAG Book Prod - Vietnamese Educational AI Assistant

A production-ready RAG (Retrieval-Augmented Generation) system designed to help Vietnamese high school students (grades 10-12) with their studies by providing intelligent answers based on official textbooks from the Ministry of Education and Training.

## Overview

This system uses advanced AI to answer student questions by either retrieving relevant information from Vietnamese textbooks or providing direct answers based on general knowledge. The multi-agent architecture ensures optimal response quality and educational value.

## Features

### Core Functionality
- **Intelligent Question Classification**: Automatically determines whether to use textbook retrieval or general knowledge
- **Multi-Agent Workflow**: Specialized agents for different types of educational queries
- **Vietnamese Textbook Integration**: Supports official textbooks for grades 10, 11, and 12
- **Step-by-Step Explanations**: Detailed reasoning for better learning
- **Multi-Choice Analysis**: Comprehensive analysis of all answer options in multiple choice questions
- **Source Document References**: Provides textbook pages and images for verification

### Subject Coverage
- Mathematics (Toán)
- Literature (Ngữ văn)  
- Physics (Vật lý)
- Chemistry (Hóa học)
- Biology (Sinh học)
- History (Lịch sử)
- Geography (Địa lý)
- English (Tiếng Anh)
- Civic Education (GDCD)
- Computer Science (Tin học)

### Textbook Series Support
- **Cánh Diều** (Canh Dieu)
- **Kết nối tri thức** (Ket noi tri thuc)
- **Chân trời sáng tạo** (Chan troi sang tao)

## Architecture

### Multi-Agent System
1. **ClassifierAgent**: Analyzes questions and routes to appropriate agent
2. **RAGAgent**: Retrieves and processes textbook content for specific queries
3. **NoRAGAgent**: Handles general knowledge questions without textbook lookup
4. **ExplainerAgent**: Formats responses for optimal student comprehension

### Technology Stack
- **Backend**: Flask + Gunicorn
- **AI Framework**: LlamaIndex + OpenAI GPT-4
- **Vector Database**: Pinecone
- **Image Storage**: Cloudinary
- **Deployment**: Docker + Nginx
- **Workflow Management**: LlamaDeploy
- **Configuration**: Hydra

## Installation

### Prerequisites
- Python 3.13+
- Docker & Docker Compose
- OpenAI API key
- Pinecone API key
- Cloudinary account
- Google API key (optional)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd rag-book-prod
```

2. **Environment Configuration**
Create a `.env` file with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret
GOOGLE_API_KEY=your_google_api_key
```

3. **Install Dependencies**
```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

4. **Prepare Data**
Place your Vietnamese textbook files in the `data/` directory following the naming convention:
```
[grade]_[book_type]_[book_subject]_page_[page_number].md
```
Example: `grade_10_canh_dieu_toan_1_page_15.md`

## Usage

### Docker Deployment (Recommended)

1. **Start the application**
```bash
docker-compose up -d
```

2. **Access the API**
The application will be available at `http://localhost:80`

### Development Mode

1. **Start the LlamaDeploy workflow**
```bash
llamadeploy run --config-file src/deployment.yml
```

2. **Start the Flask server**
```bash
python src/server/wsgi.py
```

### API Endpoints

#### Query the AI Assistant
```bash
POST /query
Content-Type: application/json

{
    "query": "Việt Nam có bao nhiêu tỉnh thành?",
    "session_id": "optional_session_id"
}
```

#### Health Check
```bash
GET /health
```

#### Session Management
```bash
GET /sessions              # List all sessions
DELETE /sessions/{id}      # Delete specific session
```

### Example Queries

**Mathematics Question:**
```json
{
    "query": "Giải phương trình x² + 3x + 2 = 0"
}
```

**History Question:**
```json
{
    "query": "Nêu ý nghĩa của chiến dịch Điện Biên Phủ"
}
```

**Multiple Choice Question:**
```json
{
    "query": "Nguyên tử có cấu hình electron lớp ngoài cùng là 3s² 3p⁵ thuộc nhóm nào? A. Nhóm IA B. Nhóm IIA C. Nhóm VIIA D. Nhóm VIA"
}
```

## Configuration

The system uses Hydra for configuration management. Main configuration is in `src/config/config.yaml`:

- **LLM Settings**: Model selection, temperature, reasoning effort
- **Vector Store**: Pinecone configuration, embedding dimensions
- **Agent Prompts**: Customizable prompts for each agent
- **Data Processing**: Chunk size, overlap, similarity thresholds

## Development

### Project Structure
```
src/
├── config/          # Configuration files
├── server/          # Flask web server
├── workflow/        # Multi-agent workflow
├── utils/           # Utility functions
└── notebooks/       # Development notebooks

data/               # Textbook content
storage/            # Local storage for development
outputs/            # Generated outputs
nginx/              # Nginx configuration
```

### Adding New Content

1. Place textbook files in `data/` with proper naming convention
2. Files will be automatically indexed on first query
3. Metadata is extracted from filenames for proper categorization

### Customizing Agents

Modify agent prompts in `src/config/config.yaml` under the `prompts` section to adjust behavior for different educational contexts.

## Monitoring

- **Logs**: Available in `flask_server.log`
- **Health Check**: Use `/health` endpoint
- **Session Tracking**: Monitor active sessions via `/sessions`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is designed for educational purposes to support Vietnamese high school students in their learning journey.

## Support

For questions or issues, please refer to the documentation or create an issue in the repository.
