# Database Updater

This Python script updates a Microsoft SQL Server database by creating the database and table if they do not exist, and inserting data from a CSV file into the specified table.

## Features


- 🔗 Connects to SQL Server using Windows Authentication or SQL Server Authentication
- 🗄️ Automatically creates the database if it doesn't exist
- 📊 Creates tables with columns based on CSV file headers
- 📁 Inserts data from CSV files into the specified table
- 🛡️ Includes error handling and connection management


## Requirements

- Python 3.x
- Microsoft SQL Server (Express, Standard, or Enterprise)
- ODBC Driver 17 for SQL Server

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Aditya-Raj-Parashar/data-entry.git
   cd database-updater
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure ODBC Driver 17 for SQL Server is installed on your machine:
   - Download from [Microsoft's official page](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

## Configuration

Before running the script, update the following variables in `database_updater.py`:

```python
server = 'localhost'  # Your SQL Server instance
database = 'your_database_name'  # Database name
table_name = 'dbo.your_table_name'  # Table name
csv_file_path = 'path/to/your/file.csv'  # CSV file path
```

## Usage

### Windows Authentication (Default)
```bash
python database_updater.py
```

### SQL Server Authentication
If you need to use SQL Server authentication instead of Windows authentication, modify the connection string in the script:

```python
# Replace the existing connection_string with:
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID=your_username;PWD=your_password;"
```


## CSV File Requirements

- CSV file should have headers in the first row
- All data will be stored as NVARCHAR(255) in the database
- Ensure your CSV file doesn't contain sensitive information before committing to version control

## Error Handling

The script includes comprehensive error handling for:
- Database connection issues
- File not found errors
- SQL execution errors
- Data type conversion issues

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- Never commit CSV files containing sensitive data
- Use environment variables for database credentials in production
- Consider using connection pooling for high-volume operations



## Troubleshooting

### Common Issues

1. **ODBC Driver not found**: Ensure ODBC Driver 17 for SQL Server is installed
2. **Connection refused**: Check if SQL Server is running and accessible
3. **Authentication failed**: Verify Windows Authentication is enabled or use correct SQL Server credentials
4. **Permission denied**: Ensure the user has appropriate database creation/modification permissions

### Getting Help

If you encounter issues:
1. Check the error message in the console output
2. Verify your SQL Server configuration
3. Ensure all dependencies are installed correctly
4. Open an issue in this repository with details about the problem

## Changelog

### v1.0.0
- Initial release
- Basic CSV to SQL Server functionality
- Windows and SQL Server authentication support
- Automatic database and table creation



## License

This project is open scourced

