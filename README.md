# ⚙️ Line Sorter

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CLI](https://img.shields.io/badge/CLI-Expertise-important?style=for-the-badge)](https://en.wikipedia.org/wiki/Command-line_interface)

```markdown
A Python script that processes and sorts text files with advanced filtering options.

## Features

- Removes non-ASCII characters
- Filters out empty lines and lines containing only dashes
- Sorts lines alphabetically (case-insensitive)
- Supports both file output and console printing
- Comprehensive unit tests
- Handles large files efficiently

## Installation

### Prerequisites
- Python 3.6 or higher

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/thebasedtaka/Line-Sorter.git
   cd text-file-sorter
   ```

## Usage

### Basic Command
```bash
python linesorter.py input.txt
```

### Command Line Options

| Option | Description | Default Value |
|--------|-------------|---------------|
| `-o OUTPUT`, `--output OUTPUT` | Output file name | `sorted.txt` |
| `-p {file,console}`, `--print {file,console}` | Output destination | `file` |

### Examples

1. **Basic usage** (output to default file):
   ```bash
   python linesorter.py ShortStory.txt
   ```

2. **Output to console**:
   ```bash
   python linesorter.py ShortStory.txt -p console
   ```

3. **Custom output filename**:
   ```bash
   python linesorter.py ShortStory.txt -o custom_sorted.txt
   ```

## Testing

The project includes comprehensive unit tests using pytest.

### Running Tests
```bash
python -m pytest test_linesorter.py -v
```

### Test Coverage
- Handles non-ASCII characters correctly
- Properly removes empty lines
- Filters lines containing only dashes
- Maintains correct alphabetical sorting
- Handles file I/O errors gracefully

## File Structure

```
text-file-sorter/
├── linesorter.py          # Main processing script
├── test_linesorter.py     # Unit tests
├── ShortStory.txt         # Sample input file
├── sorted.txt            # Sample output file
├── README.md             # This documentation
└── .gitignore            # Git ignore file
```

## Implementation Details

The script performs the following operations:
1. Reads input file with UTF-8 encoding
2. Processes each line to:
   - Remove non-ASCII characters
   - Filter empty lines and dash-only lines
   - Strip whitespace
3. Sorts lines alphabetically (case-insensitive)
4. Outputs to specified destination

## Error Handling

The script handles:
- Missing input files
- Permission issues
- Encoding problems
- Invalid arguments
