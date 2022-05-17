"""
DECORATOR PATTERN EXAMPLE

We have a class - ReportBuilder. By default, it builds PDF reports.
We need to extend its behavior and make it build
reports also in DOCX, XLSX and HTML formats at the same time.

In order to achieve it, we will create a set of wrappers
which will build reports in different formats.

Note: The classes do not really build a report because the goal is to
show a decorator pattern, so they just display a message saying that the report is being built.
"""
import xmltodict

from abc import ABCMeta, abstractmethod


class ReportBuilderInterface(metaclass=ABCMeta):
    """
    This class represents an interface for report builder classes and decorators.
    Python does not support interfaces, so the interface is implemented as a class.
    """

    @abstractmethod
    def build_report(self) -> str:
        pass


class ReportBuilder(ReportBuilderInterface):
    """
    Class that builds PDF reports.
    There is a folder called "datasources" which stores data for report building.
    Class constructor takes datasource id as a parameter and
    reads the file data from that folder.
    """

    def __init__(self, file_name: str, datasource_id: str):
        """
        Constructor for ReportBuilder class objects.
        :param file_name: Name of the file.
        :param datasource_id: Id of the datasource.
        """
        self._file_name = file_name
        self._datasource_id = datasource_id

    def _prepare_data_for_report(self) -> dict:
        """
        Takes the data from datasource and converts it to Python dict.
        Protected method.
        :return: dict
        """
        with open(f"./datasources/{self._datasource_id}.xml") as xml_file:
            file_contents: str = xml_file.read()
            return dict(xmltodict.parse(file_contents)["root"])

    def build_report(self) -> str:
        """
        Prepares data for report and builds a PDF report with this data.
        """
        report_data: dict = self._prepare_data_for_report()
        return f"Creating a PDF report. File name - {self._file_name}.pdf, Report data - {report_data}"


class ReportBuilderDecorator(ReportBuilderInterface):
    """
    Base class for report building decorators.
    This class implements the same interface as ReportBuilder class.
    """

    def __init__(self, report_builder: ReportBuilderInterface):
        self._report_builder = report_builder

    def build_report(self) -> str:
        return self._report_builder.build_report()


class ReportBuilderDOCXDecorator(ReportBuilderDecorator):
    """
    Decorator class that extends the behavior of wrapped object
    and builds DOCX reports as well.
    """

    def build_report(self) -> str:
        return f"Creating a DOCX report.({self._report_builder.build_report()})"


class ReportBuilderXLSXDecorator(ReportBuilderDecorator):
    """
    Decorator class that extends the behavior of wrapped object
    and builds XLSX reports as well.
    """

    def build_report(self) -> str:
        return f"Creating a XLSX report.({self._report_builder.build_report()})"


class ReportBuilderHTMLDecorator(ReportBuilderDecorator):
    """
    Decorator class that extends the behavior of wrapped object
    and builds HTML reports as well.
    """

    def build_report(self) -> str:
        return f"Creating a HTML report.({self._report_builder.build_report()})"


if __name__ == "__main__":
    source_id: str = "ccba9f1f-0d94-4905-aeeb-5f466a84e598"
    rep_builder: ReportBuilder = ReportBuilder("decorator_example", source_id)

    # if you need to build PDF report only:
    pdf_only_report: str = rep_builder.build_report()
    print(pdf_only_report)

    # if you need to build PDF and DOCX reports the same time (same for XLSX, HTML) ->
    # just wrap the decorator around the original builder object
    pdf_and_docx_reports: str = ReportBuilderDOCXDecorator(rep_builder).build_report()
    print(pdf_and_docx_reports)

    # if you need to build all reports at the same time:
    docx_wrapped_rep_builder = ReportBuilderDOCXDecorator(rep_builder)
    html_docx_wrapped_rep_builder = ReportBuilderHTMLDecorator(docx_wrapped_rep_builder)
    xlsx_html_docx_wrapped_rep_builder = ReportBuilderXLSXDecorator(
        html_docx_wrapped_rep_builder
    )
    multiple_reports: str = xlsx_html_docx_wrapped_rep_builder.build_report()
    print(multiple_reports)

    # due to the fact that all decorators implement the same interface as the original object,
    # one decorator can wrap another decorator. It allows to combine several decorators.
