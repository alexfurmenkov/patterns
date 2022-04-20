# Decorator

### When to use the pattern?
The ideal use case is when you need to dynamically extend behavior of an object 
and don't change the structure of that object.
Instead of creating a hierarchy of inherited classes, the pattern allows creating wrappers over the original object.

### Example
You have a class which builds reports. By default, it builds PDF reports.
Then, there was a need to be able to build reports also in DOCX, XLSX and HTML formats. 
So, you have created a base report builder class - ReportBuilder with three child classes:
ReportBuilderDocx, ReportBuilderXlsx, ReportBuilderHtml.

Later, you decided that it would be great to be able to build multiple report types simultaneously. 
In this case, the class hierarchy that you have chosen will lead to new child classes like
ReportBuilderXlsxAndDocx, ReportBuilderHtmlAndDocx etc. So, you got into a swamp of child classes.

In order to avoid lots of ReportBuilder child classes, depending on the situation, 
we will wrap the ReportBuilder object into wrappers which will build the report in the needed format. For example: 

* if we need to build a report in PDF and HTML formats, we apply HTML wrapper.
* if we need to build a report in PDF, HTML and DOCX formats, we apply HTML and DOCX wrappers.

**Dynamism is that the behavior of an object is extended without changing its structure and defining subclasses.**