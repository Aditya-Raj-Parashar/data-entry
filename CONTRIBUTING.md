# Contributing to Database Updater

Thank you for your interest in contributing to Database Updater! This document provides guidelines and information for contributors.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title**: A brief, descriptive title
- **Environment details**: Python version, OS, SQL Server version
- **Steps to reproduce**: Detailed steps that led to the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Error messages**: Full error messages or stack traces
- **Additional context**: Screenshots, configuration files (without sensitive data)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear title**: Brief description of the enhancement
- **Detailed description**: Explain the enhancement and its benefits
- **Use cases**: Real-world scenarios where this would be helpful
- **Implementation ideas**: If you have thoughts on how to implement it

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** thoroughly
4. **Update documentation** if necessary
5. **Commit your changes** with clear, descriptive messages
6. **Submit a pull request** with a clear description

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/Aditya-Raj-Parashar/data-entry.git
   cd database-updater
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Code Organization

- Keep the main logic in `database_updater.py`
- Add utility functions to separate modules if needed
- Include error handling for all database operations
- Use logging instead of print statements for debugging

### Documentation

- Update README.md for new features
- Add docstrings to new functions
- Include inline comments for complex logic
- Update requirements.txt if adding new dependencies

## Testing

Currently, the project uses basic import testing. When contributing:

- Test your code with different CSV file formats
- Test with different SQL Server configurations
- Verify error handling works correctly
- Test both Windows and SQL Server authentication methods

## Git Workflow

### Branching Strategy

- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/feature-name`: New features
- `bugfix/bug-name`: Bug fixes
- `hotfix/issue-name`: Critical fixes

### Commit Messages

Use clear, descriptive commit messages:

```
Add support for custom data types in CSV import

- Allow users to specify column data types
- Add validation for supported SQL Server types
- Update documentation with examples
```

### Pull Request Process

1. Ensure your code follows the style guidelines
2. Update documentation as needed
3. Test your changes thoroughly
4. Write a clear PR description explaining:
   - What changes were made
   - Why they were made
   - How to test them
   - Any breaking changes

## Questions?

If you have questions about contributing:

1. Check existing issues and discussions
2. Create a new issue with the "question" label
3. Be specific about what you need help with

## Recognition

Contributors will be recognized in the project documentation. Thank you for helping make Database Updater better!

## License

By contributing to Database Updater, you agree that your contributions will be licensed under the MIT License.