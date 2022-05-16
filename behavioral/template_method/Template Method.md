# Template Method

### When to use the pattern?
When a common algorithm should be extended by subclasses but the structure should remain the same. The pattern defines the
structure of the algorithm and lets the subclasses overwrite some of its steps.

### Example
You need to extract data from 3 different file formats (xpt, excel, csv) and return it as a pandas DataFrame. Your algorithm looks like:
1. Read data from the given bytes;
2. Round floats to 5 digits;
3. Rename all columns to uppercase.

Your base reader class (BaseReader) defines the algorithm structure in its public `read` method and lets the subclasses (`XPTReader`, `ExcelReader`, `CSVReader`)
overwrite the methods with the concrete implementation.