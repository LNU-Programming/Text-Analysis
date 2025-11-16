# Text Analysis Tool

A comprehensive Python application for analyzing text files, providing detailed statistics, visualizations, and export capabilities for literary works and documents.

## Features

### 📊 Comprehensive Text Analysis
- **Basic Statistics**: Line count, paragraph count, sentence count, word count, character count
- **Word Analysis**: Most common words, word length distribution, unique word count
- **Sentence Analysis**: Sentence length distribution, readability scores (LIX), longest/shortest sentences
- **Character Analysis**: Letter frequency, punctuation distribution, case analysis

### 📈 Visualizations
- Character type distribution pie charts
- Word frequency bar charts
- Sentence length distribution graphs
- Text composition visualizations

### 💾 Export Capabilities
- Generate detailed analysis reports in text format
- Save results to `exports/` directory
- Comprehensive statistics in easy-to-read format

## Project Structure

```
Text-Analysis/
├── data/                    # Text files for analysis
│   ├── All Shakespear Plays.txt
│   ├── Atheist Manifesto.txt
│   ├── Carmilla.txt
│   ├── Communist Manifesto.txt
│   ├── Dracula.txt
│   ├── Moby Dick.txt
│   ├── Pride and Prejudice.txt
│   └── War and Peace.txt
├── exports/                 # Generated analysis reports
├── src/                     # Source code
│   ├── main.py             # Main application entry point
│   ├── load.py             # File loading and selection
│   ├── analyse.py          # Core text analysis engine
│   ├── display.py          # Console output and statistics display
│   ├── export.py           # Report generation and export
│   └── graph.py            # Data visualization with matplotlib
└── README.md
```

## Installation

### Prerequisites
- Python 3.8+
- Required packages: `matplotlib`

### Setup
1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install matplotlib
   ```
3. Ensure text files are placed in the `data/` directory

## Usage

### Running the Application
```bash
python src/main.py
```

### Interactive Menu System
The application provides an intuitive menu-driven interface:

1. **Load a basic text file** - Select from available `.txt` files in `data/` directory
2. **Display basic statistics** - View fundamental text metrics
3. **Show word frequency analysis** - Analyze word usage patterns
4. **Display sentence analysis** - Examine sentence structure and readability
5. **Display character analysis** - Character type and frequency analysis
6. **Export results** - Generate comprehensive analysis report
7. **Exit program** - Close the application

### Example Analysis Output
- **LIX Readability Score**: Measures text complexity (Very Easy to Very Difficult)
- **Word Length Distribution**: Shows frequency of words by character count
- **Character Type Breakdown**: Letters, digits, spaces, punctuation percentages
- **Most Common Elements**: Top 10 words and letters with frequencies

## Technical Details

### Analysis Engine
The core analysis module (`analyse.py`) processes text character-by-character to provide:
- Accurate word and sentence boundary detection
- Support for contractions and special characters
- Comprehensive statistical calculations
- Readability scoring using LIX formula

### Data Flow
1. **File Loading** (`load.py`) - Interactive file selection
2. **Text Analysis** (`analyse.py`) - Statistical computation
3. **Display** (`display.py`) - Console output with ANSI formatting
4. **Visualization** (`graph.py`) - Matplotlib charts and graphs
5. **Export** (`export.py`) - Report generation

### Supported Text Formats
- Plain text files (`.txt`)
- UTF-8 encoding
- Multiple languages (basic support)
- Large files (optimized processing)

## Sample Analysis

The tool can analyze various types of texts:
- **Literature**: Shakespeare, classic novels
- **Manifestos**: Political and philosophical documents
- **Technical Documents**: Reports and academic papers

## Development

### Code Style
- Follows PEP 8 conventions
- Type hints for all function parameters and returns
- Comprehensive docstrings using Google style
- ANSI color codes for enhanced console output

### Module Architecture
- Modular design with clear separation of concerns
- Shared statistics dictionary for data passing
- Error handling with user-friendly messages
- Relative path handling for data and exports

## License

This project is licensed under the terms included in the LICENSE file.

---

*Text Analysis Tool - Developed for Introduction to Programming class, 2025*